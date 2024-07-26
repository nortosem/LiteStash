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


class ViewSetup(Valid):
    """The View Setup

    Enumerates the SQL used for creating a full table view in each database.

    Members:
        CREATE: the create sql statement (if not exists is the default)
        AS: the SQL 'as' term
        ALL_VALUES: the name of the view of all table values in each database
    """
    CREATE = 'CREATE VIEW IF NOT EXISTS'
    ALL_VALUES = 'all_values'

    @staticmethod
    def create():
        return f'{ViewSetup.CREATE.value}'


    @staticmethod
    def all_values():
        return f'{ViewSetup.ALL_VALUES.value}'

class SearchSetup(Valid):
    """FTS Setup

    Enumerations for setup of the FTS5 search table.

    Members:
        CREATE:
        USING:
        ALL_VALUES:
        UNINDEXED:
        DETAIL:
        INSERT:
        UPDATE:
        DELETE:
        SQLITE_DIALECT:
    """
    CREATE = 'CREATE VIRTUAL TABLE IF NOT EXISTS'
    USING = 'USING'
    ALL_VALUES = 'fts_all_values'
    UNINDEXED = 'UNINDEXED'
    DETAIL = 'detail=none'
    INSERT = 'after_insert'
    UPDATE = 'after_update'
    DELETE = 'after_delete'
    SQLITE_DIALECT = 'sqlite'

    @staticmethod
    def table_name():
        return f'{SearchSetup.ALL_VALUES.value}'

    @staticmethod
    def create():
        return f'{SearchSetup.CREATE.value}'

    @staticmethod
    def using():
        return f'{SearchSetup.USING.value}'

    @staticmethod
    def unindexed():
        return f'{SearchSetup.UNINDEXED.value}'

    @staticmethod
    def detail():
        return f'{SearchSetup.DETAIL.value}'

    @staticmethod
    def insert():
        return f'{SearchSetup.INSERT.value}'

    @staticmethod
    def update():
        return f'{SearchSetup.UPDATE.value}'

    @staticmethod
    def delete():
        return f'{SearchSetup.DELETE.value}'

    @staticmethod
    def sqlite_dialect():
        return f'{SearchSetup.SQLITE_DIALECT.value}'


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


class Trigger(Valid):
    """Trigger SQL

    The SQL components for DDL triggers in sqlite.

    Members:
        CREATE:
        AFTER_INSERT:
        NAME_INSERT:
        AFTER_UPDATE:
        NAME_UPDATE:
        AFTER_DELETE:
        NAME_DELETE:
    """
    CREATE = 'CREATE TRIGGER IF NOT EXISTS'
    AFTER_INSERT = 'AFTER INSERT ON'
    NAME_INSERT = '_insert_trigger'
    AFTER_UPDATE = 'AFTER UPDATE ON'
    NAME_UPDATE = '_update_trigger'
    AFTER_DELETE = 'AFTER DELETE ON'
    NAME_DELETE = '_delete_trigger'

    @staticmethod
    def create():
        return f'{Trigger.CREATE.value}'

    @staticmethod
    def after_insert():
        return f'{Trigger.AFTER_INSERT.value}'

    @staticmethod
    def name_insert():
        return f'{Trigger.NAME_INSERT.value}'

    @staticmethod
    def after_update():
        return f'{Trigger.AFTER_UPDATE.value}'

    @staticmethod
    def name_update():
        return f'{Trigger.NAME_UPDATE.value}'

    @staticmethod
    def after_delete():
        return f'{Trigger.AFTER_DELETE.value}'

    @staticmethod
    def name_delete():
        return f'{Trigger.NAME_DELETE.value}'


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
