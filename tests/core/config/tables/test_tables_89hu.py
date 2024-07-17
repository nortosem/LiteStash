"""Unit Test Tables_89hu

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_89hu import Tables89hu

def test_get_table_name_valid_chars():
    """Tests valid characters 8,9,-,_"""
    assert Tables89hu.get_table_name("8") == "tables_89hu_hash_8"
    assert Tables89hu.get_table_name("9") == "tables_89hu_hash_9"
    assert Tables89hu.get_table_name("-") == "tables_89hu_hash_hyphen"
    assert Tables89hu.get_table_name("_") == "tables_89hu_hash_underscore"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        Tables89hu.get_table_name("a")

def test_eight():
    """Tests the zero() method."""
    assert Tables89hu.eight() == "tables_89hu_hash_8"

def test_nine():
    """Tests the one() method."""
    assert Tables89hu.nine() == "tables_89hu_hash_9"

def test_hyphen():
    """Tests the two() method."""
    assert Tables89hu.hyphen() == "tables_89hu_hash_hyphen"

def test_underscore():
    """Tests the three() method."""
    assert Tables89hu.underscore() == "tables_89hu_hash_underscore"


