"""Unit Test Tables_kl

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_kl import TablesKL

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesKL.get_table_name("k") == "tables_kl_lower_hash_k"
    assert TablesKL.get_table_name("l") == "tables_kl_lower_hash_l"
    assert TablesKL.get_table_name("K") == "tables_kl_upper_hash_k"
    assert TablesKL.get_table_name("L") == "tables_kl_upper_hash_l"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesKL.get_table_name("#")

def test_k_low():
    """Tests the zero() method."""
    assert TablesKL.k_low() == "tables_kl_lower_hash_k"

def test_l_low():
    """Tests the one() method."""
    assert TablesKL.l_low() == "tables_kl_lower_hash_l"

def test_k_upper():
    """Tests the two() method."""
    assert TablesKL.k_upper() == "tables_kl_upper_hash_k"

def test_l_upper():
    """Tests the three() method."""
    assert TablesKL.l_upper() == "tables_kl_upper_hash_l"




