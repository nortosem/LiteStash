"""The LiteStash Core Utilities

Functions:
    setup_engine
    setup_metadata
    setup_sessions
    check_key
#TODO docs
"""
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Engine
from sqlalchemy import MetaData
from collections import namedtuple
from datetime import datetime
from hashlib import blake2b
from secrets import base64
from secrets import SystemRandom
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
from litestash.core.config.litestash_conf import EngineAttr
from litestash.core.config.litestash_conf import MetaAttr
from litestash.core.config.litestash_conf import SessionAttr
from litestash.core.config.litestash_conf import EngineConf
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.schema_conf import Pragma
from litestash.core.util.schema_util import mk_tables

def setup_engine(db_name: str) -> Engine:
    """Setup engine

    Args:
        engine_name (str): match with sqlite.db filename

    Return a tuple of (name, engine)
    {EngineConf.dirname()}/
    """
    return (db_name,
        create_engine(
            f'{EngineConf.sqlite()}{EngineConf.DIR_NAME.value}/{db_name}.db'
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

def set_pragma(db_connection, record):
    """Set Engine Pragma

    Set the pragma for the engine attach event
    Args:
        db_connection (Engine): The engine to connect
        connection (str): The connection record
    """
    if str(f'{EngineConf.SQLITE.value}'
           f'{EngineConf.DIR_NAME.value}'
           ) in record.engine.url:
        cursor = db_connection.cursor()
        cursor.execute(Pragma.journal_mode())
        cursor.execute(Pragma.synchronous())
        cursor.close()


def digest_key(key: str) -> str:
    """Key Digest Generator

    Create a unique hexidecimal digest name
    Arg:
        key (str): The text name to make a digest from
    Result:
        digest (str): A hexidecimal digest string
    """
    return blake2b(
        key.encode(),
        digest_size=Utils.SIZE.value
    ).hexdigest()


def allot(size: int = 6) -> str:
    """Allot Function

    Generate unique random set of bytes for efficient hash key distribution
    Return a urlsafe base64 str from the random bytes
    All sizes must be divisible by 3
    The default size of six bytes returns an eight character string
    Args:
        size (int): number of bytes alloted for the lot
    Result:
        lot (str): An eight character string
    """
    if size < 6:
        raise ValueError()
    lot = SystemRandom().randbytes(size)
    return base64.urlsafe_b64encode(lot).decode()


def hash_key(key_digest: str, lot: str) -> str:
    """Key Hash function

    Generate a primary database key for a name associated with some json data
    Args:
        key_digest:
            The unique digest of the string name for the json value
        lot:
            Random value to distribute keys across storage
    Result:
        hashed_key:
            A string result to use as the unique key for json data
    """
    base_key = lot + base64.urlsafe_b64encode(key_digest.encode()).decode()
    return base64.urlsafe_b64encode(base_key.encode()).decode()


def get_primary_key(key: str, lot: str):
    """Valid Data Preparation

    Generate a primary key and return the pk and lot for the given kv pair
    Args:
        key (str):
        value (str):
        lot (str):
    Result:
        pk (str):
    """
    key_digest = digest_key(key)
    return hash_key(key_digest, lot)


def get_time():
    """Get time now

    Get the current datetime now as unix timestamp
    Result:
        (tuple[int,int]): unix timestamp and microsecond time as int
    """
    time_store = datetime.now()
    store_ms_time = time_store.microsecond
    store_timestamp = int(time_store.timestamp())
    return (store_timestamp, store_ms_time)


def get_datastore(data: LiteStashData) -> LiteStashStore:
    """Get LiteStashStore

    Create a LiteStashStore object from the LiteStashData
    Args:
        data (LiteStashData): a valide key value pair
    Result:
        (LiteStashStore): data ready for use with storage
    """
    primary_key = get_primary_key(data.key, allot())
    store_timestamp, store_ms_time = get_time()
    stash_data = LiteStashStore(
        key_hash = primary_key,
        key = data.key,
        value = data.value,
        date_time = store_timestamp,
        ms_time = store_ms_time
            )
    return stash_data

