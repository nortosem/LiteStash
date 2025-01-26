import pytest
from litestash.core.config.connection_conf import (
    TimeAttr, GetConnectionAttr, SetConnectionAttr, ConnectionType
)


def test_timeattr():
    assert 'TYPE_NAME' == TimeAttr.TYPE_NAME.name
    assert 'TIMESTAMP' == TimeAttr.TIMESTAMP.name
    assert 'MICROSECOND' == TimeAttr.MICROSECOND.name
    assert 'VALUE_ERROR' == TimeAttr.VALUE_ERROR.name
    assert 'DOC' == TimeAttr.DOC.name
    assert 'GetTime' == TimeAttr.TYPE_NAME.value
    assert 'timestamp' == TimeAttr.TIMESTAMP.value
    assert 'microsecond' == TimeAttr.MICROSECOND.value
    assert 'Valid time in integer only' == TimeAttr.VALUE_ERROR.value
    assert '''Defines a namedtuple for datetime.now() value.
    Attributes:
        timestamp (int): unix timestamp attribute of a datetime instance
        microsecond (int): microsecone attribute of datetime instance
    ''' == TimeAttr.DOC.value


def test_getconnectionattr():
    assert 'TYPE_NAME' == GetConnectionAttr.TYPE_NAME.name
    assert 'HASH_KEY' == GetConnectionAttr.HASH_KEY.name
    assert 'TABLE' == GetConnectionAttr.TABLE.name
    assert 'SESSION' == GetConnectionAttr.SESSION.name
    assert 'DOC' == GetConnectionAttr.DOC.name
    assert 'Connection' == GetConnectionAttr.TYPE_NAME.value
    assert 'hash_key' == GetConnectionAttr.HASH_KEY.value
    assert 'table' == GetConnectionAttr.TABLE.value
    assert 'session' == GetConnectionAttr.SESSION.value
    assert '''
    TODO
    ''' == GetConnectionAttr.DOC.value


def test_setconnectionattr():
    assert 'TYPE_NAME' == SetConnectionAttr.TYPE_NAME.name
    assert 'DATA_STORE' == SetConnectionAttr.DATA_STORE.name
    assert 'TABLE' == SetConnectionAttr.TABLE.name
    assert 'SESSION' == SetConnectionAttr.SESSION.name
    assert 'DOC' == SetConnectionAttr.DOC.name
    assert 'Connection' == SetConnectionAttr.TYPE_NAME.value
    assert 'data' == SetConnectionAttr.DATA_STORE.value
    assert 'table' == SetConnectionAttr.TABLE.value
    assert 'session' == SetConnectionAttr.SESSION.value
    assert '''
    TODO
    ''' == SetConnectionAttr.DOC.value

def test_connectiontype():
    assert 'GET' == ConnectionType.GET.name
    assert 'SET' == ConnectionType.SET.name
    assert 'get' == ConnectionType.GET.value
    assert 'set' == ConnectionType.SET.value
