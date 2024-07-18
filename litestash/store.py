"""The Storage module

Define the LiteStash key-value database object.
LiteStash is a text key with JSON value key value store.
"""
from typing import overload
from sqlalchemy import insert
from sqlalchemy import select
from pydantic import ValidationError
from litestash.core.config.litestash_conf import StashSlots
from litestash.core.engine import Engine
from litestash.core.schema import Metadata
from litestash.core.session import Session
from litestash.models import LiteStashData
from litestash.core.util.litestash_util import get_datastore
from litestash.core.util.litestash_util import allot
from litestash.core.util.schema_util import get_db_name
from litestash.core.util.schema_util import get_table_name

class LiteStash:
    """The LiteStash

    TODO: docs
    """
    __slots__ = (StashSlots.ENGINE.value,
                 StashSlots.METADATA.value,
                 StashSlots.DB_SESSION.value
    )

    def __init__(self):
        """Initiate a new LiteStash

        Creates a new empty cache by default.
        """
        self.engine = Engine()
        self.metadata = Metadata(self.engine)
        self.db_session = Session(self.engine)

    @overload
    def set(self, key: str, value: str) -> None:
        """Set String Data

        Add a new key to the database.
        If key already exists update the value.
        Args:
            key (str):

            value (str):
        """


    @overload
    def set(self, data: LiteStashData) -> None:
        """Set LiteStashData

        Add valid data to the database.
        Args:
            data: LiteStashData
        """


    def set(self, data: str | LiteStashData, value: str):
        """Overloaded Set Function

        Insert or Update the the data named in the stash
        """
        stash_data = data

        if isinstance(data, LiteStashData):
            stash_data = get_datastore(data)

        if isinstance(data, str):
            try:
                stash = LiteStashData(key=data, value=value)
            except ValueError as v:
                print(f'Error: {v}')
            except ValidationError as e:
                print(f'Invalid key: {e}')
            stash_data = get_datastore(stash)

        table_name = get_table_name(stash_data.key_hash[0])
        db_name = get_db_name(stash_data.key_hash[0])
        metadata = self.metadata.get(db_name)
        session = self.session.get(db_name)

        table = metadata.tables[table_name]
        sql_statement = (
            insert(table)
            .values(
                key_hash=stash_data.key_hash,
                key=stash_data.key,
                value=stash_data.value,
                timestamp=stash_data.date_time,
                microseconds=stash_data.ms_time
            )
        )
        with session():
            session.execute(sql_statement)


    @overload
    def get(self, data: LiteStashData):
        """Set LiteStashData

        Get json data for the given data stash
        Args:
            data: LiteStashData

        """


    def get(self, data: str) -> LiteStashData | None:
        """LiteStash Get a value.

        Given a key return the value stored.
        Returns the key,value as LiteStashData.
        Args:
            key (str): The key for the json data
        """
        if isinstance(data, LiteStashData):
            stash_data = get_datastore(data)
            stash = LiteStashData(stash_data.key)

        if isinstance(data, str):
            try:
                stash = LiteStashData(key=data)
            except ValueError as v:
                print(f'Error: {v}')
            except ValidationError as e:
                print(f'Invalid key: {e}')
            stash_data = get_datastore(stash)

        table_name = get_table_name(stash_data.key_hash[0])
        db_name = get_db_name(stash_data.key_hash[0])
        metadata = self.metadata.get(db_name)
        session = self.session.get(db_name)

        table = metadata.tables[table_name]
        sql_statement = (
            select(table)
            .where(
                table.key_hash == stash_data.key_hash
            )
        )

        with session.begin() as db_get:
            data = db_get.execute(sql_statement)

        if data:
            stash.value = data.value
            return stash

        else:
            return None


    def delete(self):
        """LiteStash Delete

        Remove a give key and its value from the database.
        """
        pass

    def keys(self):
        """ListStash Keys"""
        pass

    def values(self):
        """Return all values from database in a dictionary."""
        pass

    def exists(self, key: str) -> bool:
        """Check if key exists and return true if it does."""


    def clear(self) -> None:
        """Clear all entries from the database."""
        pass

    def __repr__(self) -> str:
        """Detailed string representation"""
        pass

    def __str__(self) -> str:
        """Quick and minimal string"""
        pass
