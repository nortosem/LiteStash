"""Unit Test Tables_wx

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_wx import TablesWX

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesWX.get_table_name("w") == "tables_wx_lower_hash_w"
    assert TablesWX.get_table_name("x") == "tables_wx_lower_hash_x"
    assert TablesWX.get_table_name("W") == "tables_wx_upper_hash_w"
    assert TablesWX.get_table_name("X") == "tables_wx_upper_hash_x"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesWX.get_table_name("#")

def test_w_low():
    """Tests the zero() method."""
    assert TablesWX.w_low() == "tables_wx_lower_hash_w"

def test_x_low():
    """Tests the one() method."""
    assert TablesWX.x_low() == "tables_wx_lower_hash_x"

def test_w_upper():
    """Tests the two() method."""
    assert TablesWX.w_upper() == "tables_wx_upper_hash_w"

def test_x_upper():
    """Tests the three() method."""
    assert TablesWX.x_upper() == "tables_wx_upper_hash_x"

