"""The Models

The base and table models for a stash.
"""
from typing import Literal
from datetime import datetime
from pydantic import Json
from pydantic import StrictStr
from pydantic import StrictInt
from pydantic import Field
from pydantic.dataclasses import dataclass
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import JSON
from sqlalchemy.schema import Column
from sqlalchemy.schema import Table
from typing import Literal


@dataclass(slots=True)
class LiteStashData:
    """The LiteStash Data

    This class defines a class of data for use with the LiteStash database.
    """
    key: StrictStr
    value: Json


@dataclass(slots=True)
class LiteStashStore(LiteStashData):
    """LiteStash Database Fields

    The database storage class.  Defines all columns and column types in db.
    Only used by the Stash Manager and the database interface.
    """
    hash_key: StrictStr | None = Field(default=None, unique=True, index=True)
    key: StrictStr = Field(default=None, unique=True, index=True)
    value: JSON = Field(default=None)
    date_created: datetime | None = Field(default=datetime.now())


@dataclass(slots=True)
class StashColumns:
    """Valid LiteStash Column

    Definition for sqlite database columns.
    The DateTime is unix time int over now().
    TODO
    """
    name: str
    type_: Literal[Text,Integer,JSON]
    primary_key: bool = False
    index: bool = False
    unique: bool = False
    nullable: bool = False

    def get_column(self) -> Column:
        """Create columns for database tables"""
        return Column(
            self.name,
            self.type_,
            primary_key=self.primary_key,
            index=self.index,
            unique=self.unique,
            nullable=self.nullable
        )

@dataclass(slots=True)
class StashTables:
    """A LiteStash Table Definition

    Create and return a valid Table for the LiteStash Db.
    """
    name: str
    metadata: Metadata
    columns: list[StashColumns]

    def get_table(self) -> Table:
        """Create and return a valid table for the database."""
        return Table(
            name=self.name,
            metadata=self.metadat,
            *self.columns
        )
