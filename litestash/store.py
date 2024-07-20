"""LiteStash Key-Value Store

This module provides the `LiteStash` class, which acts as the main interface for
interacting with the distributed SQLite-based key-value store. It offers methods
for setting, getting, deleting, and listing key-value pairs.
"""
import orjson
from typing import overload
from sqlalchemy import insert
from sqlalchemy import select
from pydantic import ValidationError
from litestash.core.config.root import Tables as All_Tables
from litestash.core.config.litestash_conf import StashSlots
from litestash.core.engine import Engine
from litestash.core.schema import Metadata
from litestash.core.session import Session
from litestash.models import LiteStashData
from litestash.core.util.litestash_util import get_keys
from litestash.core.util.litestash_util import get_values
from litestash.core.util.litestash_util import get_datastore
from litestash.core.util.litestash_util import get_primary_key
from litestash.core.util.schema_util import get_db_name
from litestash.core.util.schema_util import get_table_name
from litestash.core.util.schema_util import mk_table_names

class LiteStash:
    """A high-performance in-memory key-value store using SQLite."""

    __slots__ = (StashSlots.ENGINE.value,
                 StashSlots.METADATA.value,
                 StashSlots.DB_SESSION.value
    )

    def __init__(self):
        """Initiate a new LiteStash

        Creates a empty cache by default.
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
        """Inserts or updates a key-value pair.

        Args:
            data: Either a `LiteStashData` object or a string key.
            value: The JSON value to store (only required when `data` is a
            string).

        Raises:
            ValueError: If the key or value is invalid.
            ValidationError: If the `LiteStashData` object fails validation.
        """
        if isinstance(data, LiteStashData):
            store = get_datastore(data)
            stash = LiteStashData(store.key)

        if isinstance(data, str):
            if value is not None:
                try:
                    stash = LiteStashData(key=data, value=value)
                except ValueError as v:
                    print(f'Error: {v}')
                except ValidationError as e:
                    print(f'Invalid key: {e}')
                store = get_datastore(stash)


        table_name = get_table_name(store.key_hash[0])
        db_name = get_db_name(store.key_hash[0])
        metadata = self.metadata.get(db_name)
        session = self.db_session.get(db_name)
        table = metadata.tables[table_name]

        sql_statement = (
            insert(table)
            .values(
                key_hash=store.key_hash,
                key=store.key,
                value=store.value,
                timestamp=store.timestamp,
                microsecond=store.microsecond
            )
        )
        with session() as set_session:
            set_session.execute(sql_statement)
            set_session.commit()


    @overload
    def get(self, data: LiteStashData):
        """Set LiteStashData

        Get json data for the given data stash
        Args:
            data: LiteStashData

        """


    def get(self, data: str) -> LiteStashData | None:
        """Retrieves a value from the cache by key.

        Args:
            key_or_data (str | LiteStashData): The key (string) or a
            `LiteStashData` object containing the key.

        Returns:
            LiteStashData: The retrieved key-value pair, or None if not found.
        """
        if isinstance(data, LiteStashData):
            store = get_datastore(data)
            stash = LiteStashData(store.key)

        if isinstance(data, str):
            try:
                stash = LiteStashData(key=data)
            except ValueError as v:
                print(f'Error: {v}')
            except ValidationError as e:
                print(f'Invalid key: {e}')
            store = get_datastore(stash)

        table_name = get_table_name(store.key_hash[0])
        db_name = get_db_name(store.key_hash[0])
        metadata = self.metadata.get(db_name)
        session = self.db_session.get(db_name)
        hash_key = get_primary_key(store.key)
        table = metadata.tables[table_name]
        sql_statement = (
            select(table).where(table.c.key_hash == hash_key)
        )

        with session() as get_session:
            data = get_session.execute(sql_statement).first()
            get_session.commit()

        if data:
            json_data = str(data[2])
            stash.value = orjson.dumps(json_data)
            return stash
        else:
            return None


    @overload
    def delete(self, data: LiteStashData):
        """LiteStash Delete

        Remove a key-value pair from the stash
        Args:
            data (LiteStashData): Remove stored data with DTO
        """


    def delete(self, data: str):
        """Deletes a key-value pair from the database.

        Args:
            data: Either a `LiteStashData` object or a string key to delete.
        """
        if isinstance(data, LiteStashData):
            store = get_datastore(data)
            stash = LiteStashData(store.key)

        if isinstance(data, str):
            try:
                stash = LiteStashData(key=data)
            except ValueError as v:
                print(f'Error: {v}')
            except ValidationError as e:
                print(f'Invalid key: {e}')
            store = get_datastore(stash)

        table_name = get_table_name(store.key_hash[0])
        db_name = get_db_name(store.key_hash[0])
        metadata = self.metadata.get(db_name)
        session = self.db_session.get(db_name)
        hash_key = get_primary_key(store.key)
        table = metadata.tables[table_name]
        sql_statement = (
            select(table).where(table.c.key_hash == hash_key)
        )

        with session() as delete_session:
            data = delete_session.execute(sql_statement)
            delete_session.delete(data)
            delete_session.commit()


    def keys(self) -> list[str]:
        """Returns a list of all keys in the database."""
        keys = []
        for db_name in All_Tables:
            table_names = mk_table_names(db_name)
            metadata = self.metadata.get(db_name)
            session = self.db_session.get(db_name)
            for table_name in table_names:
                table = metadata.tables[table_name]
                table_keys = get_keys(session, table)
                keys.append(table_keys)
        return keys


    def values(self) -> list[dict]:
        """Returns a list of all values (as dictionaries) in the database."""
        values = []
        for db_name in All_Tables:
            table_names = mk_table_names(db_name)
            metadata = self.metadata.get(db_name)
            session = self.db_session.get(db_name)
            for table_name in table_names:
                table = metadata.tables[table_name]
                table_values = get_values(session, table)
                values.append(table_values)
        return values

    def exists(self, key: str) -> bool:
        """Checks if a key exists in the database.

        Args:
            key (str): The key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        if isinstance(key, LiteStashData):
            store = get_datastore(key)
            stash = LiteStashData(store.key)

        if isinstance(key, str):
            try:
                stash = LiteStashData(key=key)
            except ValueError as v:
                print(f'Error: {v}')
            except ValidationError as e:
                print(f'Invalid key: {e}')
            store = get_datastore(stash)

        table_name = get_table_name(store.key_hash[0])
        db_name = get_db_name(store.key_hash[0])
        metadata = self.metadata.get(db_name)
        session = self.db_session.get(db_name)
        hash_key = get_primary_key(store.key)
        table = metadata.tables[table_name]
        sql_statement = (
            select(table).where(table.c.key_hash == hash_key)
        )

        with session() as exist_session:
            data = exist_session.execute(sql_statement).scalar_one()
            exist_session.commit()

        if data:
            return True
        else:
            return False


    def clear(self) -> None:
        """Clears all entries from the database."""
        for db_name in All_Tables:
            metadata = self.metadata.get(db_name)
            metadata.drop_all()
            metadata.create_all()


    def __repr__(self) -> str:
        """Detailed string representation"""
        pass

    def __str__(self) -> str:
        """Quick and minimal string"""
        pass
