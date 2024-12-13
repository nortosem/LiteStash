"""Engine Utilities

The engine_util module provides functions to assemble the LiteStash engine
module.

Functions:
- `set_pragma`: Configures SQLite PRAGMAs for the engine.
- `set_begin`: SqlAlchemy workaround for pysqlite driver
- `setup_engine`: Creates a SQLAlchemy engine for a given database.*

Classes:
* `EnginAttributes`: Namedtuple encapsulation of database name and a sqlalchemy
engine configured for use.
"""
from pathlib import Path
from sqlalchemy import event
from sqlalchemy import Engine
from sqlalchemy import create_engine
from pydantic import StrictStr
from collections import namedtuple
from litestash.logging import root_logger as logger
from litestash.core.config.schema_conf import Sql
from litestash.core.config.schema_conf import Pragma
from litestash.core.config.litestash_conf import EngineAttr
from litestash.core.config.litestash_conf import EngineConf
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
    logger.debug('Set PRAGMA on %s', db_connection)
    cursor = db_connection.cursor()
    cursor.execute(Pragma.journal_mode())
    logger.debug('journal_mode: %s', connect.last_connect_time)
    cursor.execute(Pragma.synchronous())
    logger.debug('synchronous: %s', connect.last_connect_time)
    cursor.execute(Pragma.valid_json())
    logger.debug('valid_json: %s', connect.last_connect_time)
    cursor.close()
    logger.debug('all pragmas set, close cursor %s', cursor)
    db_connection.isolation_level = None
    logger.debug(
        'db_connection isolation set to %s', db_connection.isolation_level
    )
    logger.debug('last_connect: %s', connect.last_connect_time)


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
        logger.error('Valid database name required')
        raise ValueError('Database name missing')
    if not name_match(db_name):
        logger.error('Invalid file name %s. ASCII only', db_name)
        raise ValueError(f'{EngineConf.db_name_ascii()}: {db_name}')
    if spaces_match(db_name):
        logger.error('No space characters permitted in file name: %s', db_name)
        raise ValueError(f'{EngineConf.db_name_space()}: {db_name}')
    if len(db_name) < EngineConf.min_name_length():
        logger.error('todo')
        raise ValueError(f'{EngineConf.db_name_length()}: {db_name}')
    if len(db_name) > Engine.max_name_length():
        logger.error('todo')
        raise ValueError(f'{EngineConf.db_name_length()}: {db_name}')

    if data_path is None:
        data_path = Path(
            f'{EngineConf.dirname()}/{db_name}'
        )
        logger.debug('data_path: %s', data_path)
    else:
        try:
            data_path =Path(
                f'{data_path}/{db_name}'
            )
            logger.debug('data_path: %s', data_path)
        except FileNotFoundError as path_error:
            logger.error('%s: %s', EngineConf.dir_not_found(), path_error)
            raise
        except PermissionError as path_error:
            logger.error('%s, %s', EngineConf.no_dir_access(), path_error)
            raise
        except Exception as path_error:
            logger.error('%s: %s', EngineConf.dir_path_error(), path_error)
            raise

    data_path.mkdir(parents=True, exist_ok=True)
    logger.debug('data_path mkdir if needed')

    database = f'{EngineConf.sqlite()}{data_path}/{db_name}.db'
    logger.debug('database url: %s', database)

    engine = create_engine(
        database,
        logging_name=f'{db_name}_engine',
        pool_logging_name=f'{db_name}_pool',
        echo=EngineConf.no_echo(),
        echo_pool=EngineConf.no_echo(),
        pool_size=EngineConf.pool_size(),
        max_overflow=EngineConf.max_overflow(),
    )
    logger.debug('db engine: %s', engine)

    event.listen(
        engine,
        Pragma.CONNECT.value,
        set_pragma
    )
    logger.debug('default pragma event listener added')
    event.listen(
        engine,
        Sql.BEGIN.value.lower(),
        set_begin
    )
    logger.debug('applied explicit BEGIN event listener for sql begin')
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
