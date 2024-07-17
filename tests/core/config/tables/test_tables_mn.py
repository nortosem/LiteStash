"""Unit Test Tables_mn

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_mn import TablesMN

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesMN.get_table_name("m") == "tables_mn_lower_hash_m"
    assert TablesMN.get_table_name("n") == "tables_mn_lower_hash_n"
    assert TablesMN.get_table_name("M") == "tables_mn_upper_hash_m"
    assert TablesMN.get_table_name("N") == "tables_mn_upper_hash_n"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesMN.get_table_name("#")

def test_m_low():
    """Tests the zero() method."""
    assert TablesMN.m_low() == "tables_mn_lower_hash_m"

def test_n_low():
    """Tests the one() method."""
    assert TablesMN.n_low() == "tables_mn_lower_hash_n"

def test_m_upper():
    """Tests the two() method."""
    assert TablesMN.m_upper() == "tables_mn_upper_hash_m"

def test_n_upper():
    """Tests the three() method."""
    assert TablesMN.n_upper() == "tables_mn_upper_hash_n"





