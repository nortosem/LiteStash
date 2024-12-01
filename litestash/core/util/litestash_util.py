"""LiteStash Utility Module

This module provides essential utility functions for the LiteStash key-value
store.

Functions:

- `set_pragma`: Apply configuration for sqlite engine
- `set_begin`: SqlAlchemy workaround for pysqlite driver
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
import re
import orjson
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
from litestash.logging import ENV
from litestash.logging import root_logger as logger
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
from litestash.core.config.root import Log
from litestash.core.config.litestash_conf import EngineAttr
from litestash.core.config.litestash_conf import MetaAttr
from litestash.core.config.litestash_conf import SessionAttr
from litestash.core.config.litestash_conf import TimeAttr
from litestash.core.config.litestash_conf import EngineConf
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.schema_conf import Pragma
from litestash.core.config.schema_conf import Sql
from litestash.core.config.schema_conf import ColumnFields as C
from litestash.core.util.schema_util import mk_tables

def set_pragma(db_connection, connect):
    """Sets SQLite PRAGMA settings on a new connection.
    This function is intended to be used as an event listener with SQLAlchemy
    engines to configure essential PRAGMA settings like journaling mode,
    synchronous mode, foreign key enforcement, and JSON handling.

    Args:
        db_connection: The raw DBAPI connection object
        (e.g., sqlite3.Connection).

        connect:  The SQLAlchemy internal connection record object
    """
    logger.debug(f'Set PRAGMA on {db_connection}')
    cursor = db_connection.cursor()
    cursor.execute(Pragma.journal_mode())
    logger.debug(f'journal_mode: {connect.last_connect_time}')
    cursor.execute(Pragma.synchronous())
    logger.debug(f'synchronous: {connect.last_connect_time}')
    cursor.execute(Pragma.valid_json())
    logger.debug(f'valid_json: {connect.last_connect_time}')
    cursor.close()
    logger.debug(f'all pragmas set, close cursor {cursor}')
    db_connection.isolation_level = None
    logger.debug(
        f'db_connection isolation set to {db_connection.isolation_level}'
    )
    logger.debug(f'last_connect: {connect.last_connect_time}')


def set_begin(db_connection):
    """Explicitly begins a transaction with a BEGIN statement.

    This is a workaround for the default behavior of the pysqlite driver,
    which can interfere with SQLAlchemy's transaction management. By emitting
    our own BEGIN, we ensure correct transactional behavior.

    Args:
        dbapi_connection: The raw DBAPI connection object.

    Optionally TODO: consider deferred, exclusive, or immediate BEGINs
    """
    db_connection.exec_driver_sql(Sql.BEGIN.value)


def setup_engine(db_name: str, data_path: str = None) -> Engine:
    """Sets up a SQLAlchemy engine for the given database.

    Args:
        db_name: The name of the database file.

    Returns:
        EngineAttributes: A namedtuple containing the database name and the
        engine.
    """
    space = re.compile(r'\s+')
    file_name = re.compile(f'\w+', flags=re.A)
    if db_name is None:
        logger.error(f'Valid database name required')
        raise ValueError(f'Database name missing')
    if not file_name.match(db_name):
        logger.error(f'')
        raise ValueError(f'{EngineConf.db_name_ascii()}: {db_name}')
    if space.match(db_name):
        logger.error(f'')
        raise ValueError(f'{EngineConf.db_name_space()}: {db_name}')
    if len(db_name) < EngineConf.min_name_length():
        logger.error(f'')
        raise ValueError(f'{EngineConf.db_name_length()}: {db_name}')
    if len(db_name) > Engine.max_name_length():
        logger.error(f'')
        raise ValueError(f'{EngineConf.db_name_length()}: {db_name}')

    if data_path is None
        data_path = Path(
            f'{EngineConf.dirname()}/{db_name}'
        )
        logger.debug(f'data_path: {data_path}')
    else:
        try:
            data_path =Path(
                f'{data_path}/{db_name}'
            )
            logger.debug(f'data_path: {data_path}')
        except FileNotFoundError as path_error:
            logger.error(f'{EngineConf.dir_not_found()}: {path_error}')
            raise
        except PermissionError as path_error:
            logger.error(f'{EngineConf.no_dir_access()}: {path_error}')
            raise
        except Exception as path_error:
            logger.error(f'{EngineConf.dir_path_error()}: {path_error}')

    data_path.mkdir(parents=True, exist_ok=True)
    logger.debug(f'data_path mkdir if needed')

    database = f'{EngineConf.sqlite()}{data_path}/{db_name}.db'
    logger.debug(f'database url: {database}')

    engine = create_engine(
        database,
        logging_name=f'{db_name}_engine',
        pool_logging_name=f'{db_name}_pool',
        echo=EngineConf.no_echo(),
        echo_pool=EngineConf.no_echo(),
        pool_size=EngineConf.pool_size(),
        max_overflow=EngineConf.max_overflow(),
    )
    logger.debug(f'db engine: {engine}')

    event.listen(
        engine,
        Pragma.CONNECT.value,
        set_pragma
    )
    logger.debug(f'default pragma event listener added')
    event.listen(
        engine,
        Sql.BEGIN.value.lower(),
        set_begin
    )
    logger.debug(f'applied explicit BEGIN event listener for sql begin')
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
    logger.debug(f'{engine_stash.db_name} init {metadata}')
    metadata = mk_tables(engine_stash.db_name, metadata)
    logger.debug(f'added tables to {metadata}')
    metadata.create_all(bind=engine_stash.engine, checkfirst=True)
    logger.debug(
        f'create and bind metadata to {engine_stash.engine}'
    )
    logger.debug(f'tables: {metadata.sorted_tables}')
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
        logger.debug(f'sessionmaker called for {engine_stash.engine}')
        session = sessionmaker(engine_stash.engine)
        logger.debug(f'sessionmaker created {session}')
    else:
        raise ValueError(f'{SessionAttr.VALUE_ERROR.value}')
    logger.debug(
        f'Call SessionAttributes with {engine_stash.db_name}, {session}'
    )
    quality_session = SessionAttributes(engine_stash.db_name, session)
    logger.debug(f'return quality_session {quality_session}')
    return quality_session


SessionAttributes = namedtuple(
    SessionAttr.TYPE_NAME.value,
    [
        SessionAttr.DB_NAME.value,
        SessionAttr.SESSION.value
    ]
)
SessionAttributes.__doc__ = SessionAttr.DOC.value


def allot(size: int = 6) -> str:
    """Generates a unique random string for key distribution.

    Args:
        size: The number of random bytes to use (must be divisible by 3).

    Returns:
        A URL-safe Base64-encoded string of the specified size.
    """
    if size < 6:
        raise ValueError('min size')

    if size % 3 != 0:
        raise ValueError('must be divisible by three')

    lot = SystemRandom().randbytes(size)
    return base64.urlsafe_b64encode(lot).decode()


def digest_key(key: str) -> bytes:
    """Generates a bytes digest of the given key.

    Args:
        key (str): The key string to hash.

    Returns:
        bytes: The digest of the key in bytes.
    """
    digest = blake2b(key.encode(), digest_size=Utils.SIZE.value).digest()
    return digest


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

#        time (GetTime): The GetTime namedtuple record of key creation.
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
    logger.debug(f'get_datastore primary_key: {primary_key}')
    now = get_time()
    logger.debug(f'get_datastore time@now: {now}')
    stash_data = LiteStashStore(
        key_hash = primary_key,
        key = data.key,
        value = data.value,
        timestamp = now.timestamp,
        microsecond = now.microsecond
            )
    logger.debug(f'stash_data key_hash: {stash_data.key_hash}')
    logger.debug(f'stash_data key: {stash_data.key}')
    logger.debug(f'stash_data value: {stash_data.value}')
    logger.debug(f'stash_data timestamp: {stash_data.timestamp}')
    logger.debug(f'stash_data microsecond: {stash_data.microsecond}')
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
