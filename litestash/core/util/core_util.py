"""Core Utilities

Core setup functions and classes to build a LiteStash database instance.

Functions:

- `setup_metadata`: Sets up database metadata and tables.
- `setup_sessions`: Creates a session factory for a database.

Classes:

- `MetaAttributes`: Namedtuple encapsulation of database name and a sqlalchemy
    metadata database object configured for use.
- `SessionAttributes`: Namedtuple encapsulation of database name and a
    sqlalchemy session object configured for use.
"""
from sqlalchemy import inspect
from sqlalchemy import MetaData
from collections import namedtuple
from sqlalchemy.orm.session import sessionmaker
from litestash.logging import root_logger as logger
from litestash.core.config.litestash_conf import MetaAttr
from litestash.core.config.litestash_conf import SessionAttr
from litestash.core.util.schema_util import mk_tables
from litestash.core.util.engine_util import EngineAttributes


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
