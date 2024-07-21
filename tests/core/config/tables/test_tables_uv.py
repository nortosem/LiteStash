"""Unit Test Tables_st

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_uv import TablesUV

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesUV.get_table_name("u") == "tables_uv_lower_hash_u"
    assert TablesUV.get_table_name("v") == "tables_uv_lower_hash_v"
    assert TablesUV.get_table_name("U") == "tables_uv_upper_hash_u"
    assert TablesUV.get_table_name("V") == "tables_uv_upper_hash_v"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesUV.get_table_name("#")

def test_u_low():
    """Tests the zero() method."""
    assert TablesUV.u_low() == "tables_uv_lower_hash_u"

def test_v_low():
    """Tests the one() method."""
    assert TablesUV.v_low() == "tables_uv_lower_hash_v"

def test_u_upper():
    """Tests the two() method."""
    assert TablesUV.u_upper() == "tables_uv_upper_hash_u"

def test_v_upper():
    """Tests the three() method."""
    assert TablesUV.v_upper() == "tables_uv_upper_hash_v"
