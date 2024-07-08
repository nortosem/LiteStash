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
from litestash.models import StashColumns
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Metadata
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import JSON
from typing import Generator

def setup_engine(engine_name: str) -> Engine:
    """Setup up engine

    Args:
        engine_name (str): match with sqlite.db filename

    Return a tuple of (name, engine)
    """
    return create_engine(
        f'{SetupDB.sqlite()}{SetupDB.dirname()}{name}.db',
        echo=SetupDB.echo.value
    )#TODO confirm this conf and setup process


def hash_key(key: str) -> str:
    """Get the hashed str for given key"""
    return blake2b(key.encode(), digest_size=Utils.SIZE.value).hexdigest()

def get_hash_table(key: str): -> ?:
    """Given a hashed key return the table and database for the hash.

    Args:
        key (str): user provided key for the key-value pair
    """

    table_name = ''
    db_name = ''
    #TODO implement for the app class LiteStash


def mk_hash_column() -> Column:
    """Return a Column for the hash"""
    return StashColumns.column(
        ColumnSetup.HASH.value,
        Text,
        index=True,
        unique=True,
        nullable=False
    )


def mk_key_column() -> Column:
    """Return a Column for the key being stored."""
    return StashColumns.column(
        ColumnSetup.KEY.value,
        Text,
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
        primary_key=True
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
