"""The Models

The column and data models for keeping a stash.
"""
from litestash.core.config.litestash_conf import DataScheme
from litestash.core.config.schema_conf import ColumnConfig
from litestash.core.util.model_util import ColumnType
from litestash.core.util.model_util import BlobType
from litestash.core.util.model_util import IntegerType
from litestash.core.util.model_util import JsonType
from pydantic.dataclasses import dataclass
from pydantic import validator
from pydantic import StrictBytes
from pydantic import Json
from pydantic import Field
from typing import Literal
from typing import Union
from datetime import datetime
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import BLOB
import orjson


@dataclass(frozen=True, slots=True)
class LiteStashData:
    """The LiteStash Data

    This class defines a class of data for use with the LiteStash database.
    """
    key: StrictBytes = Field(
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
    """
    key_hash: StrictBytes = Field(..., primary_key=True, index=True)
    key: StrictBytes = Field(..., unique=True, index=True)
    value: Json | None = Field(default=None)
    time: datetime | None = Field(default=datetime.now())

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
    The DateTime is unix time int over now().
    """
    name: str
    type_: Literal[
        BlobType.literal,
        IntegerType.literal,
        JsonType.literal
    ] = Field(...)
    primary_key: bool = False
    index: bool = False
    unique: bool = False

    @validator(ColumnConfig.STASH_COLUMN.value)
    def valid_type(cls, column_type: ColumnType) -> Union[BLOB,Integer,JSON]:
        """Valid Type Function

        Take a Literal and return sqlite column type.

        Args:
            column_type (ColumnType):
                A namedtuple for blob, int, or json types.
        """
        match column_type:
            case BlobType.literal:
                return BlobType.sqlite
            case IntegerType.literal:
                return IntegerType.sqlite
            case JsonType.literal:
                return JsonType.sqlite
            case _:
                raise ValueError(ColumnConfig.ERROR.value)
