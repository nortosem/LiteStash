"""The Utilities


"""
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
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Metadata
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import JSON
from typing import Generator


def setup_db_file(db: str | None):
    """Setup Database file

    Prepare default cache file, or custom name.
    TODO: Path customize && check
    """
    if db is None:
        return
    return


def setupDB(db: str | None):
    """Handle correct setupDB function call"""
    return setupDB_file(db)


def setup_engine(engine_name: str) -> Engine:
    """Setup up engine"""
    return create_engine(
        f'{SetupDB.sqlite()}{getcwd()}{SetupDB.filename()}',
        echo=SetupDB.echo.value
    )


def setup_session(engine: Engine):
    """Setup a session"""
    return sessionmaker(bind=self.engine)


def hash_key(key: str) -> str:
    """Get the hashed str for given key"""
    return blake2b(key.encode(), digest_size=Utils.SIZE.value).hexdigest()

def get_hash_table(key: str): -> ?:
    """Given a hashed key return the table and database for the hash."""
    table_name = ''
    db_name = ''


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


def mk_date_column() -> Column:
    """Return a Column for the date the data was added."""
    return StashColumns.get_column(
        ColumnSetup.DATE_CREATED.value,
        Integer,
        primary_key=True
    )


def mk_columns() -> Generator[Column, None, None]:
    """Make Columns

    Return a generator for all columns used in each table.
    """
    for column in (
        mk_hash(),
        mk_key(),
        mk_val(),
        mk_date_created()
    ):
        yield column


def mk_table_names() -> Generator[str, None, None]:
    """Make all valid Table names

    Generate names for all tables in cache
    Return a generator.
    """
    for chars in (Num,LowerCase,UpperCase):
        for suffix in chars:
            yield f'{TableName.ROOT.value}{suffix.value}'


def mk_tables(metadata: Metadata) -> Generator[Table, None, None]:
    """Make Tables

    Create all tables using preset columns and names.
    """
    for table_name in mk_table_names():
        yield Table(
            table_name,
            metadata,
            *(column for column in mk_columns())
        )
