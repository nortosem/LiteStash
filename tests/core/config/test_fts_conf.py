import pytest
from litestash.core.config.root import Valid
from litestash.core.config.fts_conf import ViewSetup, SearchSetup, Trigger

def test_viewsetup_values():
    assert ViewSetup.CREATE.value == 'CREATE VIEW IF NOT EXISTS'
    assert ViewSetup.ALL_VALUES.value == 'all_values'

def test_viewsetup_create():
    assert ViewSetup.create() == 'CREATE VIEW IF NOT EXISTS'
    assert ViewSetup.all_values() == 'all_values'


def test_searchsetup_values():
    assert SearchSetup.CREATE.value == 'CREATE VIRTUAL TABLE IF NOT EXISTS'
    assert SearchSetup.USING.value == 'USING'
    assert SearchSetup.MATCH.value == 'MATCH'
    assert SearchSetup.ALL_VALUES.value == 'fts_all_values'
    assert SearchSetup.UNINDEXED.value == 'UNINDEXED'
    assert SearchSetup.DETAIL.value == 'detail=none'
    assert SearchSetup.INSERT.value == 'after_insert'
    assert SearchSetup.UPDATE.value == 'after_update'
    assert SearchSetup.DELETE.value == 'after_delete'
    assert SearchSetup.SQLITE_DIALECT.value == 'sqlite'


def test_searchsetup_methods():
    assert SearchSetup.table_name() == 'fts_all_values'
    assert SearchSetup.create() == 'CREATE VIRTUAL TABLE IF NOT EXISTS'
    assert SearchSetup.using() == 'USING'
    assert SearchSetup.match() == 'MATCH'
    assert SearchSetup.unindexed() == 'UNINDEXED'
    assert SearchSetup.detail() == 'detail=none'
    assert SearchSetup.insert() == 'after_insert'
    assert SearchSetup.update() == 'after_update'
    assert SearchSetup.delete() == 'after_delete'
    assert SearchSetup.sqlite_dialect() == 'sqlite'

def test_trigger_values():
    assert Trigger.CREATE.value == 'CREATE TRIGGER IF NOT EXISTS'
    assert Trigger.AFTER_INSERT.value == 'AFTER INSERT ON'
    assert Trigger.NAME_INSERT.value == '_insert_trigger'
    assert Trigger.AFTER_UPDATE.value == 'AFTER UPDATE ON'
    assert Trigger.NAME_UPDATE.value == '_update_trigger'
    assert Trigger.AFTER_DELETE.value == 'AFTER DELETE ON'
    assert Trigger.NAME_DELETE.value == '_delete_trigger'

def test_trigger_methods():
    """
    Tests each staticmethod in Trigger and ColumnFields for proper fstring usage.
    """
    assert Trigger.create() == 'CREATE TRIGGER IF NOT EXISTS'
    assert Trigger.after_insert() == 'AFTER INSERT ON'
    assert Trigger.name_insert() == '_insert_trigger'
    assert Trigger.after_update() == 'AFTER UPDATE ON'
    assert Trigger.name_update() == '_update_trigger'
    assert Trigger.after_delete() == 'AFTER DELETE ON'
    assert Trigger.name_delete() == '_delete_trigger'
