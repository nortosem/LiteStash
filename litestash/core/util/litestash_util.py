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
from datetime import datetime

from hashlib import blake2b

import orjson

from typing import List
from typing import Optional
from typing import overload
from typing import Union

from secrets import base64
from secrets import randbelow

from sqlalchemy import delete
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy import select
from sqlalchemy import Table
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from pydantic import StrictBool
from pydantic import StrictBytes
from pydantic import StrictInt
from pydantic import StrictStr
from pydantic import ValidationError

from litestash.models import LiteStashData
from litestash.models import LiteStashStore
from litestash.core.config.connection_conf import ConnectionType
from litestash.core.util.connection_util import Connection
from litestash.core.util.connection_util import DatabaseConnections
from litestash.core.util.connection_util import DataResults
from litestash.core.util.connection_util import GetConnection
from litestash.core.util.connection_util import GetDataConnections
from litestash.core.util.connection_util import GetTime
from litestash.core.util.connection_util import SetConnection
from litestash.core.util.connection_util import SetDataConnections
from litestash.core.config.litestash_conf import Key
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.schema_conf import ColumnFields as C
from litestash.core.util.misc_util import spaces_match
from litestash.core.util.schema_util import get_db_name
from litestash.core.util.schema_util import get_table_name
from litestash.core.schema import Metadata
from litestash.core.session import Session as Manager
from litestash.logging import root_logger as logger


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

    if not key.isascii():
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

    if not key.isascii():
        logger.error('Primary key contains non-ASCII characters')
        raise ValueError(f'Invalid characters in key: {key}')

    try:
        key_digest = digest_key(key)
        keyed = mk_hash(key_digest)
        return keyed
    except ValidationError as error:
        logger.error('%s', error)
        raise
    except ValueError as key_error:
        logger.error('%s', Key.log_error())
        raise TypeError(f'{Key.type_error()}') from key_error


def get_time(time: datetime = None) -> tuple[int, int]:
    """Returns the current time as a named tuple (timestamp, microseconds)."""
    if time is None:
        time_store = datetime.now()
        store_ms = time_store.microsecond
        store_timestamp = int(time_store.timestamp())
        return GetTime(store_timestamp, store_ms)
    else:
        timestamp = int(time.timestamp)
        ms = time.microsecond
        return GetTime(timestamp, ms)


def time_to_live(seconds: StrictInt):
    """Time to Live

    The expiration time for an storage item.

    Args:
        seconds (StrictInt): The number of seconds until expiration froma
            unix timestamp.

    Returns:
        ttl (GetTime):
            GetTime is a namedtuple of a timestamp and microseconds.
    Raises:

    """
    if seconds < 0:
        seconds = 0
    if seconds > 31449600:
        seconds = 31449600
    if seconds == 0:
        seconds = randbelow(31449600)
        if seconds == 0:
            seconds = randbelow(31449600)
    time = get_time()
    try:
        ttl = GetTime(time.timestamp+seconds, time.microsecond)
    except ValidationError as invalid:
        logger.error('Integer values only: %s', invalid)
        raise
    return ttl


def mk_datastore(data: LiteStashData) -> LiteStashStore:
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


@overload
def connect(data: LiteStashData) -> Connection:
    """The getter connect"""


@overload
def connect(data: LiteStashStore) -> Connection:
    """The setter connect"""


def connect(data: Union[LiteStashData | LiteStashStore],
              metadata: Metadata,
              db_session: Session) -> Connection:
    """connect


    Returns:
        Connection
    """
    key_hash = None
    connection_type = None
    if isinstance(data, LiteStashData):
        key_hash = get_primary_key(data.key)
        connection_type = ConnectionType.GET.value
    elif isinstance(data, LiteStashStore):
        key_hash = data.key_hash
        connection_type = ConnectionType.SET.value
    db_name = get_db_name(key_hash[0])
    table_name = get_table_name(key_hash[0])
    metadata = metadata.get(db_name).metadata
    session = db_session.get(db_name).session
    table = metadata.tables[table_name]

    connection = None
    if connection_type is ConnectionType.GET.value:
        connection = GetConnection(key_hash, table, session)
    elif connection_type is ConnectionType.SET.value:
        connection = SetConnection(data, table, session)

    return connection


@overload
def connections(items: List[LiteStashData]):
    """"""


@overload
def connections(items: List[LiteStashStore]):
    """"""


def connections(
    items: List[Union[LiteStashData, LiteStashStore]]
) -> DatabaseConnections:
    """connections

    Given the keys from setup determine the type of connections required for a
    multiple database entry set.

    Args:
        items (List[Union[LiteStashData, LiteStashStore]]):
            Given LiteStashData list build a GetDataConnections object, or
            given LiteStashStore list, build a SetDataConnections object.

    Returns:
        connections (GetDataConnections | SetDataConnections):
            A connections object with all requested connections sorted by each
            database the connections will operate upon.
    """
    database_connections = DatabaseConnections()
    if all(connections.is_data(item) for item in items):
        database_connections = GetDataConnections()
        for data in items:
            database_connections[get_db_name(data.key_hash[0])] = data
        return database_connections
    elif all(database_connections.is_store(item) for item in items):
        database_connections = SetDataConnections()
        for data in items:
            database_connections[get_db_name(data.key_hash[0])] = data
        return database_connections


def db_data(db_connections: DatabaseConnections):
    """Yields database and data for processing."""
    for db_name in db_connections.keys():
        if not db_connections[db_name] is None:
            yield(db_name, db_connections[db_name])


def get_session(db_name: StrictStr, manager: Manager):
    """Return a session for the named database."""
    return manager.get(db_name).session


def get_table(primary_key: StrictStr, db_name: StrictStr, metadata: Metadata):
    """Return the table for the given key and metadata."""
    table_name = get_table_name(primary_key[0])
    metadata = metadata.get(db_name).metadata
    return metadata.tables[table_name]


def get_query(primary_key: StrictStr, table: Table):
    """Return the sql query for getting a value by hash key."""
    return select(table).where(table.c.key_hash == primary_key)


def mget_data(mget_connections: GetDataConnections,
             metadata: Metadata,
             manager: Manager) -> DataResults:
    """multi-getter"""
    results = DataResults()
    def process_data(db_name, data, metadata, session):
        for entry in data:
            pk = get_primary_key(entry.key)
            table = get_table(pk, db_name, metadata)
            query = get_query(pk, table)
            try:
                result = session.execute(query).first()
                if result:
                    yield LiteStashData(key=result[1], value=result[2])

            except OperationalError as oe:
                logger.error('OperationalError: %s', oe)
                yield None, str(oe)
            except IntegrityError as ie:
                logger.error('IntegrityError: %s', ie)
                yield None, str(ie)
            except SQLAlchemyError as se:
                logger.error('SQlAlchmeyError: %s', se)
                yield None, str(se)
            except Exception as error:
                logger.error('Unknown error: %s', error)
                raise


    for db_name, data in db_data(mget_connections):
        session = get_session(db_name, manager)
        with session() as mget_session:
            for result in process_data(db_name, data, metadata, session):
                if isinstance(result, tuple):
                    _, error = result
                    logger.error('error on get: %s', error)
                else:
                    results[db_name] = result
                    logger.info('stored result: %s', result)
            mget_session.commit()
    return results


def set_query(data: LiteStashStore, table: Table):
    """Return a SQL insert statement."""
    statement = (insert(table)
        .values(
            key_hash=data.key_hash,
            key=data.key,
            value=data.value,
            timestamp=data.timestamp,
            microsecond=data.microsecond
        )
    )
    return statement.on_conflict_do_update(
        index_elements=[C.HASH.value],
        set_=statement.excluded,
    )


def mset_data(mset_connections: SetDataConnections,
             metadata: Metadata,
             manager: Manager) -> None:
    """mulit-setter"""
    def process_data(db_name, data, metadata, session):
        for entry in data:
            table = get_table(entry.key_hash, db_name, metadata)
            query = set_query(entry, table)
            try:
                session.execute(query)
                yield entry.key
            except OperationalError as oe:
                logger.error('OperationalError: %s', oe)
                yield None, str(oe)
            except IntegrityError as ie:
                logger.error('IntegrityError: %s', ie)
                yield None, str(ie)
            except SQLAlchemyError as se:
                logger.error('SQlAlchmeyError: %s', se)
                yield None, str(se)
            except Exception as error:
                logger.error('Unknown error: %s', error)
                raise

    for db_name, data in db_data(mset_connections):
        session = get_session(db_name, manager)
        with session() as set_session:
            for result in process_data(db_name, data, metadata, manager):
                if isinstance(result, tuple):
                    _, message = result
                    logger.error('insert failed: %s', message)
                else:
                    logger.info('inserted %s', result)
            set_session.commit()


def get_data(connection: Connection) -> Optional[LiteStashData]:
    """get_data

    Get the LiteStashData for a given key.

    Args:

    Returns:

    Raises:

    """
    try:
        key_hash, table, session = connection
        query = get_query(key_hash, table)
        with session() as get_data_session:
            result = get_data_session.execute(query).first()
            get_data_session.commit()
        if result:
            return LiteStashData(
                key=result[1],
                value=orjson.dumps(result[2])
            )
        else: return None

    except ValidationError as invalid:
        logger.error('Validation error: %s', invalid)
        raise
    except Exception as error:
        logger.error('Unknown excetion: %s', error)
        raise

def get_time_data(connection: Connection) -> GetTime:
    """get time


    """
    try:
        key_hash, table, session = connection
        query = select(table).where(
            table.c.key_hash == key_hash
        )
        with session() as session:
            result = session.execute(query).first()
            session.commit()
        if result:
            return GetTime(result[3], result[4])
    except ValidationError as error:
        logger.error('todo: %s', error)
        raise


def set_data(connection: Connection) -> None:
    """set_data


    """
    try:
        data, table, session = connection
        query = set_query(data, table)

        with session() as set_session:
            set_session.execute(query)
            set_session.commit()

    except ValidationError as invalid:
        logger.error('invalid: %s', invalid)
        raise


#def get_datastore(key: StrictStr):
#    """Get Datastore

#    Retrieve the LiteStashStore for a given key.

#    Args:
#        key (StrictStr): The string text name for a key.

#    Returns:
#        LiteStashStore: Return the data stored with this key in the LiteStash.

#    Raises:

#    """
#    pass


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

    with session() as keys_get:
        query = select(table.c[C.KEY.value])
        keys = keys_get.execute(query).scalars().all()
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

    with session() as values_get:
        query = select(table.c[C.VALUE.value])
        values = values_get.execute(query).scalars().all()
    return values


def does_exist(connection: Connection) -> StrictBool:
    """does_exists


    """
    query_data, table, session = connection
    query = (
        select(table).where(table.c.key_hash == query_data.key_hash)
    )
    with session() as exist_session:
        data = exist_session.execute(query).first()
        exist_session.commit()
    if data:
        return True
    else:
        return False


def delete_data(connection: Connection) -> None:
    """delete_data

    Helper function for the LiteStash delete function.
    """
    hash_key, table, session = connection
    with session() as delete_session:
        delete_session.execute(
            delete(table).where(table.c.key_hash == hash_key)
        )
        delete_session.commit()
