import pytest
from litestash.core.config.root import (
    Main, Core, Util, Config, Tables
)

def test_main_enum_values():
    assert Main.CORE.value == 'core'
    assert Main.DATA.value == 'LiteStashData'
    assert Main.STORE.value == 'LiteStashStore'
    assert Main.STASH.value == 'LiteStash'


def member_chk(E):
    for member in E.__members__:
        yield E.__members__[member].value


def test_main_enum_membership():
    assert 'core' in member_chk(Main)
    assert 'LiteStashData' in member_chk(Main)
    assert 'LiteStashStore' in member_chk(Main)
    assert 'LiteStash' in member_chk(Main)

def test_core_enum_values():
    assert Core.CONFIG.value == 'config'
    assert Core.UTIL.value == 'util'
    assert Core.ENGINE.value == 'engine'
    assert Core.SCHEMA.value == 'schema'
    assert Core.SESSION.value == 'session'

def test_core_enum_membership():
    assert 'config' in member_chk(Core)
    assert 'util' in member_chk(Core)
    assert 'engine' in member_chk(Core)
    assert 'schema' in member_chk(Core)
    assert 'session' in member_chk(Core)


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
