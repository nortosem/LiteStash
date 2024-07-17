"""Unit Test Tables_47

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_47 import Tables47

def test_get_table_name_valid_chars():
    """Tests valid characters 4-7."""
    assert Tables47.get_table_name("4") == "tables_47_hash_4"
    assert Tables47.get_table_name("5") == "tables_47_hash_5"
    assert Tables47.get_table_name("6") == "tables_47_hash_6"
    assert Tables47.get_table_name("7") == "tables_47_hash_7"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        Tables47.get_table_name("a")

def test_four():
    """Tests the zero() method."""
    assert Tables47.four() == "tables_47_hash_4"

def test_five():
    """Tests the one() method."""
    assert Tables47.five() == "tables_47_hash_5"

def test_six():
    """Tests the two() method."""
    assert Tables47.six() == "tables_47_hash_6"

def test_seven():
    """Tests the three() method."""
    assert Tables47.seven() == "tables_47_hash_7"

