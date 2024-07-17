"""Unit Test Tables_st

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_st import TablesST

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesST.get_table_name("s") == "tables_st_lower_hash_s"
    assert TablesST.get_table_name("t") == "tables_st_lower_hash_t"
    assert TablesST.get_table_name("S") == "tables_st_upper_hash_s"
    assert TablesST.get_table_name("T") == "tables_st_upper_hash_t"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesST.get_table_name("#")

def test_s_low():
    """Tests the zero() method."""
    assert TablesST.s_low() == "tables_st_lower_hash_s"

def test_t_low():
    """Tests the one() method."""
    assert TablesST.t_low() == "tables_st_lower_hash_t"

def test_s_upper():
    """Tests the two() method."""
    assert TablesST.s_upper() == "tables_st_upper_hash_s"

def test_t_upper():
    """Tests the three() method."""
    assert TablesST.t_upper() == "tables_st_upper_hash_t"
