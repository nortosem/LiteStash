import pytest
import sqlite3
import orjson
from unittest.mock import MagicMock
from sqlalchemy import event
from sqlalchemy import create_mock_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import Table, Column, Integer, String, JSON
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Engine
from sqlalchemy import MetaData
from collections import namedtuple
from datetime import datetime
from hashlib import blake2b
from secrets import base64
from secrets import SystemRandom
from litestash.logging import Log
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Pragma
from litestash.core.config.schema_conf import Sql
from litestash.core.config.litestash_conf import EngineAttr
from litestash.core.config.litestash_conf import MetaAttr
from litestash.core.config.litestash_conf import SessionAttr
from litestash.core.config.litestash_conf import EngineConf
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.litestash_conf import DataScheme
from litestash.core.util.litestash_util import *
from litestash.core.config.tables import *

@pytest.fixture
def mock_db_name(monkeypatch):
    db_name = 'test_tmp.db'
    return db_name


@pytest.fixture
def mock_engine(monkeypatch, mock_db_name):
    engine = create_engine(
        f'{EngineConf.sqlite()}tests/{mock_db_name}',
        json_deserializer=orjson,
        json_serializer=orjson,
        logging_name=f'{mock_db_name}',
        pool_logging_name=f'{mock_db_name}_pool'
    )
    return engine


db_names = [table.value for table in Tables]


@pytest.fixture
def valid_urlsafe(monkeypatch):
    #possibly a fixture or parameterized list of valid chars
    pass


def test_set_pragma_connection_not_in_use(
        monkeypatch,
        caplog,
        mock_engine
    ):
    '''Mock the connection and cursor
    Run set_pragma and verify
    '''
    event.listen(
        mock_engine,
        'connect',
        set_pragma
    )
    with mock_engine.connect() as connection:
        walmode = connection.execute(text(Pragma.journal_mode()))
        print(f'walmode: {walmode}')
        syncmode = connection.execute(text(Pragma.synchronous()))
        jsonmode = connection.execute(text(Pragma.valid_json()))

    log_messages = caplog.text
    assert f"Set PRAGMA on" in log_messages
    assert f"journal_mode" in log_messages
    assert f"PRAGMA journal_mode=WAL" in log_messages
    assert f"synchronous" in log_messages
    assert f"PRAGMA synchronous=NORMAL" in log_messages
    assert f"valid_json" in log_messages
    assert f"PRAGMA json_valid = 1" in log_messages
    assert f"db_connection isolation set to None" in log_messages
    assert f"last_connect:" in log_messages


def test_set_begin(
        monkeypatch,
        caplog,
        mock_engine
    ):
    '''Verify BEGIN workaround function'''
    event.listen(
        mock_engine,
        'begin',
        set_begin
    )
    with mock_engine.connect() as connection:
        connection.execute(text('PRAGMA cache_size'))

    assert Sql.BEGIN.value in caplog.text


#@pytest.mark.parametrize("env_value", [
#    Log.DEV.value,
#    Log.PROD.value)
#])
@pytest.mark.parametrize("db_name", db_names)
def test_setup_engine(
    monkeypatch,
    caplog,
    db_name
 #       env_value,
 #       valid_echo,
 #       mock_setup_engine
):
    result = setup_engine(db_name)
    assert isinstance(result, tuple)
    engine_attributes = EngineAttributes(*result)
    assert isinstance(engine_attributes, EngineAttributes)
    assert engine_attributes.db_name == db_name
    assert isinstance(engine_attributes.engine, Engine)
    assert engine_attributes.engine.url.database.endswith(f"{db_name}.db")


def test_setup_metadata_valid_engine_attr(
        monkeypatch,
        caplog,
    ):
    db_name = "test_db"
    engine_attributes = EngineAttributes(db_name, setup_engine(db_name))
    meta_attributes = setup_metadata(engine_attributes)
    print(f'meta_attributes: {meta_attributes}')
    name, metadata = MetaAttributes(meta_attributes)
    assert name == "test_db"
    assert isinstance(metadata, MetaData)


def test_setup_metadata_invalid_engine_attr(
        monkeypatch,
        caplog,
    ):
    engine_attr = EngineAttributes("test_db", None)
    with pytest.raises(ValueError):
        setup_metadata(engine_attr)


def test_setup_sessions_valid_engine_attr(
        monkeypatch,
        caplog,
    ):
    engine_attr = EngineAttributes("test_db", create_engine("sqlite:///:memory:"))
    setup_metadata(engine_attr)
    name, session_factory = setup_sessions(engine_attr)
    assert name == "test_db"
    assert isinstance(session_factory, sessionmaker)
    assert isinstance(session_factory(), Session)


def test_setup_sessions_invalid_engine_attr(
        monkeypatch,
        caplog,
    ):
    engine_attr = EngineAttributes("test_db", None)
    with pytest.raises(ValueError):
        setup_sessions(engine_attr)


def test_allot(monkeypatch):
    new_size = 9 # size in bytes
    test_lot_default = allot()
    test_lot_new_size = allot(new_size)
    assert test_lot_default != test_lot_new_size
    assert len(test_lot_default) == 8
    assert len(test_lot_new_size) == 12


def test_digest_key():
    test_key = 'my_key'
    test_hex_digest = digest_key(test_key).hex()
    test_hex_digest_two = digest_key('my_key').hex()
    assert isinstance(digest_key(test_key), bytes)
    assert test_hex_digest == test_hex_digest_two


def test_mk_hash():
    test_key = 'tester'
    test_hash = mk_hash(test_key.encode())
    assert isinstance(test_hash, str)
    assert base64.urlsafe_b64decode(test_hash.encode()).decode() == test_key


def test_get_primary_key():
    test_key = 'testKey'
    test_digest = digest_key(test_key)
    test_hash = mk_hash(test_digest)
    test_pk = get_primary_key(test_key)
    assert isinstance(test_pk, str)
    assert test_pk == test_hash

def test_get_time():
    result = get_time()
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)  # timestamp
    assert isinstance(result[1], int)  # microseconds


# get_datastore test
valid_key = "valid_key"
valid_value = {"data": "some_value"}
invalid_key = ""

@pytest.fixture
def valid_data():
    return LiteStashData(key=valid_key, value=valid_value)

"""
@pytest.fixture(autouse=True)
def mock_dependencies():
    with patch("litestash.core.util.litestash_util.get_primary_key") as mock_get_primary_key:
        with patch("litestash.core.util.litestash_util.get_time") as mock_get_time:
            mock_get_primary_key.return_value = "hashed_key"
            mock_get_time.return_value = GetTime(1234567890, 123456)
            yield


def test_get_datastore_valid_data(valid_data):
    result = get_datastore(valid_data)
    assert isinstance(result, LiteStashStore)
    assert result.key_hash == "hashed_key"
    assert result.key == valid_key
    assert result.value == valid_value
    assert result.timestamp == 1234567890
    assert result.microsecond == 123456

def test_get_datastore_invalid_key_empty():
    with pytest.raises(ValueError):
        get_datastore(LiteStashData(key=invalid_key, value=valid_value))

def test_get_datastore_invalid_value_none():
    with pytest.raises(ValueError):
        get_datastore(LiteStashData(key=valid_key, value=None))


# get_keys && get_values test
class MockSession:
    def __init__(self):
        self.results = []

    def execute(self, statement):
        return self

    def scalars(self):
        return self

    def all(self):
        return self.results


class MockTable:
    def __init__(self, columns):
        self.columns = columns
        self.c = {col.name: col for col in columns}


@pytest.fixture
def mock_session_with_keys():
    session = MockSession()
    session.results = ["key1", "key2", "key3"]
    return session


@pytest.fixture
def mock_session_with_values():
    session = MockSession()
    session.results = [{"value1": 1}, {"value2": 2}, {"value3": 3}]
    return session


@pytest.fixture
def sample_table():
    columns = [
        Column("id", Integer, primary_key=True),
        Column("key", String),
        Column("value", JSON),
    ]
    return MockTable(columns)


def test_get_keys_valid_table(mock_session_with_keys, sample_table):
    keys = get_keys(mock_session_with_keys, sample_table)
    assert keys == ["key1", "key2", "key3"]
    mock_session_with_keys.execute.assert_called_once_with(
        text("SELECT key_value_store.key FROM key_value_store")
    )


def test_get_keys_empty_table():
    session = MockSession()
    session.results = []
    table = MockTable([])
    keys = get_keys(session, table)
    assert keys == []

def test_get_values_valid_table(mock_session_with_values, sample_table):
    values = get_values(mock_session_with_values, sample_table)
    assert values == [{"value1": 1}, {"value2": 2}, {"value3": 3}]
    mock_session_with_values.execute.assert_called_once_with(
        text("SELECT key_value_store.value FROM key_value_store")
    )


def test_get_values_empty_table():
    session = MockSession()
    session.results = []
    table = MockTable([])
    values = get_values(session, table)
    assert values == []
"""
