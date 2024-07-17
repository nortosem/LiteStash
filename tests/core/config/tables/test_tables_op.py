"""Unit Test Tables_op

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_op import TablesOP

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesOP.get_table_name("o") == "tables_op_lower_hash_o"
    assert TablesOP.get_table_name("p") == "tables_op_lower_hash_p"
    assert TablesOP.get_table_name("O") == "tables_op_upper_hash_o"
    assert TablesOP.get_table_name("P") == "tables_op_upper_hash_p"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesOP.get_table_name("#")

def test_o_low():
    """Tests the zero() method."""
    assert TablesOP.o_low() == "tables_op_lower_hash_o"

def test_p_low():
    """Tests the one() method."""
    assert TablesOP.p_low() == "tables_op_lower_hash_p"

def test_o_upper():
    """Tests the two() method."""
    assert TablesOP.o_upper() == "tables_op_upper_hash_o"

def test_p_upper():
    """Tests the three() method."""
    assert TablesOP.p_upper() == "tables_op_upper_hash_p"
