"""LiteStash Schema Configuration

Provides configuration for defining the structure of the LiteStash database
schema.

This module includes the following configuration elements:

- **`Pragma`:**  SQLite PRAGMA statements for database setup and optimization.
- **`ColumnSetup`:**  Column names used in the LiteStash tables.
- **`ColumnConfig`:** Configuration for mapping column types and validating
column definitions.
- **`Names`:**  Enum for common table and database suffixes used in naming
conventions.
"""

from litestash.core.config.root import Valid

class Pragma(Valid):
    """Sqlite Pragma

    The default pragma configuration.
    """
    CONNECT = 'connect'
    PRAGMA = 'PRAGMA'
    JOURNAL_MODE = 'journal_mode=WAL;'
    SYNCHRONOUS = 'synchronous=NORMAL;'
    FOREIGN_KEYS = 'foreign_keys=ON;'
    JSON = 'json_valid = 1;'
    BEGIN = 'BEGIN'

    @staticmethod
    def journal_mode() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.JOURNAL_MODE.value}'

    @staticmethod
    def synchronous() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.SYNCHRONOUS.value}'

    @staticmethod
    def foreign_keys() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.FOREIGN_KEYS.value}'

    @staticmethod
    def valid_json() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.JSON.value}'


class Sql(Valid):
    """SQL Terms

    Enumerations of regularly used SQL terms.
    Members:
        BEGIN:
        INSERT:
        DELETE:
        AND:
        WHERE:
        VALUES:
        NEW:
        OLD:
        END:
    """
    BEGIN = 'BEGIN'
    INSERT = 'INSERT INTO'
    DELETE = 'DELETE FROM'
    AND = 'AND'
    WHERE = 'WHERE'
    VALUES = 'VALUES'
    NEW = 'NEW'
    OLD = 'OLD'
    END = 'END;'

    @staticmethod
    def begin():
        return f'{Sql.BEGIN.value}'

    @staticmethod
    def insert():
        return f'{Sql.INSERT.value}'

    @staticmethod
    def delete():
        return f'{Sql.DELETE.value}'

    @staticmethod
    def where():
        return f'{Sql.WHERE.value}'

    @staticmethod
    def values():
        return f'{Sql.VALUES}'

    @staticmethod
    def new():
        return f'{Sql.NEW.value}'

    @staticmethod
    def old():
        return f'{Sql.OLD.value}'

    @staticmethod
    def end():
        return f'{Sql.END.value}'


class ColumnSetup(Valid):
    """The Column Setup

    Define the column attributes for each table
    """
    HASH = 'key_hash'
    KEY = 'key'
    VALUE = 'value'
    TIMESTAMP = 'timestamp'
    MICROSECOND = 'microsecond'
    TABLE_NAME = 'table_name'

    @staticmethod
    def hash():
        return f'{ColumnSetup.HASH.value}'

    @staticmethod
    def key():
        return f'{ColumnSetup.KEY.value}'

    @staticmethod
    def value():
        return f'{ColumnSetup.VALUE.value}'

    @staticmethod
    def timestamp():
        return f'{ColumnSetup.TIMESTAMP.value}'

    @staticmethod
    def microsecond():
        return f'{ColumnSetup.MICROSECOND.value}'

    @staticmethod
    def table_name():
        return f'{ColumnSetup.TABLE_NAME.value}'

class ColumnConfig(Valid):
    """The namedtuple Column config

    A config for mapping literal type string to sqlite database type.
    """
    TYPE_NAME = 'ColumnTypes'
    TYPE_STR = 'literal'
    TYPE_DB = 'sqlite'
    STR = 'String'
    INT = 'Integer'
    JSON = 'JSON'
    STASH_COLUMN = 'type_'
    DATA_KEY = 'key'
    DATA_VALUE = 'value'
    DOC = 'todo'
    ERROR = 'Value must be a valid column type'

class Names(Valid):
    """Various Names

    Also the Table name suffix as HASH
    """
    HYPHEN = 'hyphen'
    UNDER = 'underscore'
    HASH = '_hash_'
    LOW = '_lower'
    UP = '_upper'
    DB = '.db'
    ERROR = 'Invalid character request'
