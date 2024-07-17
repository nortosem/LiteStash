"""Unit Test Tables_ef

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_ef import TablesEF

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesEF.get_table_name("e") == "tables_ef_lower_hash_e"
    assert TablesEF.get_table_name("f") == "tables_ef_lower_hash_f"
    assert TablesEF.get_table_name("E") == "tables_ef_upper_hash_e"
    assert TablesEF.get_table_name("F") == "tables_ef_upper_hash_f"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesEF.get_table_name("#")

def test_e_low():
    """Tests the zero() method."""
    assert TablesEF.e_low() == "tables_ef_lower_hash_e"

def test_f_low():
    """Tests the one() method."""
    assert TablesEF.f_low() == "tables_ef_lower_hash_f"

def test_e_upper():
    """Tests the two() method."""
    assert TablesEF.e_upper() == "tables_ef_upper_hash_e"

def test_f_upper():
    """Tests the three() method."""
    assert TablesEF.f_upper() == "tables_ef_upper_hash_f"

