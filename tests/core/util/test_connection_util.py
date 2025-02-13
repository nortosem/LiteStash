import pytest
from litestash.core.config.root import Tables as All_Tables
from litestash.core.util.connection_util import (
    DatabaseConnections,
    GetDataConnections,
    SetDataConnections,
    DataResults,
    GetTime,
    GetConnection,
    SetConnection
)
from litestash.models import LiteStashData, LiteStashStore
from litestash.core.session import Session as Manager
from pydantic import StrictStr
from sqlalchemy.orm import Session
from typing import List, Union, Set

class MockManager:
    def get(self, database):
        return MockDatabaseSession()


class MockDatabaseSession:
    def __init__(self):
        self.session = Session()


@pytest.fixture
def db_connections():
    return DatabaseConnections()


def test_get_time():
    """Test creation & access of GetTime."""
    time = GetTime(timestamp=1234567890, microsecond=123456)
    assert time.timestamp == 1234567890
    assert time.microsecond == 123456


@pytest.fixture
def get_conn():
    return GetConnection(hash_key='key', table='table', session=Session())

@pytest.fixture
def set_conn():
    return SetConnection(data_store='store', table='table', session=Session())

def test_database_connections_init(db_conns):
    for db in db_conns.__slots__:
        assert getattr(db_conns, db) is None

def test_contains_method(db_conns):
    assert ('valid_db' in db_conns) == ('valid_db' in db_conns.__slots__)

def test_getitem_method(db_conns):
    db_name = db_conns.__slots__[0]
    setattr(db_conns, db_name, [LiteStashData()])
    assert db_conns[db_name] == [LiteStashData()]

def test_setitem_method(db_conns):
    db_name = db_conns.__slots__[0]
    db_conns[db_name] = LiteStashData()
    assert len(db_conns[db_name]) == 1

    db_conns[db_name] = [LiteStashData(), LiteStashData()]
    assert len(db_conns[db_name]) == 3

    db_conns[db_name] = LiteStashStore()
    assert len(db_conns[db_name]) == 4

def test_clear_method(db_conns):
    db_name = db_conns.__slots__[0]
    db_conns[db_name] = [LiteStashData()]
    db_conns.clear()
    for db in db_conns.__slots__:
        assert getattr(db_conns, db) is None

def test_get_method(db_conns):
    db_name = db_conns.__slots__[0]
    db_conns[db_name] = [LiteStashData()]
    assert db_conns.get(db_name) == [LiteStashData()]

def test_is_data_method(db_conns):
    assert db_conns.is_data(LiteStashData())
    assert not db_conns.is_data(LiteStashStore())

def test_is_store_method(db_conns):
    assert db_conns.is_store(LiteStashStore())
    assert not db_conns.is_store(LiteStashData())

def test_items_method(db_conns):
    db_name = db_conns.__slots__[0]
    db_conns[db_name] = [LiteStashData()]
    items = db_conns.items()
    assert items == [[db_name, [LiteStashData()]]]

def test_keys_method(db_conns):
    assert set(db_conns.keys()) == set(db_conns.__slots__)

def test_session_method():
    mock_manager = Manager()
    mock_manager.get = lambda x: type('Mock', (object,), {'session': Session()})()
    db_conns = DatabaseConnections()
    result = db_conns.session('some_db', mock_manager)
    assert isinstance(result, Session)

def test_values_method(db_conns):
    db_name = db_conns.__slots__[0]
    db_conns[db_name] = [LiteStashData()]
    assert db_conns.values() == [[LiteStashData()]]

def test_subclass_inheritance():
    assert issubclass(GetDataConnections, DatabaseConnections)
    assert issubclass(SetDataConnections, DatabaseConnections)
    assert issubclass(DataResults, DatabaseConnections)

def test_namedtuple_get_time(get_time):
    assert get_time.timestamp == 1234567890
    assert get_time.microsecond == 123456

def test_namedtuple_get_connection(get_conn):
    assert get_conn.hash_key == 'key'
    assert get_conn.table == 'table'
    assert isinstance(get_conn.session, Session)

def test_namedtuple_set_connection(set_conn):
    assert set_conn.data_store == 'store'
    assert set_conn.table == 'table'
    assert isinstance(set_conn.session, Session)
