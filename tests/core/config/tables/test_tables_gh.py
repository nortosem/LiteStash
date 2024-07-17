"""Unit Test Tables_gh

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_gh import TablesGH

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesGH.get_table_name("g") == "tables_gh_lower_hash_g"
    assert TablesGH.get_table_name("h") == "tables_gh_lower_hash_h"
    assert TablesGH.get_table_name("G") == "tables_gh_upper_hash_g"
    assert TablesGH.get_table_name("H") == "tables_gh_upper_hash_h"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesGH.get_table_name("#")

def test_g_low():
    """Tests the zero() method."""
    assert TablesGH.g_low() == "tables_gh_lower_hash_g"

def test_h_low():
    """Tests the one() method."""
    assert TablesGH.h_low() == "tables_gh_lower_hash_h"

def test_g_upper():
    """Tests the two() method."""
    assert TablesGH.g_upper() == "tables_gh_upper_hash_g"

def test_h_upper():
    """Tests the three() method."""
    assert TablesGH.h_upper() == "tables_gh_upper_hash_h"


