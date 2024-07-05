"""The Models

The base and table models for a stash.
"""
from litestash.config import TableName
from litestash.config import Num
from litestash.config import LowerCase
from litestash.config import UpperCase
from typing import Literal
from typing import Generator
from datetime import datetime
from pydantic import BaseModel
from pydantic import Json
from pydantic import StrictStr
from pydantic import StrictInt
from pydantic import Field
from pydantic import Relationship
from pydantic.dataclasses import dataclass
from sqlalchemy.schema import Column
from sqlalchemy.schema import Table
from sqlalchemy.shema import Metadata
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

@dataclass(slots=True)
class LiteStashData(BaseModel):
    """The LiteStash Data

    This class defines a class of data for use with the LiteStash database.
    """
    key: StrictStr
    value: Json


@dataclass(slots=True)
class LiteStashStore(Base, LiteStashData):
    """LiteStash Database Fields

    The database storage class.  Defines all columns and column types in db.
    Only used by the Stash Manager and the database interface.
    """
    hash_key: StrictStr | None = Field(default=None, unique=True, index=True)
    key: StrictStr = Field(default=None, unique=True, index=True)
    value: JSON = Field(default=None, index=True)
    date_created:  | None = Field(default=datetime.now())


@dataclass(slots=True)
class ColumnLiteStash(BaseModel):
    """LiteStash Columns

    TODO
    """
    name: StrictStr
    type_: Literal["StrictStr", "StrictInt", "JSON"]
    primary_key: bool = False
    index: bool = False
    unique: bool = False


    def mk_id(self) -> Column:
        """Return the unique id column"""
        return Column('id',Integer,primary_key=True)

    def mk_hash(self) -> Column:
        """Return a Column for the hash"""
        return Column(self.name, str, index=True, unique=True)

    def mk_key(self) -> Column:
        """Return a Column for the key being stored."""
        return Column(self.name, str, index=True, unique=True)

    def mk_value(self) -> Column:
        """Return a Column for the value being stored."""
        return Column(self.name, JSON, index=True)

    def mk_date_create(self) -> Column:
        """Return a Column for the date the data was added."""
        return Column(self.name, str)


def mk_table_names() -> Generator[str, None, None]:
    """Make all valid Table names

    Generate names for all tables in cache
    Return a generator.
    """
    for chars in (Num,LowerCase,UpperCase):
        for suffix in chars:
           yield f'{TableName.ROOT.value}{suffix.value}'


def mk_table(name: str,  ) -> Table:
    """


    """
    pass


def mk_tables() -> Generator[Table, None, None]:
    """


    """
    pass


def mk_columns() -> Generator[Column, None, None]:
    """


    """
    pass



