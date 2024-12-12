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
import orjson
from queue import Queue
from pathlib import Path
from hashlib import blake2b
from typing import Callable
from threading import Lock
from threading import Thread
from hashlib import blake2b
from datetime import datetime
from secrets import base64
from secrets import SystemRandom
from collections import namedtuple
from pydantic import StrictStr
from pydantic import StrictBytes
from sqlalchemy import event
from sqlalchemy import select
from sqlalchemy import inspect
from sqlalchemy import Engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.session import sessionmaker
from concurrent.futures import Future
from litestash.logging import ENV
from litestash.logging import root_logger as logger
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
from litestash.core.schema import Metadata
from litestash.core.session import Session
from litestash.core.config.root import Log
from litestash.core.config.litestash_conf import Key
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.litestash_conf import TaskAttr
from litestash.core.config.litestash_conf import TaskSlots
from litestash.core.config.litestash_conf import EngineAttr
from litestash.core.config.litestash_conf import MetaAttr
from litestash.core.config.litestash_conf import SessionAttr
from litestash.core.config.litestash_conf import TimeAttr
from litestash.core.config.litestash_conf import EngineConf
from litestash.core.config.schema_conf import Pragma
from litestash.core.config.schema_conf import Sql
from litestash.core.config.schema_conf import ColumnFields as C
from litestash.core.util.schema_util import mk_tables
from litestash.core.util.misc_util import name_match
from litestash.core.util.misc_util import spaces_match


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


def setup_engine(db_name: StrictStr, data_path: StrictStr = None) -> Engine:
    """Sets up a SQLAlchemy engine for the given database.

    Args:
        db_name: The name of the database file.

    Returns:
        EngineAttributes: A namedtuple containing the database name and the
        engine.
    """
    if db_name is None:
        logger.error(f'Valid database name required')
        raise ValueError(f'Database name missing')
    if not name_match(db_name):
        logger.error(f'Invalid file name {db_name}. ASCII only')
        raise ValueError(f'{EngineConf.db_name_ascii()}: {db_name}')
    if spaces_match(db_name):
        logger.error(f'No space characters permitted in file name: {db_name}')
        raise ValueError(f'{EngineConf.db_name_space()}: {db_name}')
    if len(db_name) < EngineConf.min_name_length():
        logger.error(f'')
        raise ValueError(f'{EngineConf.db_name_length()}: {db_name}')
    if len(db_name) > Engine.max_name_length():
        logger.error(f'')
        raise ValueError(f'{EngineConf.db_name_length()}: {db_name}')

    if data_path is None:
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
            raise

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
    if engine_stash is None:
        logger.error('Database engine attributes are missing')
        raise(ValueError(f'Engine attributes cannot be None'))

    if not isinstance(engine_stash, EngineAttributes):
        logger.error(f'{type(engine_stash)}: invalid EngineAttributes')
        raise(TypeError(f'Invalid engine attributes: {engine_stash}'))

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
    if engine_stash is None:
        logger.error('Session engine attributes missing')
        raise(ValueError(f'EngineAttributes cannot be None'))

    if not isinstance(engine_stash, EngineAttributes):
        logger.error(f'{type(engine_stash)}: invalid type')
        raise(TypeError(f'EngineAttributes not found: {engine_stash}'))

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


def create_task(session: Session, queue, Queue): -> Task
    """Create a Task

    Function for creating a task to manage a specific database.

    Args:
        session (Session):
        queue (Queue):
    Returns:
        task (Task):
    Raises:

    """
    class Task:
        """Task

        This class manages the creation and access to task runners for each
        database thread.

        Attributes:

            __slots__ (tuple): A tuple of attribute names for memory
                optimization.

        Methods:
            __run:
            send:
            stop:
        """
        __slots__ = TaskSlots.get()

        def __init__(self, session: Session, queue: Queue):
            """Task Constructor

            Initialize the thread Task and link it to a database.
            """
            self.db_name = session.db_name
            self.session = session.session
            self.queue = queue
            self.thread = Thread(target=self.__run)
            self.thread.daemon = True
            self.thread.start()
            self.lock = Lock()


        def __run(self, func, data, future: Future):
            """__Run

            The Task thread's internal work function processor
            """
            while True:
                work is None:
                    break
                try:
                    with self.lock:
                        try:
                            func, data, future = work
                            result = func(data)
                            future.set_result(result)
                        except Exception as error:
                            future.set_exception(error)
                except Exception as error:
                    logger.error(f'Task error: {error}')
                finally:
                    self.queue.task_done()


        def send(self, func: Callable, data: LiteStashData, future=None):
            """Send

            Send a job for the task to run in the queue for its database.

            Args:
                func (Callable): The API function to call
                data (LiteStashData): The given key and, or, value.
                future (Future): The Future object for this task.
            """
            self.queue.put((func, data, future))


        def stop(self):
            """Stop

            Top the thread for this database.
            """
            self.queue.put(None)
            self.queue.join()


    return Task(session, queue)


def setup_tasks(session: Session, queue: Queue): -> TaskAttributes
    """Creates and returns Task and returns it for a specific database.

    Args


    Returns:
        TaskAttributes:

    Raises:

    """


TaskAttributes = namedtuple(
    TaskAttr.TYPE_NAME.value,
    [
        TaskAttr.DB_NAME.value,
        TaskAttr.TASK.value
    ]
)
TaskAttributes.__doc__ = TaskAttr.DOC.value

def allot(size: int = 6) -> StrictStr:
    """Generates a unique random string for key distribution.

    Args:
        size: The number of random bytes to use (must be divisible by 3).

    Returns:
        A URL-safe Base64-encoded string of the specified size.
    """
    if size is None:
        logger.error('No size provided for the random bytes')
        raise(ValueError('A value of six or more is required'))

    if not isinstance(size, int):
        logger.error(f'Integer size not provided: {size}')
        raise(TypeError(f'Invalid size type: {type(size)}'))

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
        raise ValueError(f'Invalid key provided: {key}')

    if not name_match(key):
        logger.error('Valid key requires ASCII only.')
        raise ValueError(f'')

    try:
        digest = blake2b(
            key.encode(),
            digest_size=Utils.SIZE.value
        ).digest()
        return digest
    except ValidationError as key_error:
        logger.error()
        raise TypeError from key_error


def mk_hash(digest: StrictBytes) -> StrictStr:
    """Generates a URL-safe Base64 hash of the given key digest."""
    if digest is None:
        logger.error('Digest required to make a hash')
        raise ValueError(f'No digest provided')

    if not isinstance(digest, bytes):
        logger.error(f'Digest type is bytes, not {type(digest)}')
        raise TypeError(f'Invalid type of digest: {type(digest)}')

    try:
        return base64.urlsafe_b64encode(digest).decode()
    except ValidationError as digest_error:
        logger.error()
        raise TypeError from digest_error


def get_primary_key(key: StrictStr) -> StrictStr:
    """Generates a unique primary key for a given key."""
    if key is None:
        logger.error('Primary key cannot be empty')
        raise ValueError('No primary key string provided')

    if spaces_match(key):
        logger.error(f'Primary key contains spaces: {key}')
        raise ValueError(f'Invalid characters found in key: {key}')

    if not name_match(key):
        logger.error('Primary key contains non-ASCII characters')
        raise ValueError(f'Invalid characters in key: {key}')

    try:
        key_digest = digest_key(key)
        keyed = mk_hash(key_digest)
        return keyed
    except ValidationError as key_error:
        logger.error(Key.log_error())
        raise TypeError(Key.type_error()) from value_error


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
        raise ValueError(f'')

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


def get_keys(session: Session, table: Table) -> list[StrictStr]:
    """Retrieves all keys from the specified table.

    Args:
        session: The SQLAlchemy session to use.
        table: The SQLAlchemy Table object to query.

    Returns:
        list[str]: A list of all keys in the table.
    """
    if session is None:
        logger.error()
        raise ValueError()

    if table is None:
        logger.error()
        raise ValueError()

    if not isinstance(session, Session):
        logger.error()
        raise(TypeError())

    if not isinstance(table, Table):
        logger.error()
        raise(TypeError())

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
        logger.error()
        raise ValueError()

    if table is None:
        logger.error()
        raise ValueError()

    if not isinstance(session, Session):
        logger.error()
        raise TypeError()

    if not isinstance(table, Table):
        logger.error()
        raise TypeError()

    with session() as values_get:
        sql_statement = select(table.c[C.VALUE.value])
        values = values_get.execute(sql_statement).scalars().all()
    return values
