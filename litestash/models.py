"""The Models

The column and data models for keeping a stash.
"""
from litestash.core.config.litestash_conf import DataScheme
from litestash.core.config.schema_conf import ColumnConfig
from litestash.core.util.model_util import ColumnType
from litestash.core.util.model_util import StrType
from litestash.core.util.model_util import IntType
from litestash.core.util.model_util import JsonType
from pydantic.dataclasses import dataclass
from pydantic import validator
from pydantic import StrictStr
from pydantic import StrictInt
from pydantic import Json
from pydantic import Field
from typing import Literal
from typing import Union
from datetime import datetime
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String
import orjson


@dataclass(frozen=True, slots=True)
class LiteStashData:
    """The LiteStash Data

    This class defines a class of data for use with the LiteStash database.
    Args:
        key (str): A text label for some json data
        value (json): A text string composed of json data
    """
    key: StrictStr = Field(
        ...,
        min_length=DataScheme.MIN_LENGTH.value,
        max_length=DataScheme.MAX_LENGTH.value,
    )
    value: Json | None = Field(default=None)

    class Config:
        """Define data config attributes"""
        orm_mode = False
        extra = f'{DataScheme.FORBID_EXTRA.value}'
        json_loads = orjson.loads
        json_dumps = orjson.dumps

@dataclass(slots=True)
class LiteStashStore:
    """LiteStash Database Fields

    The database storage class.  Defines all columns and column types in db.
    Only used by the Stash Manager and the database interface.
    Args:
        key_hash (StrictStr): The base64 urlsafe primary key
        key_digest (StrictStr): A unique string that identifies a key
        lot (StrictStr): A unique string id alloted to the storage object
        key (StrictStr): The text name label for the json data
        value (Json): The json data being stashed
        date_time (StrictInt): Y,M,D,H,M,S as POSIX datetime integer
        ms_time (StrictInt): The microseconds floated from datetime source
    """
    key_hash: StrictStr = Field(..., primary_key=True, index=True)
    key_digest: StrictStr = Field(..., unique=True, index=True)
    lot: StrictStr = Field(..., unique=True, index=True)
    key: StrictStr = Field(..., unique=True, index=True)
    value: Json | None = Field(default=None)
    date_time: StrictInt | None = Field(default=None)
    ms_time: StrictInt | None = Field(default=None)

    class Config:
        """LiteStashStore Config"""
        orm_mode = True
        extra = f'{DataScheme.FORBID_EXTRA.value}'
        json_loads = orjson.loads
        json_dumps = orjson.dumps


@dataclass(slots=True)
class StashColumn:
    """Valid LiteStash Column

    Definition for sqlite database columns.
    Args:
        name (str): The name for a column
        type_ (Literal[str,float,json]):
            Only permit Text, Float, or Json types for any column
        primary_key (bool): Label as partcipating in rowid for a row of data
        index (bool): Create an index if True
        unique (bool): Mark some column unique
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

    @validator(ColumnConfig.STASH_COLUMN.value)
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
