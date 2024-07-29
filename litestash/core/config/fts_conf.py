"""LiteStash FTS Configuration

Define the configuration for the Full-text search on LiteStash data.
"""
from litestash.core.config.root import Valid

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
    MATCH = 'MATCH'
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
    def match():
        return f'{SearchSetup.MATCH.value}'

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
