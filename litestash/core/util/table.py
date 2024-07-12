"""The Database Table Build Functions

TODO: docs
"""
from litestash.core.config import ColumnSetup as Col
from litestash.core.config import ColumnConfig
from litestash.models import StashColumns
from collections import namedtuple
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import BLOB
from typing import Generator
from typing import Optional

def mk_hash_column() -> Column:
    """Return a Column for the hash"""
    return StashColumns.column(
        Col.HASH.value,
        BLOB,
        primary_key=True,
        nullable=False
    )


def mk_key_column() -> Column:
    """Return a Column for the key being stored."""
    return StashColumns.column(
        Col.KEY.value,
        BLOB,
        unique=True,
        index=True,
        nullable=False
    )


def mk_value_column() -> Column:
    """Return a Column for the value being stored."""
    return StashColumns.column(
        Col.VALUE.value,
        JSON,
        nullable=True
    )


def mk_time_column() -> Column:
    """Return a Column for the date the data was added."""
    return StashColumns.get_column(
        Col.TIME.value,
        Integer,
        nullable=True
        )


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


ColumnType = namedtuple(
    ColumnConfig.TYPE_NAME.value,
    [
        ColumnConfig.TYPE_STR.value,
        ColumnConfig.TYPE_DB.value
    ]
)
ColumnType.__doc__ = ColumnType.DOC.value


BlobType = ColumnType(ColumnConfig.BLOB.value, BLOB)
IntegerType = ColumnType(ColumnConfig.INTEGER.value, Integer)
JsonType = ColumnType(ColumnConfig.JSON.value, JSON)

def valid_type(column_type: ColumnType) -> Optional[BLOB,Integer,JSON]:
    """Valid Type Function

    Take a Literal and return sqlite column type.

    Args:
        column_type (ColumnType):
            A namedtuple for blob, int, or json types.
    """
    match column_type:
        case BlobType.literal:
            return BlobType.sqlite
        case IntegerType.literal:
            return IntegerType.sqlite
        case JsonType.literal:
            return JsonType.sqlite
        case _:
            raise ValueError(ColumnConfig.ERROR.value)
