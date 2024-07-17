import pytest
from litestash.core.config.schema_conf import (
    Valid, Pragma, ColumnSetup, ColumnConfig
)

def test_pragma_values():
    assert Pragma.CONNECT.value == 'connect'
    assert Pragma.PRAGMA.value == 'PRAGMA'
    assert Pragma.JOURNAL_MODE.value == 'journal_mode=WAL'
    assert Pragma.SYNCHRONOUS.value == 'synchronous=NORMAL'
    assert Pragma.FOREIGN_KEYS.value == 'foreign_keys=ON'

def test_pragma_methods():
    assert Pragma.journal_mode() == 'PRAGMA journal_mode=WAL'
    assert Pragma.synchronous() == 'PRAGMA synchronous=NORMAL'
    assert Pragma.foreign_keys() == 'PRAGMA foreign_keys=ON'

def test_column_setup_values():
    assert ColumnSetup.HASH.value == 'key_hash'
    assert ColumnSetup.KEY.value == 'key'
    assert ColumnSetup.VALUE.value == 'value'
    assert ColumnSetup.TIMESTAMP.value == 'timestamp'
    assert ColumnSetup.MS_TIME.value == 'microseconds'

def test_column_config_values():
    assert ColumnConfig.TYPE_NAME.value == 'ColumnTypes'
    assert ColumnConfig.TYPE_STR.value == 'literal'

