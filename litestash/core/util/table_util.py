"""The Database Table Build Functions

TODO: docs
"""
from litestash.core.config.schema_conf import ColumnSetup as Col
from litestash.models import StashColumn
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import BLOB
from typing import Generator

def mk_hash_column() -> Column:
    """Return a Column for the hash"""
    return StashColumn.column(
        Col.HASH.value,
        BLOB,
        primary_key=True,
    )


def mk_key_column() -> Column:
    """Return a Column for the key being stored."""
    return StashColumn.column(
        Col.KEY.value,
        BLOB,
        unique=True,
        index=True,
    )


def mk_value_column() -> Column:
    """Return a Column for the value being stored."""
    return StashColumn.column(
        Col.VALUE.value,
        JSON,
    )


def mk_time_column() -> Column:
    """Return a Column for the date the data was added."""
    time_column = StashColumn(Col.TIME.value,Integer)
    return time_column


def mk_columns() -> Generator[Column, None, None]:
    """Make Columns

    Return a generator for all columns used in each table.
    """
    for column in (
        mk_hash_column(),
        mk_key_column(),
        mk_value_column(),
        mk_time_column()
    ):
        yield column