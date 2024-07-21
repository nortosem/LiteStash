import pytest
from tests.core.config.test_root import member_chk
from litestash.core.config.model import StashConf


def test_stash_data_conf_values():
    """Verifies the values of the StashDataConf enum members."""
    assert StashConf.ORM_MODE.value == "orm_mode"
    assert StashConf.EXTRA.value == "extra"
    assert StashConf.JSON_LOADS.value == "json_loads"
    assert StashConf.JSON_DUMPS.value == "json_dumps"

def test_stash_data_conf_membership():
    """Verifies the membership of values in the StashDataConf enum."""
    assert "orm_mode" in member_chk(StashConf)
    assert "extra" in member_chk(StashConf)
    assert "json_loads" in member_chk(StashConf)
    assert "json_dumps" in member_chk(StashConf)

