import pytest
from tests.core.config.test_root import member_chk
from litestash.core.config.model import StashDataConf


def test_stash_data_conf_values():
    """Verifies the values of the StashDataConf enum members."""
    assert StashDataConf.ORM_MODE.value == "orm_mode"
    assert StashDataConf.EXTRA.value == "extra"
    assert StashDataConf.JSON_LOADS.value == "json_loads"
    assert StashDataConf.JSON_DUMPS.value == "json_dumps"

def test_stash_data_conf_membership():
    """Verifies the membership of values in the StashDataConf enum."""
    assert "orm_mode" in member_chk(StashDataConf)
    assert "extra" in member_chk(StashDataConf)
    assert "json_loads" in member_chk(StashDataConf)
    assert "json_dumps" in member_chk(StashDataConf)

