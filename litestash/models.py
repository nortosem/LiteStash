"""LiteStash Data Models

This module defines the data models used by LiteStash for representing
key-value pairs and database column definitions.

Classes:
    LiteStashData: A data transfer object (DTO) for key-value pairs.
    LiteStashStore: Represents the structure of data stored in the database.
    StashColumn: Defines a column for a LiteStash database table.
"""
import orjson
from typing import Union
from typing import Literal
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy import Integer
from pydantic import Json
from pydantic import Field
from pydantic import StrictStr
from pydantic import StrictInt
from pydantic import field_validator
from pydantic.dataclasses import dataclass
from litestash.core.util.model_util import StrType
from litestash.core.util.model_util import IntType
from litestash.core.util.model_util import JsonType
from litestash.core.util.model_util import ColumnType
from litestash.core.config.model import StashConf
from litestash.core.config.schema_conf import ColumnConfig
from litestash.core.config.litestash_conf import DataScheme

@dataclass(slots=True)
class LiteStashData:
    """Data Transfer Object (DTO) for key-value pairs.

    Attributes:
        key (str): A unique identifier for the value (alphanumeric and ASCII
        only).
        value (Json): The JSON data to be stored or retrieved.
    """
    model_config = {
        StashConf.ORM_MODE.value: False,
        StashConf.EXTRA.value: DataScheme.FORBID_EXTRA.value,
        StashConf.JSON_LOADS.value: orjson.loads,
        StashConf.JSON_DUMPS.value: orjson.dumps
    }

    key: StrictStr = Field(
        ...,
        min_length=DataScheme.MIN_LENGTH.value,
        max_length=DataScheme.MAX_LENGTH.value,
    )
    value: Json | None = Field(default=None)

    @field_validator(ColumnConfig.DATA_KEY.value)
    def valid_key(cls, key: str):
        """Validate Key String

        Valid keys have only alphanumeric & ASCII characters
        Args:
            key (str): the name for the json being stashed
        """
        if not key.isascii():
            raise ValueError('ascii')
        return key


    @field_validator(ColumnConfig.DATA_VALUE.value)
    def valid_value(cls, value):
        """Validate & serialize the value to JSON"""
        if not isinstance(value, (dict,list,str,type(None))):
            raise TypeError('no')

        if isinstance(value, (dict,list)):
            value = orjson.dumps(value).decode()

        return value


@dataclass(slots=True)
class LiteStashStore:
    """Database model for key-value pairs.

    This class is used internally by the LiteStash manager and database
    interface.

    Attributes:
        key_hash (str):  Base64 URL-safe primary key.
        key (str):  The original key (unique and indexed).
        value (Json): The JSON data (optional).
        date_time (int): POSIX timestamp.
        ms_time (int): Microseconds.
    """
    key_hash: StrictStr = Field(...)
    key: StrictStr = Field(...)
    value: Json | None = Field(default=None)
    timestamp: StrictInt | None = Field(default=None)
    microsecond: StrictInt | None = Field(default=None)


@dataclass(slots=True)
class StashColumn:
    """Defines the structure of a column in a LiteStash database table.

    Attributes:
        name (str): The column name.
        type_ (Literal[...]) : The SQLAlchemy type of the column.
        primary_key (bool): Whether the column is a primary key
        (default: False).
        index (bool): Whether to create an index on the column
        (default: False).
        unique (bool): Whether the column has a unique constraint
        (default: False).
    """
    name: str
    type_: Literal[
        StrType.literal,
        IntType.literal,
        JsonType.literal
    ] = Field(...)
    primary_key: bool = False
    index: bool = False
    unique: bool = False

    @field_validator(ColumnConfig.STASH_COLUMN.value)
    def valid_type(cls, column_type: ColumnType) -> Union[String,Integer,JSON]:
        """Valid Type Function

        Take a Literal and return sqlite column type.
        Args:
            column_type (ColumnType):
                A namedtuple for str, float, or json types.
        """
        match column_type:
            case StrType.literal:
                return StrType.sqlite
            case IntType.literal:
                return StrType.sqlite
            case JsonType.literal:
                return JsonType.sqlite
            case _:
                raise ValueError(ColumnConfig.ERROR.value)
