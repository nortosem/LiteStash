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
from sqlalchemy import event
from sqlalchemy import select
from sqlalchemy import inspect
from sqlalchemy import Engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm.session import Session
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
from litestash.core.config.litestash_conf import TimeAttr
from litestash.core.config.litestash_conf import EngineConf
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.schema_conf import Pragma
from litestash.core.config.schema_conf import ColumnSetup as C
from litestash.core.util.schema_util import mk_tables

def set_pragma(db_connection, connect):
    """Set Engine Pragma

    Set the pragma for the engine attach event
    Args:
        db_connection (Engine): The engine to connect
        connection (str): The connection record
    """
    print(f'connect: {connect}')# use with logging etc
    cursor = db_connection.cursor()
    cursor.execute(Pragma.journal_mode())
    cursor.execute(Pragma.synchronous())
    cursor.execute(Pragma.valid_json())
    cursor.close()
    db_connection.isolation_level = None


def set_begin(db_connection):
    """Begin transaction

    Workaround for locking behavior per:
    https://docs.sqlalchemy.org/en/20/dialects/sqlite.html
    #dialect-sqlite-pysqlite-connect
    """
    db_connection.exec_driver_sql(Pragma.BEGIN.value)


def setup_engine(db_name: str) -> Engine:
    """Setup engine

    Args:
        engine_name (str): match with sqlite.db filename

    Return a tuple of (name, engine)
    {EngineConf.dirname()}/
    """
    engine = create_engine(
        f'{EngineConf.sqlite()}{EngineConf.dirname()}/{db_name}.db',
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


def setup_metadata(engine_attributes: EngineAttributes):
    """Setup Metadata & Tables

    Args:
        stash (LiteStashEngine):  Retrieve name & engine to setup from
        slot (str): datable named attribute slot
    """
    db_name, engine = engine_attributes
    metadata = MetaData()
    metadata = mk_tables(db_name, metadata)
    metadata.create_all(bind=engine, checkfirst=True)
    quality_metadata = MetaAttributes(db_name, metadata)
    return quality_metadata


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
    quality_session = SessionAttributes(db_name, session)
    return quality_session


SessionAttributes = namedtuple(
    SessionAttr.TYPE_NAME.value,
    [
        SessionAttr.DB_NAME.value,
        SessionAttr.SESSION.value
    ]
)
SessionAttributes.__doc__ = SessionAttr.DOC.value


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


def mk_hash(key: str) -> str:
    """Key Hash function

    Generate a primary database key for a name associated with some json data
    Args:
        key:
            Random value to distribute keys across storage
    Result:
        hashed_key:
            A string result to use as the unique key for json data
    """
    return base64.urlsafe_b64encode(key.encode()).decode()


def get_primary_key(key: str) -> str:
    """Valid Data Preparation

    Generate a primary key and return the pk and lot for the given kv pair
    Args:
        key (str):
    Result:
        pk (str):
    """
    key_digest = digest_key(key)
    keyed = mk_hash(key)
    digested = mk_hash(key_digest)
    return mk_hash(keyed+digested)


def get_time() -> tuple[int, int]:
    """Get time now

    Get the current datetime now as unix timestamp
    Result:
        GetTime: unix timestamp and microsecond time as int
    """
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
    """Get LiteStashStore

    Create a LiteStashStore object from the LiteStashData
    Args:
        data (LiteStashData): a valide key value pair
    Result:
        (LiteStashStore): data ready for use with storage
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
    """Get all keys

    The get_keys function gets all of the key names from a table
    Result:
        (list[str]): all plain text key's naming some data in the table
    """
    sql_statement = select(table.c.key[C.KEY.value])
    keys = session.execute(sql_statement).scalars().all()
    return keys

def get_values(session: Session, table: Table) -> list[dict]:
    """Get all values

    The get_values function get all of the values from a table
    Result:
        (list[]): all of the json data store in a taable
    """
    sql_statement = select(table.c[C.VALUE.value])
    values = session.execute(sql_statement).scalars().all()
    return values
