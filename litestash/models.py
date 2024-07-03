"""The Models

The base and table models for a stash.
"""
from datetime import datetime
from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

class StashModel(SQLModel):
    """Stash: Base Model

    TODO
    """
    id: int | None = Field(default=None, primary_key=True)
    hash_key: str | None = Field(default=None, primary_key=True)
    key: str = Field(default=None, index=True)
    value: str = Field(default=None, index=True)
    date_created: datetime | None = Field(default=None)
