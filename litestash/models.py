"""LiteStash Data Models

This module defines the data models used by LiteStash for representing
key-value pairs and database column definitions.

Classes:
    LiteStashData: A data transfer object (DTO) for key-value pairs.
    LiteStashStore: Represents the structure of data stored in the database.
    StashColumn: Defines a column for a LiteStash database table.
"""
import orjson

from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String

from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_validator
from pydantic import Json
from pydantic import StrictBool
from pydantic import StrictInt
from pydantic import StrictFloat
from pydantic import StrictStr
from pydantic import ValidationError
from pydantic.dataclasses import dataclass

from litestash.core.config.litestash_conf import DataScheme
from litestash.core.util.misc_util import spaces_match
from litestash.core.util.model_util import ColumnType
from litestash.core.util.model_util import IntType
from litestash.core.util.model_util import JsonType
from litestash.core.util.model_util import StrType
from litestash.core.config.model import Parameter
from litestash.core.config.model import StashField
from litestash.core.config.model import StashDataclass
from litestash.core.config.schema_conf import ColumnConfig


@dataclass(slots=Parameter.SLOTS.value,
    config=ConfigDict(StashDataclass.CONFIG.value))
class LiteStashData:
    """Data Transfer Object (DTO) for key-value pairs.

    Attributes:
        key (str): A unique identifier for the value (alphanumeric and ASCII
        only).
        value (Json): The JSON data to be stored or retrieved.
    """
    key: StrictStr = Field(
        ...,
        min_length=DataScheme.MIN_LENGTH.value,
        max_length=DataScheme.MAX_LENGTH.value,
    )
    value: Optional[Union[
        Json | Dict | List | StrictBool | \
        StrictFloat | StrictInt | StrictStr | type(None) \
    ]] = Field(default=None)

    @field_validator(ColumnConfig.DATA_KEY.value)
    @classmethod
    def valid_key(cls, key: str):
        """Validate Key String

        Valid keys have only alphanumeric & ASCII characters
        Args:
            key (str): the name for the json being stashed
        """
        if not key.isascii():
            raise ValueError(StashField.VALID_KEY_ASCII.value)

        if spaces_match(key):
            raise ValueError(StashField.VALID_KEY_TEXT.value)

        return key

    @field_validator(ColumnConfig.DATA_VALUE.value, mode='before')
    @classmethod
    def valid_value(cls, value: Any):
        """Validate & serialize the value to JSON"""
        if isinstance(value, (dict,list,bool,str,int,float,type(None))):
            return orjson.dumps(value)
        else:
            raise ValueError(StashField.VALID_VALUE_JSON.value)


@dataclass(slots=Parameter.SLOTS.value,
    config=ConfigDict(StashDataclass.CONFIG.value))
class LiteStashStore:
    """Database model for key-value pairs.

    This class is used internally by the LiteStash manager and database
    interface.

    Attributes:
        key_hash (str):  Base64 URL-safe primary key.
        key (str):  The original key (unique and indexed).
        value (Json): The JSON data (optional).
        timestamp (int): POSIX timestamp.
        microsecond (int): Microseconds.
    """
    key_hash: StrictStr = Field(...)
    key: StrictStr = Field(...)
    value: Json | None = Field(default=None)
    timestamp: StrictInt | None = Field(default=None)
    microsecond: StrictInt | None = Field(default=None)


@dataclass(slots=Parameter.SLOTS.value,
    config=ConfigDict(StashDataclass.CONFIG.value))
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
    name: StrictStr
    type_: Literal[
        StrType.literal,
        IntType.literal,
        JsonType.literal
    ] = Field(...)
    primary_key: StrictBool = False
    index: StrictBool = False
    unique: StrictBool = False

    @field_validator(ColumnConfig.STASH_COLUMN.value)
    @classmethod
    def valid_type(cls, column_type: ColumnType) -> Union[String,Integer,JSON]:
        """Valid Type Function

        Take a Literal and return sqlite column type.
        Args:
            column_type (ColumnType):
                A namedtuple for str, int, or json types.
        """
        match column_type:
            case StrType.literal:
                return StrType.sqlite
            case IntType.literal:
                return IntType.sqlite
            case JsonType.literal:
                return JsonType.sqlite
            case _:
                raise ValueError(ColumnConfig.ERROR.value)
