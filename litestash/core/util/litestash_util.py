"""LiteStash Utility Module

This module provides essential utility functions for the LiteStash key-value
store.

Functions:


- `digest_key`: Generates a hexadecimal digest of a key.
- `mk_hash`: Generates a hash for a key.
- `get_primary_key`: Generates a primary database key for a key-value pair.
- `get_time`: Gets the current time as a Unix timestamp and microseconds.
- `get_datastore`: Creates a LiteStashStore object from LiteStashData.
- `get_keys`: Retrieves all keys from a table.
- `get_values`: Retrieves all values from a table.

"""
from hashlib import blake2b
from datetime import datetime
from secrets import base64
from collections import namedtuple
from pydantic import StrictStr
from pydantic import StrictBytes
from sqlalchemy import select
from sqlalchemy import Table
from sqlalchemy import Session
#from litestash.logging import ENV
from litestash.logging import root_logger as logger
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
#from litestash.core.config.root import Log
from litestash.core.config.litestash_conf import Key
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.litestash_conf import TimeAttr
from litestash.core.config.schema_conf import ColumnFields as C
from litestash.core.util.misc_util import name_match
from litestash.core.util.misc_util import spaces_match


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
