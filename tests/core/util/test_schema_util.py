import pytest
from litestash.core.util.litestash_util import *
from litestash.models import LiteStashData
from litestash.core.config import root as r
from sqlalchemy import MetaData

def test_setup_engine():
    db_name = "test_db"
    result = setup_engine(db_name)
    assert isinstance(result, EngineAttributes)
    assert result.db_name == db_name
    assert isinstance(result.engine, Engine)
    assert result.engine.url.database.endswith(f"{db_name}.db")

# Test Cases for setup_metadata()
def test_setup_metadata_valid_engine_attr():
    engine_attr = EngineAttributes("test_db", create_engine("sqlite:///:memory:"))
    name, metadata = setup_metadata(engine_attr)
    assert name == "test_db"
    assert isinstance(metadata, MetaData)

def test_setup_metadata_invalid_engine_attr():
    engine_attr = EngineAttributes("test_db", None)
    with pytest.raises(ValueError):
        setup_metadata(engine_attr)


# Test Cases for setup_sessions()
def test_setup_sessions_valid_engine_attr():
    engine_attr = EngineAttributes("test_db", create_engine("sqlite:///:memory:"))
    setup_metadata(engine_attr)  # Create tables before setting up sessions
    name, session_factory = setup_sessions(engine_attr)
    assert name == "test_db"
    assert isinstance(session_factory, sessionmaker)
    assert isinstance(session_factory(), Session)  # Check if it creates a Session

def test_setup_sessions_invalid_engine_attr():
    engine_attr = EngineAttributes("test_db", None)
    with pytest.raises(ValueError):
        setup_sessions(engine_attr)

def test_setup_sessions_no_tables():
    engine_attr = EngineAttributes("test_db", create_engine("sqlite:///:memory:"))
    with pytest.raises(ValueError, match=SessionAttr.VALUE_ERROR.value):
        setup_sessions(engine_attr)


# Test Cases for get_hash_table()
def test_get_hash_table_valid_hashes():
    hashes = [b'0' * 17, b'5' * 17, b'a' * 17, b'z' * 17, b'A' * 17, b'Z' * 17, b'-' * 17, b'_' * 17]
    for h in hashes:
        db_name, table_name = get_hash_table(h)
        assert db_name in Tables._value2member_map_.values()  # Assert valid DB name
        # Assert valid table name based on your mapping logic

def test_get_hash_table_invalid_hash():
    with pytest.raises(ValueError, match=Utils.DB_NAME_ERROR.value):
        get_hash_table(b"g" * 17)  # Invalid hash character


# Test Cases for digest_key()
def test_digest_key():
    key = "test_key"
    result = digest_key(key)
    assert isinstance(result, str)
    assert len(result) == Utils.SIZE.value * 2  # Hex digest has double the length of digest_size

# Test Cases for allot()
def test_allot_valid_size():
    result = allot()
    assert isinstance(result, str)
    assert len(result) == 8  # Default size of 6 returns 8 characters

def test_allot_invalid_size():
    with pytest.raises(ValueError):
        allot(size=5)  # Size not divisible by 3


# Test Cases for hash_key()
def test_hash_key():
    key_digest = "test_digest"
    lot = "test_lot"
    result = hash_key(key_digest, lot)
    assert isinstance(result, str)
    # Add more specific assertions based on your hashing logic


# Test Cases for get_primary_key()
def test_get_primary_key():
    key = "test_key"
    result = get_primary_key(key, allot())
    assert isinstance(result, str)

# Test Cases for get_time()
# ... (from previous responses)

