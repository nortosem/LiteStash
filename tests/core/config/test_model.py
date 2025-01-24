import pytest
from tests.core.config.test_root import name_chk, value_chk
from litestash.core.config.model import Parameter, StashDataclass, StashField


def test_parameters():
    """Verifies the values of the Parameter enum members."""
    assert 'SLOTS' in name_chk(Parameter)
    assert 'FROM_ATTRIBUTES' in name_chk(Parameter)
    assert 'EXTRA' in name_chk(Parameter)
    assert True in value_chk(Parameter)
    assert 'from_attributes' in value_chk(Parameter)
    assert 'extra' in value_chk(Parameter)


def test_stashdataclass():
    """Verify the values of the StashDataclass enum."""
    assert StashDataclass.CONFIG.name == 'CONFIG'
    assert StashDataclass.CONFIG.value == (('from_attributes', False),
                                           ('extra', 'forbid'))


def test_stashfield():
    """Verify the values of the StashField enum."""
    assert 'VALID_KEY_ASCII' in name_chk(StashField)
    assert 'VALID_KEY_TEXT' in name_chk(StashField)
    assert 'VALID_VALUE_JSON' in name_chk(StashField)
    assert 'VALID_VALUE_TYPE' in name_chk(StashField)
    assert 'VALID_KEY_LENGTH' in name_chk(StashField)
    assert 'AT_MOST' in name_chk(StashField)
    assert 'AT_LEAST' in name_chk(StashField)
    assert 'Value error, ASCII keys only' in value_chk(StashField)
    assert 'Key text missing' in value_chk(StashField)
    assert 'JSON input should be string, bytes, or bytearray' in value_chk(StashField)
    assert 'Input should be a valid string' in value_chk(StashField)
    assert '1 validation error for' in value_chk(StashField)
    assert 'String should have at most 999 characters' in value_chk(StashField)
    assert 'String should have at least 3 characters' in value_chk(StashField)
