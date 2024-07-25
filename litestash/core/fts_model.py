"""FTS Model

The Full-Text Search module defines the columns used by the FTS virtual table.
The Schema class and the setup_metadata utility function use the fts_model to
return valid data used in search results.
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
from litestash.core.config.schema_conf import ColumnConfig

   # key_hash: StrictStr
   # table_name: StrictStr
   # value: Json


@dataclass(slots=True)
class ValueSearchColumn:
    """Define the valid structure of the value column for fts virtual table.

    Attributes:
        name (str): The column name
        tuple_ (Literal[...]) : The SQLAlchemy type of the column.
    """
    name: StrictStr
    type_: Literal[StrType.literal, JsonType.literal] = Field(...)

    @field_validator(ColumnConfig.STASH_COLUMN.value)
    def valid_type(cls, column_type: ColumnType) -> Union[String,JSON]:
        """Valid Type Function

        Take a Literal and return sqlite column type.
        Args:
            column_type (ColumnType):
                A namedtuple for str or json types.
        """
        match column_type:
            case StrType.literal:
                return StrType.sqlite
            case JsonType.literal:
                return JsonType.sqlite
            case _:
                raise ValueError(ColumnConfig.ERROR.value)

    # key_hash: StrictStr
    # table_name: StrictStr
    # timestamp: StrictInt
    # microsecond: StrictInt


@dataclass(slots=True)
class TimeSearchColumn:
    """Define the valid structure of the time columns for fts virtual table.

    Attributes:
        name:
        tuple_: (Literal[...]) : The SQLAlchemy type of the column.
    """
    name: StrictStr
    type_: Literal[StrType.literal, IntType.literal] = Field(...)

    @field_validator(ColumnConfig.STASH_COLUMN.value)
    def valid_type(cls, column_type: ColumnType) -> Union[String,Integer]:
        """Valid Type Function

        Take a Literal and return sqlite column type.
        Args:
            column_type (ColumnType):
                A namedtuple for str or json types.
        """
        match column_type:
            case StrType.literal:
                return StrType.sqlite
            case IntType.literal:
                return IntType.sqlite
            case _:
                raise ValueError(ColumnConfig.ERROR.value)
