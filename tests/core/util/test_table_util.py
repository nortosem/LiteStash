"""Test table_util module

Test the mk_table_gnerator and ensure all of the get_tables_* work.
Test the get_column(StashColumn) function returns the correct column for all
valid columns
Test each mk_*_column function and edge cases with the mk_columns function test.
Unit tests and Integration test module.
"""
import logging
import pytest
import random
from typing import Generator, Callable, Type
from sqlalchemy import Column
from unittest.mock import patch, MagicMock
from litestash.core.util import table_util
from litestash.models import StashColumn
from litestash.core.config.schema_conf import ColumnFields as Col
from litestash.core.config.schema_conf import ColumnConfig as Conf
from litestash.core.config.tables import *
#from litestash.exceptions.core_exceptions import LiteStashException
from litestash.exceptions.core.util.table_util_exceptions import *
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
'''
from typing import Generator
from typing import Callable
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, JSON, String
from unittest.mock import patch, MagicMock, Mock
from litestash.core.util.table_util import get_column, mk_hash_column, mk_key_column, mk_value_column, mk_timestamp_column, mk_microseconds_column, mk_columns, mk_table_generator
from litestash.models import StashColumn
from litestash.core.config.schema_conf import ColumnFields as Col
from litestash.core.config.schema_conf import ColumnConfig as Conf
from litestash.models import StashColumn, ColumnType
from litestash.core.util.schema_util import *
from sqlalchemy import MetaData
from litestash.core.config import tables as test_tables

from litestash.core.config.schema_conf import Names
from litestash.core.util import table_util
from litestash.core.config.schema_conf import Names
'''

# Fixtures
@pytest.fixture(params=[
    Tables03, Tables47, Tables89hu, TablesAB, TablesCD, TablesEF,
    TablesGH, TablesIJ, TablesKL, TablesMN, TablesOP, TablesQR,
    TablesST, TablesUV, TablesWX, TablesYZ
])
def table_class(request):
    """Table Class enumerations"""
    return request.param


@pytest.fixture(params=[0,1,2,3])
def test_index(request):
    return request.param


@pytest.fixture(params=[
    ("0", "tables_03"), ("1", "tables_03"), ("2", "tables_03"),
    ("3", "tables_03"), ("4", "tables_47"), ("5", "tables_47"),
    ("6", "tables_47"), ("7", "tables_47"), ("8", "tables_89hu"),
    ("9", "tables_89hu"), ("-", "tables_89hu"), ("_", "tables_89hu"),
    ("a", "tables_ab"), ("b", "tables_ab"), ("c", "tables_cd"),
    ("d", "tables_cd"), ("e", "tables_ef"), ("f", "tables_ef"),
    ("g", "tables_gh"), ("h", "tables_gh"), ("i", "tables_ij"),
    ("j", "tables_ij"), ("k", "tables_kl"), ("l", "tables_kl"),
    ("m", "tables_mn"), ("n", "tables_mn"), ("o", "tables_op"),
    ("p", "tables_op"), ("q", "tables_qr"), ("r", "tables_qr"),
    ("s", "tables_st"), ("t", "tables_st"), ("u", "tables_uv"),
    ("v", "tables_uv"), ("w", "tables_wx"), ("x", "tables_wx"),
    ("y", "tables_yz"), ("z", "tables_yz"), ("A", "tables_ab"),
    ("B", "tables_ab"), ("C", "tables_cd"), ("D", "tables_cd"),
    ("E", "tables_ef"), ("F", "tables_ef"), ("G", "tables_gh"),
    ("H", "tables_gh"), ("I", "tables_ij"), ("J", "tables_ij"),
    ("K", "tables_kl"), ("L", "tables_kl"), ("M", "tables_mn"),
    ("N", "tables_mn"), ("O", "tables_op"), ("P", "tables_op"),
    ("Q", "tables_qr"), ("R", "tables_qr"), ("S", "tables_st"),
    ("T", "tables_st"), ("U", "tables_uv"), ("V", "tables_uv"),
    ("W", "tables_wx"), ("X", "tables_wx"), ("Y", "tables_yz"),
    ("Z", "tables_yz"),
])
def valid_hash_and_db_name(request):
    """Yields valid hash prefixes and their corresponding database names."""
    return request.param


@pytest.fixture
def mock_stash_column():
    return StashColumn(name="test", type_=Conf.STR.value)

'''
@pytest.fixture
def mock_sqlalchemy_column():
    with patch("sqlalchemy.Column", new=MagicMock) as mock_column:
        yield mock_column
'''
@pytest.fixture
def mock_sqlalchemy_column():
    with patch("sqlalchemy.Column", new=MockColumn) as mock_column:
        yield mock_column


@pytest.fixture
def expected_column():
    return Column("test", Conf.STR.value)
# End Fixtures

# Test mk_table_generator
def test_generator_util(caplog, table_class):
    """Test retrieval of all valid tables"""
    table_name_generator = table_util.mk_table_generator(table_class)
    table_names = list(table_name_generator())
    assert all(
        table_class.get_table_name(char.value) in table_names
        for char in table_class
    )
    assert not caplog.records

