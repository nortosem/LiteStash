import pytest
from litestash.core.config.misc_conf import Matches


def test_matches():
    assert 'LOG_ERROR' == Matches.LOG_ERROR.name
    assert 'TYPE_ERROR' == Matches.TYPE_ERROR.name
    assert 'Expected a string, but got incorrect type: ' == Matches.LOG_ERROR.value
    assert 'Value must be a string' == Matches.TYPE_ERROR.value
    assert Matches.log_error() == 'Expected a string, but got incorrect type: '
    assert Matches.type_error() == 'Value must be a string'
