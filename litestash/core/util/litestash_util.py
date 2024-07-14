"""The LiteStash Core Utilities

Functions:
    setup_engine
    setup_metadata
    setup_sessions
    check_key
#TODO docs
"""
from litestash.core.config.litestash_conf import EngineAttr
from litestash.core.config.litestash_conf import MetaAttr
from litestash.core.config.litestash_conf import SessionAttr
from litestash.core.config.litestash_conf import EngineConf
from litestash.core.config.litestash_conf import DataScheme
from litestash.core.config.litestash_conf import Utils
from litestash.core.util.schema_util import mk_tables
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Engine
from sqlalchemy import MetaData
from collections import namedtuple
from hashlib import blake2b

def setup_engine(db_name: str) -> Engine:
    """Setup engine

    Args:
        engine_name (str): match with sqlite.db filename

    Return a tuple of (name, engine)
    {EngineConf.dirname()}/
    """
    return (db_name,
        create_engine(
            f'{EngineConf.sqlite()}{db_name}.db'
        )
    )

EngineAttributes = namedtuple(
    EngineAttr.TYPE_NAME.value,
    [
        EngineAttr.DB_NAME.value,
        EngineAttr.ENGINE.value
    ]
)
EngineAttributes.__doc__ = EngineAttr.DOC.value


def setup_metadata(engine_attributes: EngineAttributes):
    """Setup Metadata & Tables

    Args:
        stash (LiteStashEngine):  Retrieve name & engine to setup from
        slot (str): datable named attribute slot
    """
    db_name, engine = engine_attributes
    metadata = MetaData()
    metadata = mk_tables(db_name, metadata)
    metadata.create_all(bind=engine)
    return (db_name, metadata)


MetaAttributes = namedtuple(
    MetaAttr.TYPE_NAME.value,
    [
        MetaAttr.DB_NAME.value,
        MetaAttr.METADATA.value
    ]
)
MetaAttributes.__doc__ = MetaAttr.DOC.value


def setup_sessions(engine_attributes: EngineAttributes):
    """Make a sesssion

    Given a LiteStashEngine make a session factory for a database engine.

    Args:
        slot (str): database name slot
        stash (LiteStashEngine): An Engine with Metadata already setup
    """
    db_name, engine = engine_attributes
    if inspect(engine).get_table_names():
        session = sessionmaker(engine)
    else:
        raise ValueError(f'{SessionAttr.VALUE_ERROR.value}')
    return (db_name, session)


SessionAttributes = namedtuple(
    SessionAttr.TYPE_NAME.value,
    [
        SessionAttr.DB_NAME.value,
        SessionAttr.SESSION.value
    ]
)
SessionAttributes.__doc__ = SessionAttr.DOC.value


def check_key(key: str) -> bytes:
    """Validates and encodes an ASCII string key to bytes."""
    if key.isacii():
        if key.isalnum():
            return key.encode()
        else:
            raise ValueError(DataScheme.ALNUM_ERROR.value)
    else:
        raise ValueError(DataScheme.ASCII_ERROR.value)


def hash_key(key: bytes) -> bytes:
    """Get the hashed str bytes for a key"""
    return blake2b(key, digest_size=Utils.SIZE.value).hexdigest().encode()
