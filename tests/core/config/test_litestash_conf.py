import pytest
from litestash.core.config.litestash_conf import (
    DataScheme, StashSlots, Utils, EngineAttr, MetaAttr,
    SessionAttr, EngineConf
)

def test_data_scheme_values():
    assert DataScheme.TITLE.value == 'Data'
    assert DataScheme.DESCRIPTION.value == 'The key name and JSON data for the given key.'
    assert DataScheme.MIN_LENGTH.value == 4
    assert DataScheme.MAX_LENGTH.value == 41
    assert DataScheme.FORBID_EXTRA.value == 'forbid'

def test_stash_slots_values():
    assert StashSlots.ENGINE.value == 'engine'
    assert StashSlots.METADATA.value == 'metadata'
    assert StashSlots.DB_SESSION.value == 'db_session'

def test_utils_values():
    assert Utils.SIZE.value == 17
    assert Utils.DB_NAME_ERROR.value == 'Invalid character'

def test_engine_attr_values():
    assert EngineAttr.TYPE_NAME.value == 'EngineAttr'
    assert EngineAttr.DB_NAME.value == 'db_name'
    assert EngineAttr.ENGINE.value == 'engine'

def test_meta_attr_values():
    assert MetaAttr.TYPE_NAME.value == 'MetaAttr'
    assert MetaAttr.DB_NAME.value == 'db_name'
    assert MetaAttr.METADATA.value == 'metadata'

def test_session_attr_values():
    assert SessionAttr.TYPE_NAME.value == 'SessionAttr'
    assert SessionAttr.DB_NAME.value == 'db_name'
    assert SessionAttr.SESSION.value == 'session'
    assert SessionAttr.VALUE_ERROR.value == 'Invalid database: no tables found'

def test_engine_conf_values():
    assert EngineConf.SQLITE.value == 'sqlite:///'
    assert EngineConf.DIR_NAME.value == 'data'
    assert EngineConf.ECHO.value == True
    assert EngineConf.FUTURE.value == True
    assert EngineConf.NO_ECHO.value == False
    assert EngineConf.NO_FUTURE.value == False

def test_engine_conf_methods():
    assert EngineConf.sqlite() == 'sqlite:///'
    assert EngineConf.dirname() == 'data'
    assert EngineConf.echo() == True
    assert EngineConf.future() == True
    assert EngineConf.no_echo() == False
    assert EngineConf.no_future() == False

