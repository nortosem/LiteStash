"""The Database Table Build Functions

TODO: docs
"""
from sqlalchemy import Column
from typing import Generator
from litestash.models import StashColumn
from litestash.core.config.schema_conf import ColumnSetup as Col
from litestash.core.config.schema_conf import ColumnConfig as Conf
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

def get_tables_03() -> Generator[str, None, None]:
    """Generate all table names for 0-3"""
    for char in Tables03:
        table_name = Tables03.get_table_name(char.value)
        yield table_name


def get_tables_47() -> Generator[str, None, None]:
    """Generate all table names for 4-7"""
    for char in Tables47:
        table_name = Tables47.get_table_name(char.value)
        yield table_name


def get_tables_89hu() -> Generator[str, None, None]:
    """Generate all table names for 8,9,-,_"""
    for char in Tables89hu:
        table_name = Tables89hu.get_table_name(char.value)
        yield table_name


def get_tables_ab() -> Generator[str, None, None]:
    """Generate all table names for a,b,A,B"""
    for char in TablesAB:
        table_name = TablesAB.get_table_name(char.value)
        yield table_name


def get_tables_cd() -> Generator[str, None, None]:
    """Generate all table names for c,d,C,D"""
    for char in TablesCD:
        table_name = TablesCD.get_table_name(char.value)
        yield table_name


def get_tables_ef() -> Generator[str, None, None]:
    """Generate all table names for e,f,E,F"""
    for char in TablesEF:
        table_name = TablesEF.get_table_name(char.value)
        yield table_name


def get_tables_gh() -> Generator[str, None, None]:
    """Generate all table names for g,h,G,H"""
    for char in TablesGH:
        table_name = TablesGH.get_table_name(char.value)
        yield table_name


def get_tables_ij() -> Generator[str, None, None]:
    """Generate all table names for i,j,I,J"""
    for char in TablesIJ:
        table_name = TablesIJ.get_table_name(char.value)
        yield table_name

def get_tables_kl() -> Generator[str, None, None]:
    """Generate all table names for k,l,K,L"""
    for char in TablesKL:
        table_name = TablesKL.get_table_name(char.value)
        yield table_name

def get_tables_mn() -> Generator[str, None, None]:
    """Generate all table names for m,n,M,N"""
    for char in TablesMN:
        table_name = TablesMN.get_table_name(char.value)
        yield table_name


def get_tables_op() -> Generator[str, None, None]:
    """Generate all table names for o,p,O,P"""
    for char in TablesOP:
        table_name = TablesOP.get_table_name(char.value)
        yield table_name


def get_tables_qr() -> Generator[str, None, None]:
    """Generate all table names for q,r,Q,R"""
    for char in TablesQR:
        table_name = TablesQR.get_table_name(char.value)
        yield table_name


def get_tables_st() -> Generator[str, None, None]:
    """Generate all table names for s,t,S,T"""
    for char in TablesST:
        table_name = TablesST.get_table_name(char.value)
        yield table_name

def get_tables_uv() -> Generator[str, None, None]:
    """Generate all table names for u,v,U,V"""
    for char in TablesUV:
        table_name = TablesUV.get_table_name(char.value)
        yield table_name

def get_tables_wx() -> Generator[str, None, None]:
    """Generate all table names for w,x,W,X"""
    for char in TablesWX:
        table_name = TablesWX.get_table_name(char.value)
        yield table_name

def get_tables_yz() -> Generator[str, None, None]:
    """Generate all table names for y,z,Y,Z"""
    for char in TablesYZ:
        table_name = TablesYZ.get_table_name(char.value)
        yield table_name

def get_column(stash_column: StashColumn) -> Column:
    """Create columns for database tables"""
    column = Column(
        stash_column.name,
        stash_column.type_,
        primary_key=stash_column.primary_key,
        index=stash_column.index,
        unique=stash_column.unique,
    )
    return column

def mk_hash_column() -> Column:
    """Return a Column for the hash"""
    stash_column = StashColumn(
        name=Col.HASH.value,
        type_=Conf.STR.value,
        primary_key=True,
    )
    return get_column(stash_column)


def mk_key_column() -> Column:
    """Return a Column for the key being stored."""
    key_column = StashColumn(
        name=Col.KEY.value,
        type_=Conf.STR.value,
        unique=True,
        index=True
    )
    return get_column(key_column)


def mk_value_column() -> Column:
    """Return a Column for the value being stored."""
    value_column = StashColumn(
        name=Col.VALUE.value,
        type_=Conf.JSON.value,
    )
    return get_column(value_column)


def mk_timestamp_column() -> Column:
    """Return a Column for the unix timestamp for when the data was added."""
    timestamp = StashColumn(
        name=Col.TIMESTAMP,
        type_=Conf.INT.value
    )
    return get_column(timestamp)


def mk_microseconds_column() -> Column:
    """Return a Column for the micrseconds linked to the timestamp"""
    ms = StashColumn(
        name=Col.MICROSECOND.value,
        type_=Conf.INT.value
    )
    return get_column(ms)

def mk_columns() -> Generator[Column, None, None]:
    """Make Columns

    Return a generator for all columns used in each table.
    """
    for column in (
        mk_hash_column(),
        mk_key_column(),
        mk_value_column(),
        mk_timestamp_column(),
        mk_microseconds_column()
    ):
        yield column
