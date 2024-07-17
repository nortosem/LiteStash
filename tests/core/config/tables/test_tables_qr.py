"""Unit Test Tables_qr

Full coverage unittesting for configuration
"""
import pytest
from litestash.core.config.schema_conf import Names
from litestash.core.config.root import Tables
from litestash.core.config.tables.tables_qr import TablesQR

def test_get_table_name_valid_chars():
    """Tests valid characters e,f,A,B"""
    assert TablesQR.get_table_name("q") == "tables_qr_lower_hash_q"
    assert TablesQR.get_table_name("r") == "tables_qr_lower_hash_r"
    assert TablesQR.get_table_name("Q") == "tables_qr_upper_hash_q"
    assert TablesQR.get_table_name("R") == "tables_qr_upper_hash_r"

def test_get_table_name_invalid_char():
    """Tests invalid character."""
    with pytest.raises(ValueError, match=Names.ERROR.value):
        TablesQR.get_table_name("#")

def test_q_low():
    """Tests the zero() method."""
    assert TablesQR.q_low() == "tables_qr_lower_hash_q"

def test_r_low():
    """Tests the one() method."""
    assert TablesQR.r_low() == "tables_qr_lower_hash_r"

def test_q_upper():
    """Tests the two() method."""
    assert TablesQR.q_upper() == "tables_qr_upper_hash_q"

def test_r_upper():
    """Tests the three() method."""
    assert TablesQR.r_upper() == "tables_qr_upper_hash_r"

