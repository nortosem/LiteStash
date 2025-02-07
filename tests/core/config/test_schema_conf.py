import pytest
from litestash.core.config.schema_conf import (
    Valid, Pragma, ColumnFields, ColumnConfig, Names, Sql
)

def test_pragma_values():
    assert Pragma.CONNECT.value == 'connect'
    assert Pragma.JOURNAL_MODE.value == 'journal_mode=WAL;'
    assert Pragma.SYNCHRONOUS.value == 'synchronous=NORMAL;'
    assert Pragma.FOREIGN_KEYS.value == 'foreign_keys=ON;'
    assert Pragma.JSON.value == 'json_valid = 1;'

def test_pragma_methods():
    assert Pragma.journal_mode() == 'PRAGMA journal_mode=WAL;'
    assert Pragma.synchronous() == 'PRAGMA synchronous=NORMAL;'
    assert Pragma.foreign_keys() == 'PRAGMA foreign_keys=ON;'
    assert Pragma.valid_json() == 'PRAGMA json_valid = 1;'


def test_column_fields_values():
    assert ColumnFields.HASH.value == 'key_hash'
    assert ColumnFields.KEY.value == 'key'
    assert ColumnFields.VALUE.value == 'value'
    assert ColumnFields.TIMESTAMP.value == 'timestamp'
    assert ColumnFields.MICROSECOND.value == 'microsecond'
    assert ColumnFields.TABLE_NAME.value == 'table_name'


def test_column_config_values():
    assert ColumnConfig.TYPE_NAME.value == 'ColumnTypes'
    assert ColumnConfig.TYPE_STR.value == 'literal'
    assert ColumnConfig.TYPE_DB.value == 'sqlite'
    assert ColumnConfig.STR.value == 'String'
    assert ColumnConfig.INT.value == 'Integer'
    assert ColumnConfig.JSON.value == 'JSON'
    assert ColumnConfig.STASH_COLUMN.value == 'type_'
    assert ColumnConfig.DATA_KEY.value == 'key'
    assert ColumnConfig.DATA_VALUE.value == 'value'
    assert ColumnConfig.DOC.value == 'todo'
    assert ColumnConfig.ERROR.value == "Input should be 'String', 'Integer' or 'JSON'"


def test_names_values():
    assert Names.HYPHEN.value == 'hyphen'
    assert Names.UNDER.value == 'underscore'
    assert Names.HASH.value == '_hash_'
    assert Names.LOW.value == '_lower'
    assert Names.UP.value == '_upper'
    assert Names.DB.value == '.db'
    assert Names.ERROR.value == 'Invalid character request'

def test_sql_values():
    assert Sql.PRAGMA.value == 'PRAGMA'
    assert Sql.BEGIN.value == 'BEGIN'
    assert Sql.INSERT.value == 'INSERT INTO'
    assert Sql.DELETE.value == 'DELETE FROM'
    assert Sql.AND.value == 'AND'
    assert Sql.WHERE.value == 'WHERE'
    assert Sql.VALUES.value == 'VALUES'
    assert Sql.NEW.value == 'NEW'
    assert Sql.OLD.value == 'OLD'
    assert Sql.END.value == 'END;'


def test_sql_methods():
    assert Sql.begin() == 'BEGIN'
    assert Sql.insert() == 'INSERT INTO'
    assert Sql.delete() == 'DELETE FROM'
    assert Sql.where() == 'WHERE'
    assert Sql.values() == 'VALUES'
    assert Sql.new() == 'NEW'
    assert Sql.old() == 'OLD'
    assert Sql.end() == 'END;'

