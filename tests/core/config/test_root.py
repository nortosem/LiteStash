import pytest
from litestash.core.config.root import (
    Main, Core, Util, Config, Tables
)

def test_main_enum_values():
    assert Main.CORE.value == 'core'
    assert Main.DATA.value == 'LiteStashData'
    assert Main.STORE.value == 'LiteStashStore'
    assert Main.STASH.value == 'LiteStash'


def name_chk(E):
    for member in E.__members__.keys():
        yield member


def value_chk(E):
    for member in E.__members__:
        yield E.__members__[member].value


def test_main_enum_membership():
    assert 'core' in value_chk(Main)
    assert 'LiteStashData' in value_chk(Main)
    assert 'LiteStashStore' in value_chk(Main)
    assert 'LiteStash' in value_chk(Main)

def test_core_enum_values():
    assert Core.CONFIG.value == 'config'
    assert Core.UTIL.value == 'util'
    assert Core.ENGINE.value == 'engine'
    assert Core.SCHEMA.value == 'schema'
    assert Core.SESSION.value == 'session'

def test_core_enum_membership():
    assert 'config' in value_chk(Core)
    assert 'util' in value_chk(Core)
    assert 'engine' in value_chk(Core)
    assert 'schema' in value_chk(Core)
    assert 'session' in value_chk(Core)


def test_util_enum_values():
    pass

def test_util_enum_membership():
    pass

def test_config_enum_values():
    pass

def test_config_enum_membership():
    pass

def test_tables_enum_values():
    pass

def test_tables_enum_membership():
    pass
