"""Unit Test Tables_03

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_03 import Tables03

def test_get_table_name_valid_chars():
    """Tests valid characters 0-3."""
    assert Tables03.get_table_name("0") == "tables_03_hash_0"
    assert Tables03.get_table_name("1") == "tables_03_hash_1"
    assert Tables03.get_table_name("2") == "tables_03_hash_2"
    assert Tables03.get_table_name("3") == "tables_03_hash_3"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        Tables03.get_table_name("a")

def test_zero():
    """Tests the zero() method."""
    assert Tables03.zero() == "tables_03_hash_0"

def test_one():
    """Tests the one() method."""
    assert Tables03.one() == "tables_03_hash_1"

def test_two():
    """Tests the two() method."""
    assert Tables03.two() == "tables_03_hash_2"

def test_three():
    """Tests the three() method."""
    assert Tables03.three() == "tables_03_hash_3"
