"""LiteStash Table Utilities

This module provides helper functions for creating and managing SQLAlchemy Table
objects used in the LiteStash key-value store. It includes functions for:

- Generating table names based on hash prefixes.
- Creating tables with predefined columns.
- Defining standard column objects for consistent table structures.
"""
from enum import Enum
from sqlalchemy import Column
from typing import Generator
from typing import Callable
from typing import Type
from litestash.logging import root_logger as logger
from litestash.models import StashColumn
from litestash.core.config.root import Table
from litestash.core.config.default_exceptions.util_exceptions import \
    TableUtilErrorMessages
from litestash.core.config.tables.tables_03 import Tables03
from litestash.core.config.tables.tables_47 import Tables47
from litestash.core.config.tables.tables_89hu import Tables89hu
from litestash.core.config.tables.tables_ab import TablesAB
from litestash.core.config.tables.tables_cd import TablesCD
from litestash.core.config.tables.tables_ef import TablesEF
from litestash.core.config.tables.tables_gh import TablesGH
from litestash.core.config.tables.tables_ij import TablesIJ
from litestash.core.config.tables.tables_kl import TablesKL
from litestash.core.config.tables.tables_mn import TablesMN
from litestash.core.config.tables.tables_op import TablesOP
from litestash.core.config.tables.tables_qr import TablesQR
from litestash.core.config.tables.tables_st import TablesST
from litestash.core.config.tables.tables_uv import TablesUV
from litestash.core.config.tables.tables_wx import TablesWX
from litestash.core.config.tables.tables_yz import TablesYZ
from litestash.core.config.schema_conf import ColumnFields as Col
from litestash.core.config.schema_conf import ColumnConfig as Conf
from litestash.exceptions.core.util.table_util_expceptions import \
    InvalidStashColumnError
from litestash.exceptions.core.util.table_util_expceptions import \
    InvalidTableClassError
from litestash.exceptions.core.util.table_util_expceptions import \
    NoneTableClassError
from litestash.exceptions.core.util.table_util_expceptions import \
    ParentTableClassError
from litestash.exceptions.core.util.table_util_expceptions import \
    StashColumnTypeError
from litestash.exceptions.core.util.table_util_expceptions import \
    TableNameNotFoundError
from litestash.exceptions.core.util.table_util_expceptions import \
    TableUtilError


def _generator(
    table_class: Type[Table]
) -> Callable[, Generator[str, None, None]]:
    """Internal utility for mk_table_generator"""
    for char in table_class:
        table_name = table_class.get_table_name(char.value)
        if not table_name:
            logger.error(ErrorMessage.GET_ENGINE.value)
            raise TableNameNotFoundError()
        yield table_name

            logger.error('Table name not found')
            raise ValueError('No such table found.')
        yield table_name


def mk_table_generator(
    table_class: Type[Table]
) -> Callable[, Generator[str, None, None]]:
    """Tablename generator factory"""
    if table_class is None:
        logger.error(
            f'Tables cannot be Nothing: ({table_class},{type(table_class)})'
        )
        raise NoneTableClassError()
    try:
        if not issubclass(table_class, Table):
            logger.error(f'Invalid table classe: {table_class}')
            raise InvalidTableClassError()

        if table_class == Table:
            logger.error(f'A specific table is required')
            raise ParentTableClassError()

    except TypeError as e:
        logger.error(f'A valid Table class is required: {type(table_class)}')
        raise InvalidTableClassError()

    return lambda: _generator(table_class)


get_tables_03 = mk_table_generator(Tables03)
"""Generates table names for the '0-3' hash prefix database."""

get_tables_47 = mk_table_generator(Tables47)
"""Generates table names for the '4-7' hash prefix database."""

get_tables_89hu = mk_table_generator(Tables89hu)
"""Generates table names for the '8,9,-,_' hash prefix database"""

get_tables_ab = mk_table_generator(TablesAB)
"""Generates table names for the 'a,b,A,B' hash prefix database"""

get_tables_cd = mk_table_generator(TablesCD)
"""Generates table names for the c,d,C,D hash prefix database"""

get_tables_ef = mk_table_generator(TablesEF)
"""Generates table names for the e,f,E,F hash prefix database"""

get_tables_gh = mk_table_generator(TablesGH)
"""Generates table names for the g,h,G,H hash prefix database"""

get_tables_ij = mk_table_generator(TablesIJ)
"""Generates table names for the i,j,I,J hash prefix database"""

get_tables_kl = mk_table_generator(TablesKL)
"""Generates table names for the k,l,K,L  hash prefix database"""

get_tables_mn = mk_table_generator(TablesMN)
"""Generates table names for the m,n,M,N hash prefix database"""

get_tables_op = mk_table_generator(TablesOP)
"""Generates table names for the o,p,O,P hash prefix database"""

get_tables_qr = mk_table_generator(TablesQR)
"""Generates table names for the q,r,Q,R hash prefix database"""

get_tables_st = mk_table_generator(TablesST)
"""Generates table names for the s,t,S,T hash prefix database"""

get_tables_uv = mk_table_generator(TablesUV)
"""Generates table names for the u,v,U,V hash prefix database"""

get_tables_wx = mk_table_generator(TablesWX)
"""Generates table names for the w,x,W,X hash prefix database"""

get_tables_yz = mk_table_generator(TablesYZ)
"""Generates table names for the y,z,Y,Z hash prefix database"""


def get_column(stash_column: StashColumn) -> Column:
    """Creates a SQLAlchemy Column object from a StashColumn definition."""
    if stash_column is None:
        logger.error('None is not a valid table column')
        raise InvalidStashColumnError()

    if not isinstance(stash_column, StashColumn):
        logger.error(f'Invalid stash_column type: {type(stash_column)}'
        raise StashColumnTypeError()

    column = Column(
        stash_column.name,
        stash_column.type_,
        primary_key=stash_column.primary_key,
        index=stash_column.index,
        unique=stash_column.unique,
    )
    return column


def mk_hash_column() -> Column:
    """Returns a SQLAlchemy Column for the 'key_hash' column."""
    stash_column = StashColumn(
        name=Col.HASH.value,
        type_=Conf.STR.value,
        primary_key=True,
    )
    return get_column(stash_column)


def mk_key_column() -> Column:
    """Returns a SQLAlchemy Column for the 'key' column."""
    key_column = StashColumn(
        name=Col.KEY.value,
        type_=Conf.STR.value,
        unique=True,
        index=True
    )
    return get_column(key_column)


def mk_value_column() -> Column:
    """Returns a SQLAlchemy Column for the 'value' column."""
    value_column = StashColumn(
        name=Col.VALUE.value,
        type_=Conf.JSON.value,
    )
    return get_column(value_column)


def mk_timestamp_column() -> Column:
    """Returns a SQLAlchemy Column for the 'timestamp' column."""
    timestamp = StashColumn(
        name=Col.TIMESTAMP.value,
        type_=Conf.INT.value
    )
    return get_column(timestamp)


def mk_microseconds_column() -> Column:
    """Returns a SQLAlchemy Column for the 'microsecond' column."""
    ms = StashColumn(
        name=Col.MICROSECOND.value,
        type_=Conf.INT.value
    )
    return get_column(ms)


def mk_columns() -> Generator[Column, None, None]:
    """Generates all SQLAlchemy Column objects for a standard LiteStash table.
    """
    for column in (
        mk_hash_column(),
        mk_key_column(),
        mk_value_column(),
        mk_timestamp_column(),
        mk_microseconds_column()
    ):
        yield column
