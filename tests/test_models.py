import pytest
import orjson
import re
from sqlalchemy import JSON, String, Integer
from litestash.models import LiteStashData, LiteStashStore, StashColumn, ColumnType, StrType, IntType, JsonType
from litestash.core.config.schema_conf import ColumnConfig
from litestash.core.config.litestash_conf import DataScheme
from litestash.core.config.model import StashField
from litestash.core.util.model_util import ColumnType
from litestash.core.util.model_util import IntType
from litestash.core.util.model_util import JsonType
from litestash.core.util.model_util import StrType
from pydantic import ValidationError
from sqlalchemy import Column
from sqlalchemy import Integer as sqlInteger
from sqlalchemy import String as sqlString
from sqlalchemy import JSON as sqlJSON

@pytest.fixture(params=[chr(code)*3 for code in range(0x0142, 0x0148)])
def invalid_ascii_key(request):
    """The latin range beyond ASCII"""
    return request.param


@pytest.fixture(params=[chr(code)*3 for code in range(0x4E42, 0x4E48)])
def invalid_cjk_key(request):
    """The CJK characters"""
    return request.param


@pytest.fixture(params=[chr(code)*3 for code in range(0x1F642, 0x1F648)])
def invalid_emoji_key(request):
    """The smiley emoji characters"""
    return request.param


@pytest.fixture(params=[
        '   ',
        '   '*30,
        '   '*333
    ])
def empty_key(request):
    """The empty spaces"""
    return request.param


@pytest.fixture(params=[
    '4',
    '42',
    'XxX'*334,
])
def invalid_key_length(request):
    """Invalid key size"""
    return request.param


@pytest.fixture(params=[
    420,
    4.2,
    True,
    ('tuple', 'key'),
    {'set'}
])
def invalid_key_type(request):
    """Invalid key types"""
    return request.param


@pytest.fixture(params=[
    complex(4, 2),
    lambda x: x,
    bytearray('not json str'.encode()),
    bytes('not a json'.encode()),
    object()
])
def invalid_value(request):
    """Invalid json values"""
    return request.param


@pytest.fixture(params=[
    'key',
    'key_under',
    'keyCamel',
    'max'*333,
    '123345',
])
def valid_key(request):
    """Valid ASCII keys. String only."""
    return request.param


@pytest.fixture(params=[
    'valid_str_value',
    {'valid_dict_str': 'value'},
    {'valid_dict_int': 0},
    {'valid_dict_float': 4.2},
    {'valid_dict_bool': True},
    {'valid_dict_list': ['1',
                         2,
                         False,
                         'four',
                         {'list_dict': True},
                         ['list_list', ['a','inner', 'list']]
                         ]},
    ['valid', 'list', 'str_value'],
    ['valid', 'list', 'int_value', 42],
    ['valid', 'list', 'float_value', 4.2],
    ['valid', 'list', 'bool_value', False],
    ['valid', 'list_list_value', ['a', 42, 4.2, True]],
    ['valid', 'list_dict_value', {'dict_list': 42}]
])
def valid_value(request):
    """Valid data value fixture"""
    return request.param


def test_lsd_data_validation(valid_key, valid_value):
    """Test enumerations of valid keys and values"""
    data  = LiteStashData(key=valid_key, value=valid_value)
    assert data.key == valid_key
    assert data.value == valid_value


def test_lsd_invalid_key_length(invalid_key_length):
    """Test enumeration of invalid key lengths"""
    with pytest.raises(ValidationError) as error_info:
        LiteStashData(key=invalid_key_length)
    if len(invalid_key_length) < DataScheme.MIN_LENGTH.value:
        assert StashField.AT_LEAST.value in str(error_info.value)

    if len(invalid_key_length) > DataScheme.MAX_LENGTH.value:
        print('max_lenght: ', str(error_info.value))
        assert StashField.AT_MOST.value in str(error_info.value)


def test_lsd_invalid_key_type(invalid_key_type):
    """Test enumeration of invalid key types"""
    with pytest.raises(ValidationError) as error_info:
        LiteStashData(key=invalid_key_type)
    assert StashField.VALID_VALUE_TYPE.value in str(error_info.value)


def test_lsd_invalid_key_content(
    invalid_ascii_key,
    invalid_cjk_key,
    invalid_emoji_key,
    empty_key):
    """Test for non-ASCII key content"""
    with pytest.raises(ValueError) as error_info:
        LiteStashData(key=invalid_ascii_key)
    assert StashField.VALID_KEY_ASCII.value in str(error_info)

    with pytest.raises(ValueError) as error_info:
        LiteStashData(key=invalid_cjk_key)
    assert StashField.VALID_KEY_ASCII.value in str(error_info.value)

    with pytest.raises(ValueError) as error_info:
        LiteStashData(key=invalid_emoji_key)
    assert StashField.VALID_KEY_ASCII.value in str(error_info.value)

    with pytest.raises(ValueError) as error_info:
        LiteStashData(key=empty_key)
    assert StashField.VALID_KEY_TEXT.value in str(error_info.value)


def test_lsd_invalid_value(invalid_value):
    """Test enumeration of invalid value content"""
    possible_errors = ["Invalid JSON",
                        "Value must be JSON serializable",
                        "JSON input should be string"]
    with pytest.raises(ValueError) as error_info:
        lsd = LiteStashData(key='key', value=invalid_value)
    assert any(error in str(error_info.value) for error in possible_errors)


@pytest.fixture
def valid_datastore():
    data = {
        "key_hash":"test_hash",
        "key": "test_key",
        "value": '{"data": "test_value"}',
        "timestamp": 1678886400,
        "microsecond": 123456
    }
    return data


def test__valid_data(valid_datastore):
    """Test with valid data."""
    store = LiteStashStore(**valid_datastore)

    assert store.key_hash == "test_hash"
    assert store.key == "test_key"
    assert store.value == {"data": "test_value"}
    assert store.timestamp == 1678886400
    assert store.microsecond == 123456


@pytest.mark.parametrize("field, invalid", [
    ("key_hash", 123),
    ("key", 123),
    ("value", ('a', 'set')),
    ("timestamp", "not an int"),
    ("microsecond", "not an int"),
])
def test_invalid_fields_types(valid_datastore, field, invalid):
    """Test invalid data types for each field."""
    data = valid_datastore
    data[field] = invalid

    with pytest.raises(ValidationError) as error_info:
        LiteStashStore(**data)
    assert field in str(error_info)


@pytest.mark.parametrize("field", [
    'key_hash',
    'key',
    'value',
    'timestamp',
    'microsecond'
])
def test_missing_fields(valid_datastore, field):
    """Test missing fields, both required and defaults."""
    data = valid_datastore
    data.pop(field)
    if field == 'key_hash' or field == 'key':
        with pytest.raises(ValidationError) as error_info:
            store = LiteStashStore(**data)

        assert "Field required" in str(error_info.value)
    else:
        store = LiteStashStore(**data)
        assert getattr(store, field) == None


@pytest.mark.parametrize("column_type, expected_type", [
    (StrType.literal, StrType.sqlite),
    (IntType.literal, IntType.sqlite),
    (JsonType.literal, JsonType.sqlite),
])
def test_valid_column_types(column_type, expected_type):
    """Test all valid column types are mapped to their SQLAlchemy type."""
    column = StashColumn(name="test", type_=column_type)
    assert column.type_ == expected_type


@pytest.mark.parametrize("invalid_type", [
    "not_a_type",
    123,
    None,
    [StrType.literal],
])
def test_invalid_column_types(invalid_type):
    """Test invalid type raises"""
    with pytest.raises(ValueError) as exc_info:
        StashColumn(name="test", type_=invalid_type)
    assert ColumnConfig.ERROR.value in str(exc_info.value)


def test_all_conditions():
    """Test all conditions in the match statement."""
    str_column = StashColumn(name="str_col", type_=StrType.literal)
    assert str_column.type_ == sqlString
    str_column.type_ = IntType.sqlite
    assert str_column.type_ == sqlInteger

    int_column = StashColumn(name="int_col", type_=IntType.literal)
    assert int_column.type_ == sqlInteger
    int_column.type_ = JsonType.sqlite
    assert int_column.type_ == sqlJSON

    json_column = StashColumn(name="json_col", type_=JsonType.literal)
    assert json_column.type_ == sqlJSON
    json_column.type_ = StrType.sqlite
    assert json_column.type_ == sqlString

    with pytest.raises(ValueError) as exc_info:
        StashColumn(name="invalid_col", type_=set(['set']))
    assert ColumnConfig.ERROR.value in str(exc_info.value)


def test_default_booleans():
    """Ensure default boolean values are set correctly."""
    column = StashColumn(name="test_col", type_=StrType.literal)
    assert column.primary_key is False
    assert column.index is False
    assert column.unique is False

@pytest.mark.parametrize("bool_values", [
    (True, True, True),
    (False, False, False),
    (True, False, True),
    (False, True, False)
])
def test_boolean_combinations(bool_values):
    """Test all boolean combinations for primary_key, index, and unique."""
    primary_key, index, unique = bool_values
    column = StashColumn(name="test_col", type_=StrType.literal,
                         primary_key=primary_key, index=index, unique=unique)
    assert column.primary_key == primary_key
    assert column.index == index
    assert column.unique == unique


def test_stash_column():
    with pytest.raises(ValidationError) as error_info:
        sc = StashColumn(name="test_column")
    assert 'Field required' in str(error_info.value)


def test_dynamic_type_change():
    """Test changing type dynamically after initialization."""
    column = StashColumn(name="test", type_=StrType.literal)
    assert column.type_ == sqlString

    column.type_ = set("not_a_literal")
    with pytest.raises(ValueError) as error_info:
        column.valid_type(column.type_)
    assert ColumnConfig.ERROR.value in str(error_info.value)

def test_pydantic_validation():
    """Ensure Pydantic catches invalid types before they reach the validator."""
    with pytest.raises(ValidationError) as error_info:
        StashColumn(name="test", type_=set("not_a_literal"))
