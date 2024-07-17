"""Unit Test Tables_ab

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_ab import TablesAB

def test_get_table_name_valid_chars():
    """Tests valid characters a,b,A,B"""
    assert TablesAB.get_table_name("a") == "tables_ab_lower_hash_a"
    assert TablesAB.get_table_name("b") == "tables_ab_lower_hash_b"
    assert TablesAB.get_table_name("A") == "tables_ab_upper_hash_a"
    assert TablesAB.get_table_name("B") == "tables_ab_upper_hash_b"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesAB.get_table_name("#")

def test_a_low():
    """Tests the zero() method."""
    assert TablesAB.a_low() == "tables_ab_lower_hash_a"

def test_b_low():
    """Tests the one() method."""
    assert TablesAB.b_low() == "tables_ab_lower_hash_b"

def test_a_upper():
    """Tests the two() method."""
    assert TablesAB.a_upper() == "tables_ab_upper_hash_a"

def test_b_upper():
    """Tests the three() method."""
    assert TablesAB.b_upper() == "tables_ab_upper_hash_b"



