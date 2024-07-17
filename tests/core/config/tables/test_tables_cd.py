"""Unit Test Tables_cd

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_cd import TablesCD

def test_get_table_name_valid_chars():
    """Tests valid characters a,b,A,B"""
    assert TablesCD.get_table_name("c") == "tables_cd_lower_hash_c"
    assert TablesCD.get_table_name("d") == "tables_cd_lower_hash_d"
    assert TablesCD.get_table_name("C") == "tables_cd_upper_hash_c"
    assert TablesCD.get_table_name("D") == "tables_cd_upper_hash_d"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesCD.get_table_name("#")

def test_c_low():
    """Tests the zero() method."""
    assert TablesCD.c_low() == "tables_cd_lower_hash_c"

def test_d_low():
    """Tests the one() method."""
    assert TablesCD.d_low() == "tables_cd_lower_hash_d"

def test_c_upper():
    """Tests the two() method."""
    assert TablesCD.c_upper() == "tables_cd_upper_hash_c"

def test_d_upper():
    """Tests the three() method."""
    assert TablesCD.d_upper() == "tables_cd_upper_hash_d"
