"""The Utilities


"""
from litestash.config import TableName
from litestash.config import Num
from litestash.config import LowerCase
from litestash.config import UpperCase
from litestash.config import SetupDB
from litestash.config import ColumnSetup
from litestash.models import StashColumns
from sqlalchemy.schema import Table
from sqlalchemy.schema import Metadata
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import JSON
from typing import Generator

def setupDB_file(db: str | None):
    """Setup Database file

    Prepare default cache file, or custom name.
    TODO: Path customize && check
    """
    pass


def setupDB_memory():
    """Setup in memory temporary database."""
    pass


def setupDB(db: str | None):
    """Handle correct setupDB function call"""
    if db is None:
        return setupDB_memory()
    return setupDB_file(db)


def mk_id() -> Column:
    """Return the unique id column"""
    return StashColumns.column(
        ColumnSetup.ROW_ID.value,
        Integer,
        primary_key=True
    )


def mk_hash() -> Column:
    """Return a Column for the hash"""
    return     return StashColumns.column(
        ColumnSetup.HASH.value,
        Text,
        index=True,
        unique=True,
        nullable=False
    )


def mk_key() -> Column:
    """Return a Column for the key being stored."""
    return StashColumns.column(
        ColumnSetup.KEY.value,
        Text,
        unique=True,
        index=True,
        nullable=False
    )


def mk_value() -> Column:
    """Return a Column for the value being stored."""
    return StashColumns.column(
        ColumnSetup.VALUE.value,
        JSON,
        nullable-False
    )


def mk_date_created() -> Column:
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
        mk_id(),
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
