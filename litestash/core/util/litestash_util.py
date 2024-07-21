"""LiteStash Utility Module

This module provides essential utility functions for the LiteStash key-value
store.

Functions:

- `setup_engine`: Creates a SQLAlchemy engine for a given database.
- `setup_metadata`: Sets up database metadata and tables.
- `setup_sessions`: Creates a session factory for a database.
- `set_pragma`: Configures SQLite PRAGMAs for the engine.
- `set_begin`: Begins a transaction with a specified isolation level.
- `digest_key`: Generates a hexadecimal digest of a key.
- `allot`: Creates a random string for key distribution.
- `mk_hash`: Generates a hash for a key.
- `get_primary_key`: Generates a primary database key for a key-value pair.
- `get_time`: Gets the current time as a Unix timestamp and microseconds.
- `get_datastore`: Creates a LiteStashStore object from LiteStashData.
- `get_keys`: Retrieves all keys from a table.
- `get_values`: Retrieves all values from a table.

"""
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy import select
from sqlalchemy import inspect
from sqlalchemy import Engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm.session import Session
from collections import namedtuple
from pathlib import Path
from datetime import datetime
from hashlib import blake2b
from secrets import base64
from secrets import SystemRandom
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
from litestash.core.config.litestash_conf import EngineAttr
from litestash.core.config.litestash_conf import MetaAttr
from litestash.core.config.litestash_conf import SessionAttr
from litestash.core.config.litestash_conf import TimeAttr
from litestash.core.config.litestash_conf import EngineConf
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.schema_conf import Pragma
from litestash.core.config.schema_conf import ColumnSetup as C
from litestash.core.util.schema_util import mk_tables

def set_pragma(db_connection, connect):
    """Sets SQLite PRAGMA settings on a new connection.
    This function is intended to be used as an event listener with SQLAlchemy
    engines to configure essential PRAGMA settings like journaling mode,
    synchronous mode, foreign key enforcement, and JSON handling.

    Args:
        dbapi_connection: The raw DBAPI connection object
        (e.g., sqlite3.Connection).

        connection_record:  The SQLAlchemy connection record
        (not used in this implementation).
    """
    print(f'connection: {connect}')
    cursor = db_connection.cursor()
    cursor.execute(Pragma.journal_mode())
    cursor.execute(Pragma.synchronous())
    cursor.execute(Pragma.valid_json())
    cursor.close()
    db_connection.isolation_level = None


def set_begin(db_connection):
    """Explicitly begins a transaction with a BEGIN statement.

    This is a workaround for the default behavior of the pysqlite driver,
    which can interfere with SQLAlchemy's transaction management. By emitting
    our own BEGIN, we ensure correct transactional behavior.

    Args:
        dbapi_connection: The raw DBAPI connection object.
    """
    db_connection.exec_driver_sql(Pragma.BEGIN.value)


def setup_engine(db_name: str) -> Engine:
    """Sets up a SQLAlchemy engine for the given database.

    Args:
        db_name: The name of the database file.

    Returns:
        EngineAttributes: A namedtuple containing the database name and the
        engine.
    """
    data_path = Path(
        f'{EngineConf.dirname()}/{db_name}'
    )
    data_path.mkdir(parents=True, exist_ok=True)

    engine = create_engine(
        f'{EngineConf.sqlite()}{data_path}/{db_name}.db',
        echo=EngineConf.no_echo(),
        echo_pool=EngineConf.no_echo(),
        pool_size=EngineConf.pool_size(),
        max_overflow=EngineConf.max_overflow(),
        pool_logging_name=db_name,
    )
    event.listen(
        engine,
        Pragma.CONNECT.value,
        set_pragma
    )
    event.listen(
        engine,
        Pragma.BEGIN.value.lower(),
        set_begin
    )
    quality_engine = EngineAttributes(db_name, engine)
    return quality_engine


EngineAttributes = namedtuple(
    EngineAttr.TYPE_NAME.value,
    [
        EngineAttr.DB_NAME.value,
        EngineAttr.ENGINE.value
    ]
)
EngineAttributes.__doc__ = EngineAttr.DOC.value


def setup_metadata(engine_stash: EngineAttributes):
    """Sets up and returns SQLAlchemy metadata for the given database engine.

    Args:
        engine_stash: A namedtuple containing the database name
        (`db_name`) and SQLAlchemy `Engine` object.

    Returns:
        MetaAttributes: A namedtuple containing the database name and the
        initialized `MetaData` object.
    """
    metadata = MetaData()
    metadata = mk_tables(engine_stash.db_name, metadata)
    metadata.create_all(bind=engine_stash.engine, checkfirst=True)
    quality_metadata = MetaAttributes(engine_stash.db_name, metadata)
    return quality_metadata


MetaAttributes = namedtuple(
    MetaAttr.TYPE_NAME.value,
    [
        MetaAttr.DB_NAME.value,
        MetaAttr.METADATA.value
    ]
)
MetaAttributes.__doc__ = MetaAttr.DOC.value


def setup_sessions(engine_stash: EngineAttributes):
    """Creates and returns a session factory for the given database engine.

    This function checks if the database has tables before creating the session
    factory.
    If no tables are found, it raises a `ValueError`.

    Args:
        engine_stash: A namedtuple containing the database name
        (`db_name`) and SQLAlchemy `Engine` object.

    Returns:
        SessionAttributes: A namedtuple containing the database name and the
        session factory.

    Raises:
        ValueError: If no tables are found in the database.
    """
    if inspect(engine_stash.engine).get_table_names():
        session = sessionmaker(engine_stash.engine)
    else:
        raise ValueError(f'{SessionAttr.VALUE_ERROR.value}')
    quality_session = SessionAttributes(engine_stash.db_name, session)
    return quality_session


SessionAttributes = namedtuple(
    SessionAttr.TYPE_NAME.value,
    [
        SessionAttr.DB_NAME.value,
        SessionAttr.SESSION.value
    ]
)
SessionAttributes.__doc__ = SessionAttr.DOC.value


def digest_key(key: str) -> bytes:
    """Generates a bytes digest of the given key.

    Args:
        key (str): The key string to hash.

    Returns:
        bytes: The digest of the key in bytes.
    """
    return blake2b(
        key.encode(),
        digest_size=Utils.SIZE.value
    ).digest()


def allot(size: int = 6) -> str:
    """Generates a unique random string for key distribution.

    Args:
        size: The number of random bytes to use (must be divisible by 3).

    Returns:
        A URL-safe Base64-encoded string of the specified size.
    """
    if size < 6:
        raise ValueError()
    lot = SystemRandom().randbytes(size)
    return base64.urlsafe_b64encode(lot).decode()


def mk_hash(digest: bytes) -> str:
    """Generates a URL-safe Base64 hash of the given key digest."""
    return base64.urlsafe_b64encode(digest).decode()


def get_primary_key(key: str) -> str:
    """Generates a unique primary key for a given key."""
    key_digest = digest_key(key)
    keyed = mk_hash(key_digest)
    return keyed


def get_time() -> tuple[int, int]:
    """Returns the current time as a named tuple (timestamp, microseconds)."""
    time_store = datetime.now()
    store_ms = time_store.microsecond
    store_timestamp = int(time_store.timestamp())
    now = GetTime(store_timestamp, store_ms)
    return now


GetTime = namedtuple(
    TimeAttr.TYPE_NAME.value,
    [
        TimeAttr.TIMESTAMP.value,
        TimeAttr.MICROSECOND.value
    ]
)
GetTime.__doc__ = TimeAttr.DOC.value


def get_datastore(data: LiteStashData) -> LiteStashStore:
    """Creates a `LiteStashStore` object from `LiteStashData`.

    Args:
        data: A `LiteStashData` object.

    Returns:
        A `LiteStashStore` object ready for database storage.
    """
    primary_key = get_primary_key(data.key)
    now = get_time()
    stash_data = LiteStashStore(
        key_hash = primary_key,
        key = data.key,
        value = data.value,
        timestamp = now.timestamp,
        microsecond = now.microsecond
            )
    return stash_data


def get_keys(session: Session, table: Table) -> list[str]:
    """Retrieves all keys from the specified table.

    Args:
        session: The SQLAlchemy session to use.
        table: The SQLAlchemy Table object to query.

    Returns:
        list[str]: A list of all keys in the table.
    """
    with session() as keys_get:
        sql_statement = select(table.c[C.KEY.value])
        keys = keys_get.execute(sql_statement).scalars().all()
    return keys

def get_values(session: Session, table: Table) -> list[dict]:
    """Retrieves all values from the specified table.

    Args::
        session: The SQLAlchemy session to use.
        table: The SQLAlchemy Table object to query.

    Returns:
        list[dict]: A list of all JSON values in the table (deserialized).
    """
    with session() as values_get:
        sql_statement = select(table.c[C.VALUE.value])
        values = values_get.execute(sql_statement).scalars().all()
    return values
