"""The Utilities


"""
from collections import namedtuple
import orjson
from os import getcwd
from hashlib import blake2b
from pathlib import Path
from litestash.config import Utils
from litestash.config import TableName
from litestash.config import Digitables
from litestash.config import LowerTables
from litestash.config import UpperTables
from litestash.config import SetupDB
from litestash.config import ColumnSetup
from litestash.config import SessionStash
from litestash.models import StashColumns
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import inspect
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Metadata
from sqlalchemy import Engine
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import JSON
from typing import Generator

def setup_engine(engine_name: str) -> Engine:
    """Setup engine

    Args:
        engine_name (str): match with sqlite.db filename

    Return a tuple of (name, engine)
    """
    return (name,
            create_engine(
                f'{SetupDB.sqlite()}{SetupDB.dirname()}{name}.db',
                echo=SetupDB.echo.value
                )
            )

StashEngine = namedtuple(
    EngineStash.TYPE_NAME.value,
    [EngineStash.DB_NAME.value,
    EngineStash.ENGINE.value]
)
StashEngine.__doc__ = EngineStash.DOC.value


def setup_metadata(stash: LiteStashEngine, slot: str):
    """Setup Metadata & Tables

    Args:
        stash (LiteStashEngine):  Retrieve name & engine to setup from
        slot (str): datable named attribute slot
    """
    name, engine = getattr(stash, slot)
    metadata = Metadata()
    metadata = mk_tables(metadata)
    metadata.create_all(bind=engine, checkfirst=True)
    return (name, metadata)


StashMeta = namedtuple(
    MetaStash.TYPE_NAME.value,
    [MetaStash.DB_NAME.value,
    MetaStash.METADATA.value]
)
StashMeta.__doc__ = MetaStash.DOC.value


def setup_sessions(stash: LiteStashEngine, slot: str):
    """Make a sesssion

    Given a LiteStashEngine make a session factory for a database engine.

    Args:
        slot (str): database name slot
        stash (LiteStashEngine): An Engine with Metadata already setup
    """
    name, engine = getattr(stash, slot)
    if inspect(engine).get_table_name():
        session = sessionmaker(engine)
    else:
        raise ValueError(f'{SessionStash.VALUE_ERROR.value}')
    return (name, session)


StashSession = namedtuple(
    Sessionstash.TYPE_NAME.value,
    [SessionStash.DB_NAME.value,
    SessionStash.SESSION.value]
)
StashSession.__doc__ = SessionStash.DOC.value

def check_key(key: str) -> bytes:
    """Validates and encodes an ASCII string key to bytes."""
    if key.isacii():
        if key.isalnum():
            return key.encode()
        else:
            raise ValueError(DataScheme.ALNUM_ERROR.value)
    else:
        raise ValueError(DataScheme.ASCII_ERROR.value)


def hash_key(key: str) -> str:
    """Get the hashed str bytes for a key"""
    return blake2b(key, digest_size=Utils.SIZE.value).hexdigest().encode()

def get_hash_table(key: bytes): -> ?:
    """Given a hashed key return the table and database for the hash.

    Args:
        key (bytes): user provided key for the key-value pair
    """

    table_name = ''
    db_name = ''
    #TODO implement for the app class LiteStash


def mk_hash_column() -> Column:
    """Return a Column for the hash"""
    return StashColumns.column(
        ColumnSetup.HASH.value,
        BLOB,
        index=True,
        primary_key=True,
        nullable=False
    )


def mk_key_column() -> Column:
    """Return a Column for the key being stored."""
    return StashColumns.column(
        ColumnSetup.KEY.value,
        BLOB,
        unique=True,
        index=True,
        nullable=False
    )


def mk_value_column() -> Column:
    """Return a Column for the value being stored."""
    return StashColumns.column(
        ColumnSetup.VALUE.value,
        JSON,
        nullable-False
    )


def mk_time_column() -> Column:
    """Return a Column for the date the data was added."""
    return StashColumns.get_column(
        ColumnSetup.TIME.value,
        Integer,
        )


def mk_columns() -> Generator[Column, None, None]:
    """Make Columns

    Return a generator for all columns used in each table.
    """
    for column in (
        mk_hash_column(),
        mk_key_column(),
        mk_val_column(),
        mk_time_column()
    ):
        yield column


def mk_table_names() -> Generator[str, None, None]:
    """Make all valid Table names

    Generate names for all tables in cache
    Return a generator.
    """
    for chars in (Digitables,LowerTables,UpperTables):
        for suffix in chars:
            yield f'{TableName.ROOT.value}{suffix.value}'


def mk_tables(metadata: Metadata) -> Metadata:
    """Make Tables

    Create all tables using preset columns and names.
    """
    for table_name in mk_table_names():
        yield Table(
            table_name,
            metadata,
            *(column for column in mk_columns())
        )
    return metadata
