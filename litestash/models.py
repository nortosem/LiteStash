"""The Models

The column and data models for keeping a stash.
"""
from litestash.core.config.litestash import DataScheme
from litestash.core.util.table import valid_type
from litestash.core.util.table import BlobType
from litestash.core.util.table import IntegerType
from litestash.core.util.table import JsonType
from pydantic.dataclasses import dataclass
from pydantic import StrictBytes
from pydantic import Json
from pydantic import Field
from typing import Literal
from datetime import datetime
from sqlalchemy.schema import Column
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
    type_: Literal[BlobType.literal, IntegerType.literal, JsonType.literal]
    primary_key: bool = False
    index: bool = False
    unique: bool = False

    def get_column(self) -> Column:
        """Create columns for database tables"""
        column_type = valid_type(self.type_)
        return Column(
            self.name,
            column_type,
            primary_key=self.primary_key,
            index=self.index,
            unique=self.unique,
            nullable=self.nullable
        )
