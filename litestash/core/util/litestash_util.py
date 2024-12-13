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
#import orjson
#from pathlib import Path
from hashlib import blake2b
#from typing import Callable
from datetime import datetime
from secrets import base64
from secrets import SystemRandom
from collections import namedtuple
from pydantic import StrictStr
from pydantic import StrictBytes
from sqlalchemy import select
from sqlalchemy import inspect
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.session import sessionmaker
#from litestash.logging import ENV
from litestash.logging import root_logger as logger
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
#from litestash.core.schema import Metadata as StashMetadata
#from litestash.core.session import Session as Stashsession
#from litestash.core.config.root import Log
from litestash.core.config.litestash_conf import Key
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.litestash_conf import MetaAttr
from litestash.core.config.litestash_conf import SessionAttr
from litestash.core.util.engine_util import EngineAttributes
from litestash.core.config.litestash_conf import TimeAttr
from litestash.core.config.schema_conf import ColumnFields as C
from litestash.core.util.schema_util import mk_tables
from litestash.core.util.misc_util import name_match
from litestash.core.util.misc_util import spaces_match


def setup_metadata(engine_stash: EngineAttributes):
    """Sets up and returns SQLAlchemy metadata for the given database engine.

    Args:
        engine_stash: A namedtuple containing the database name
        (`db_name`) and SQLAlchemy `Engine` object.

    Returns:
        MetaAttributes: A namedtuple containing the database name and the
        initialized `MetaData` object.
    """
    if engine_stash is None:
        logger.error('Database engine attributes are missing')
        raise ValueError('Engine attributes cannot be None')

    if not isinstance(engine_stash, EngineAttributes):
        logger.error('%s: invalid EngineAttributes', type(engine_stash))
        raise TypeError(f'Invalid engine attributes: {engine_stash}')

    metadata = MetaData()
    logger.debug('%s init %s', engine_stash.db_name, metadata)
    metadata = mk_tables(engine_stash.db_name, metadata)
    logger.debug('added tables to %s', metadata)
    metadata.create_all(bind=engine_stash.engine, checkfirst=True)
    logger.debug(
        'create and bind metadata to %s', engine_stash.engine
    )
    logger.debug('tables: %s', metadata.sorted_tables)
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
    if engine_stash is None:
        logger.error('Session engine attributes missing')
        raise ValueError('EngineAttributes cannot be None')

    if not isinstance(engine_stash, EngineAttributes):
        logger.error('%s: invalid type', type(engine_stash))
        raise TypeError(f'EngineAttributes not found: {engine_stash}')

    if inspect(engine_stash.engine).get_table_names():
        logger.debug('sessionmaker called for %s', engine_stash.engine)
        session = sessionmaker(engine_stash.engine)
        logger.debug('sessionmaker created %s', session)
    else:
        raise ValueError(f'{SessionAttr.VALUE_ERROR.value}')
    logger.debug(
        'Call SessionAttributes with %s, %s', engine_stash.db_name, session
    )
    quality_session = SessionAttributes(engine_stash.db_name, session)
    logger.debug('return quality_session %s', quality_session)
    return quality_session


SessionAttributes = namedtuple(
    SessionAttr.TYPE_NAME.value,
    [
        SessionAttr.DB_NAME.value,
        SessionAttr.SESSION.value
    ]
)
SessionAttributes.__doc__ = SessionAttr.DOC.value


def allot(size: int = 6) -> StrictStr:
    """Generates a unique random string for key distribution.

    Args:
        size: The number of random bytes to use (must be divisible by 3).

    Returns:
        A URL-safe Base64-encoded string of the specified size.
    """
    if size is None:
        logger.error('No size provided for the random bytes')
        raise ValueError('A value of six or more is required')

    if not isinstance(size, int):
        logger.error('Integer size not provided: %s', size)
        raise TypeError(f'Invalid size type: {type(size)}')

    if size < 6:
        raise ValueError('min size')

    if size % 3 != 0:
        raise ValueError('must be divisible by three')

    lot = SystemRandom().randbytes(size)
    return base64.urlsafe_b64encode(lot).decode()


def digest_key(key: StrictStr) -> bytes:
    """Generates a bytes digest of the given key.

    Args:
        key (str): The key string to hash.

    Returns:
        bytes: The digest of the key in bytes.
    """
    if key is None:
        logger.error('No string provided for the key')
        raise ValueError('Key cannot be empty')

    if spaces_match(key):
        logger.error('Spaces found in digest key string argument')
        raise ValueError(f'Invalid key provided: %s {key}')

    if not name_match(key):
        logger.error('Valid key requires ASCII only.')
        raise ValueError('todo')

    try:
        digest = blake2b(
            key.encode(),
            digest_size=Utils.SIZE.value
        ).digest()
        return digest
    except ValueError as key_error:
        logger.error('todo')
        raise TypeError from key_error


def mk_hash(digest: StrictBytes) -> StrictStr:
    """Generates a URL-safe Base64 hash of the given key digest."""
    if digest is None:
        logger.error('Digest required to make a hash')
        raise ValueError('No digest provided')

    if not isinstance(digest, bytes):
        logger.error('Digest type is bytes, not %s', type(digest))
        raise TypeError(f'Invalid type of digest: {type(digest)}')

    try:
        return base64.urlsafe_b64encode(digest).decode()
    except ValueError as digest_error:
        logger.error('')
        raise TypeError from digest_error


def get_primary_key(key: StrictStr) -> StrictStr:
    """Generates a unique primary key for a given key."""
    if key is None:
        logger.error('Primary key cannot be empty')
        raise ValueError('No primary key string provided')

    if spaces_match(key):
        logger.error('Primary key contains spaces: %s', key)
        raise ValueError(f'Invalid characters found in key: {key}')

    if not name_match(key):
        logger.error('Primary key contains non-ASCII characters')
        raise ValueError(f'Invalid characters in key: {key}')

    try:
        key_digest = digest_key(key)
        keyed = mk_hash(key_digest)
        return keyed
    except ValueError as key_error:
        logger.error('%s', Key.log_error())
        raise TypeError(f'{Key.type_error()}') from key_error


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
    if data is None:
        logger.error('No LiteStash Data found')
        raise ValueError('todo')

    primary_key = get_primary_key(data.key)
    logger.debug('get_datastore primary_key: %s', primary_key)
    now = get_time()
    logger.debug('get_datastore time@now: %s', now)
    stash_data = LiteStashStore(
        key_hash = primary_key,
        key = data.key,
        value = data.value,
        timestamp = now.timestamp,
        microsecond = now.microsecond
            )
    logger.debug('stash_data key_hash: %s', stash_data.key_hash)
    logger.debug('stash_data key: %s', stash_data.key)
    logger.debug('stash_data value: %s', stash_data.value)
    logger.debug('stash_data timestamp: %s', stash_data.timestamp)
    logger.debug('stash_data microsecond: %s', stash_data.microsecond)
    return stash_data


def get_keys(session: Session, table: Table) -> list[StrictStr]:
    """Retrieves all keys from the specified table.

    Args:
        session: The SQLAlchemy session to use.
        table: The SQLAlchemy Table object to query.

    Returns:
        list[str]: A list of all keys in the table.
    """
    if session is None:
        logger.error('todo')
        raise ValueError('todo')

    if table is None:
        logger.error('todo')
        raise ValueError('todo')

    if not isinstance(session, Session):
        logger.error('todo')
        raise TypeError('todo')

    if not isinstance(table, Table):
        logger.error('todo')
        raise TypeError('todo')

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
    if session is None:
        logger.error('todo')
        raise ValueError('todo')

    if table is None:
        logger.error('todo')
        raise ValueError('todo')

    if not isinstance(session, Session):
        logger.error('todo')
        raise TypeError('todo')

    if not isinstance(table, Table):
        logger.error('todo')
        raise TypeError('todo')

    with session() as values_get:
        sql_statement = select(table.c[C.VALUE.value])
        values = values_get.execute(sql_statement).scalars().all()
    return values
