"""Unit Test Tables_yz

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_yz import TablesYZ

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesYZ.get_table_name("y") == "tables_yz_lower_hash_y"
    assert TablesYZ.get_table_name("z") == "tables_yz_lower_hash_z"
    assert TablesYZ.get_table_name("Y") == "tables_yz_upper_hash_y"
    assert TablesYZ.get_table_name("Z") == "tables_yz_upper_hash_z"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesYZ.get_table_name("#")

def test_w_low():
    """Tests the zero() method."""
    assert TablesYZ.y_low() == "tables_yz_lower_hash_y"

def test_x_low():
    """Tests the one() method."""
    assert TablesYZ.z_low() == "tables_yz_lower_hash_z"

def test_w_upper():
    """Tests the two() method."""
    assert TablesYZ.y_upper() == "tables_yz_upper_hash_y"

def test_x_upper():
    """Tests the three() method."""
    assert TablesYZ.z_upper() == "tables_yz_upper_hash_z"


