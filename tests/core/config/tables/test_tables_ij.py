"""Unit Test Tables_ij

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_ij import TablesIJ

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesIJ.get_table_name("i") == "tables_ij_lower_hash_i"
    assert TablesIJ.get_table_name("j") == "tables_ij_lower_hash_j"
    assert TablesIJ.get_table_name("I") == "tables_ij_upper_hash_i"
    assert TablesIJ.get_table_name("J") == "tables_ij_upper_hash_j"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesIJ.get_table_name("#")

def test_i_low():
    """Tests the zero() method."""
    assert TablesIJ.i_low() == "tables_ij_lower_hash_i"

def test_j_low():
    """Tests the one() method."""
    assert TablesIJ.j_low() == "tables_ij_lower_hash_j"

def test_i_upper():
    """Tests the two() method."""
    assert TablesIJ.i_upper() == "tables_ij_upper_hash_i"

def test_j_upper():
    """Tests the three() method."""
    assert TablesIJ.j_upper() == "tables_ij_upper_hash_j"



