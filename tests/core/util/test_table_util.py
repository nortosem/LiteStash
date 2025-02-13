"""Test table_util module

Test the mk_table_gnerator and ensure all of the get_tables_* work.
Test the get_column(StashColumn) function returns the correct column for all
valid columns #TODO
Test each mk_*_column function and edge cases with the mk_columns function test.
#TODO individual assertion and raises tests for all mk_* functions.



"""
from typing import Generator
from typing import Callable
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, JSON, String
import pytest
from unittest.mock import patch
from litestash.core.util.table_util import get_column, mk_hash_column, mk_key_column, mk_value_column, mk_timestamp_column, mk_microseconds_column, mk_columns
from litestash.models import StashColumn
from litestash.core.config.schema_conf import ColumnFields as Col
from litestash.core.config.schema_conf import ColumnConfig as Conf
from litestash.models import StashColumn, ColumnType
from litestash.core.util.schema_util import *
from sqlalchemy import MetaData
from litestash.core.config import tables as test_tables
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
from litestash.core.config.schema_conf import Names
from litestash.core.util import table_util


@pytest.mark.parametrize(
    'get_tables, valid_table_names',
    [
        (Tables03, [
            "tables_03_hash_0",
            "tables_03_hash_1",
            "tables_03_hash_2",
            "tables_03_hash_3"
        ]),
        (Tables47, [
            'tables_47_hash_4',
            'tables_47_hash_5',
            'tables_47_hash_6',
            'tables_47_hash_7'
        ]),
        (Tables89hu, [
            'tables_89hu_hash_8',
            'tables_89hu_hash_9',
            'tables_89hu_hash_hyphen',
            'tables_89hu_hash_underscore'
        ]),
        (TablesAB, [
            'tables_ab_lower_hash_a',
            'tables_ab_lower_hash_b',
            'tables_ab_upper_hash_a',
            'tables_ab_upper_hash_b'
        ]),
        (TablesCD, [
            'tables_cd_lower_hash_c',
            'tables_cd_lower_hash_d',
            'tables_cd_upper_hash_c',
            'tables_cd_upper_hash_d'
        ]),
        (TablesEF, [
            'tables_ef_lower_hash_e',
            'tables_ef_lower_hash_f',
            'tables_ef_upper_hash_e',
            'tables_ef_upper_hash_f'
        ]),
        (TablesGH, [
            'tables_gh_lower_hash_g',
            'tables_gh_lower_hash_h',
            'tables_gh_upper_hash_g',
            'tables_gh_upper_hash_h'
        ]),
        (TablesIJ, [
            'tables_ij_lower_hash_i',
            'tables_ij_lower_hash_j',
            'tables_ij_upper_hash_i',
            'tables_ij_upper_hash_j'
        ]),
        (TablesKL, [
            'tables_kl_lower_hash_k',
            'tables_kl_lower_hash_l',
            'tables_kl_upper_hash_k',
            'tables_kl_upper_hash_l'
        ]),
        (TablesMN, [
            'tables_mn_lower_hash_m',
            'tables_mn_lower_hash_n',
            'tables_mn_upper_hash_m',
            'tables_mn_upper_hash_n'
        ]),
        (TablesOP, [
            'tables_op_lower_hash_o',
            'tables_op_lower_hash_p',
            'tables_op_upper_hash_o',
            'tables_op_upper_hash_p'
        ]),
        (TablesQR, [
            'tables_qr_lower_hash_q',
            'tables_qr_lower_hash_r',
            'tables_qr_upper_hash_q',
            'tables_qr_upper_hash_r'
        ]),
        (TablesST, [
            'tables_st_lower_hash_s',
            'tables_st_lower_hash_t',
            'tables_st_upper_hash_s',
            'tables_st_upper_hash_t'
        ]),
        (TablesUV, [
            'tables_uv_lower_hash_u',
            'tables_uv_lower_hash_v',
            'tables_uv_upper_hash_u',
            'tables_uv_upper_hash_v'
        ]),
        (TablesWX, [
            'tables_wx_lower_hash_w',
            'tables_wx_lower_hash_x',
            'tables_wx_upper_hash_w',
            'tables_wx_upper_hash_x'
        ]),
        (TablesYZ, [
            'tables_yz_lower_hash_y',
            'tables_yz_lower_hash_z',
            'tables_yz_upper_hash_y',
            'tables_yz_upper_hash_z'
        ])
    ]
)
def test_get_table_names(monkeypatch, get_tables, valid_table_names):
    """Test all of table name generator functions"""
    table_name_generator = table_util.mk_table_generator(get_tables)
    assert isinstance(table_name_generator, Callable), f"""
        {table_name_generator} must return a list of table names"""

    table_names = list(table_name_generator())
    assert len(table_names) == len(valid_table_names), f"invalid table list"

    for table_name in table_names:
        assert table_name in valid_table_names, f"Invalid table name"


@pytest.fixture
def mock_empty_table_class():
    """A mock class for testing the empty generator case."""
    class MockTable:
        def __init__(self):
            self.values = []

        def __iter__(self):
            return iter(self.values)

        @staticmethod
        def get_table_name(value):
            return f"mock_table_{value}"

    yield MockTable()


class MockBadTable:
    """Invalid subclass"""
    pass


def test_get_invalid_table_names(mock_empty_table_class):
    """Test mk_table_generator errors"""
    with pytest.raises(ValueError) as error_info:
        tng = table_util.mk_table_generator(None)
    assert 'Invalid value' in str(error_info.value)

    with pytest.raises(TypeError) as error_info:
        tng = table_util.mk_table_generator(MockBadTable)
    assert 'Incorrect table type' in str(error_info.value)


class MockColumn:
    """A mock column class"""
    def __init__(
        self,
        name,
        type_,
        primary_key=False,
        index=False,
        unique=False,
    ):
        self.name = name
        self.type = type_
        self.primary_key = primary_key
        self.index = index
        self.unique = unique

    def __eq__(self, other):
        """Custom equality check for comparing mock columns."""
        return (
            self.name == other.name
            and self.type == other.type
            and self.primary_key == other.primary_key
            and self.index == other.index
            and self.unique == other.unique
        )


@pytest.fixture
def mock_stash_column():
    return StashColumn(name="test", type_=Conf.STR.value)


@pytest.fixture
def mock_sqlalchemy_column():
    with patch("sqlalchemy.Column", new=MockColumn) as mock_column:
        yield mock_column


def test_get_column(mock_sqlalchemy_column, stash_column, expected_column):
    """Test get_column with various column definitions."""
    column = get_column(stash_column)
    assert column == expected_column


def test_mk_columns(mock_sqlalchemy_column):
    columns = list(mk_columns())
    assert len(columns) == 5
    assert isinstance(columns[0], MockColumn) and columns[0].name == Col.HASH.value

@pytest.fixture(params=[
    ("0", "tables_03"),
    ("1", "tables_03"),
    ("2", "tables_03"),
    ("3", "tables_03"),
    ("4", "tables_47"),
    ("5", "tables_47"),
    ("6", "tables_47"),
    ("7", "tables_47"),
    ("8", "tables_89hu"),
    ("9", "tables_89hu"),
    ("-", "tables_89hu"),
    ("_", "tables_89hu"),
    ("a", "tables_ab"),
    ("b", "tables_ab"),
    ("c", "tables_cd"),
    ("d", "tables_cd"),
    ("e", "tables_ef"),
    ("f", "tables_ef"),
    ("g", "tables_gh"),
    ("h", "tables_gh"),
    ("i", "tables_ij"),
    ("j", "tables_ij"),
    ("k", "tables_kl"),
    ("l", "tables_kl"),
    ("m", "tables_mn"),
    ("n", "tables_mn"),
    ("o", "tables_op"),
    ("p", "tables_op"),
    ("q", "tables_qr"),
    ("r", "tables_qr"),
    ("s", "tables_st"),
    ("t", "tables_st"),
    ("u", "tables_uv"),
    ("v", "tables_uv"),
    ("w", "tables_wx"),
    ("x", "tables_wx"),
    ("y", "tables_yz"),
    ("z", "tables_yz"),
    ("A", "tables_ab"),
    ("B", "tables_ab"),
    ("C", "tables_cd"),
    ("D", "tables_cd"),
    ("E", "tables_ef"),
    ("F", "tables_ef"),
    ("G", "tables_gh"),
    ("H", "tables_gh"),
    ("I", "tables_ij"),
    ("J", "tables_ij"),
    ("K", "tables_kl"),
    ("L", "tables_kl"),
    ("M", "tables_mn"),
    ("N", "tables_mn"),
    ("O", "tables_op"),
    ("P", "tables_op"),
    ("Q", "tables_qr"),
    ("R", "tables_qr"),
    ("S", "tables_st"),
    ("T", "tables_st"),
    ("U", "tables_uv"),
    ("V", "tables_uv"),
    ("W", "tables_wx"),
    ("X", "tables_wx"),
    ("Y", "tables_yz"),
    ("Z", "tables_yz"),
])
def valid_hash_and_db_name(request):
    """Yields valid hash prefixes and their corresponding database names."""
    yield request.param


def test_get_none_column():
    """Test get_column with None for the Stash_Column"""
    with pytest.raises(ValueError) as error_info:
        get_column(None)
    assert 'Table column cannot be None' in str(error_info.value)


def test_get_invalid_column():
    """Test get_column with non-stash_column"""
    with pytest.raises(TypeError) as error_info:
        get_column(object())
    assert 'Invalid stash_column type' in str(error_info.value)


def test_get_column():
    """Test get_column function for creating a SQLAlchemy Column object."""
    stash_column = StashColumn(name='test_col', type_=Conf.STR.value)
    column = get_column(stash_column)
    assert isinstance(column, Column)
    assert column.name == 'test_col'
    assert column.type.__class__.__name__ == Conf.STR.value


def test_mk_hash_column():
    column = mk_hash_column()
    assert isinstance(column, Column)
    assert column.name == Col.HASH.value
    assert column.primary_key
    assert column.type.__class__.__name__ == Conf.STR.value


def test_mk_columns():
    """Test mk_columns generator to ensure it yields the correct columns."""
    columns = list(mk_columns())
    assert len(columns) == 5

    assert isinstance(columns[0], Column)
    assert columns[0].name == Col.HASH.value
    assert columns[0].primary_key

