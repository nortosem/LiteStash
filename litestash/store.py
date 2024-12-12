"""LiteStash Key-Value Store

This module provides the `LiteStash` class, which acts as the main interface for
interacting with the distributed SQLite-based key-value store. It offers methods
for setting, getting, deleting, and listing key-value pairs.
"""
import orjson
from typing import overload
from typing import Dict
from typing import List
from typing import Union
from pydantic import Json
from pydantic import StrictStr
from pydantic import StrictBool
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import delete
from concurrent.futures import ThreadPoolExecutor, Future
from litestash.logging import root_logger as logger
from litestash.core.config.root import Tables as All_Tables
from litestash.core.config.litestash_conf import StashSlots
from litestash.core.engine import Engine
from litestash.core.schema import Metadata
from litestash.core.session import Session
from litestash.models import LiteStashData
from litestash.core.config.litestash_conf import StashError
from litestash.core.util import fts
from litestash.core.util.litestash_util import get_keys
from litestash.core.util.litestash_util import get_values
from litestash.core.util.litestash_util import get_datastore
from litestash.core.util.litestash_util import get_primary_key
from litestash.core.util.schema_util import get_db_name
from litestash.core.util.schema_util import get_table_name
from litestash.core.util.schema_util import mk_table_names

class LiteStash:
    """A high-performance key-value store using SQLite."""

    __slots__ = (StashSlots.ENGINE.value,
                 StashSlots.METADATA.value,
                 StashSlots.DB_SESSION.value
    )

    def __init__(self, search: StrictBool = False):
        """Initiate a new LiteStash

        Creates a empty cache by default.
        """
        self.engine = Engine()
        self.metadata = Metadata(self.engine)
        self.db_session = Session(self.engine)

        if search:
            fts.create_all_search_tables(
                self.engine,
                self.metadata,
                self.db_session
            )

    @overload
    def set(self,
            key: StrictStr,
            value: Union[StrictStr, Json, None] = None) -> None:
        """Overload set using key,value string"""


    @overload
    def set(self, key: LiteStashData) -> None:
        """Overload set using LiteStashData"""


    def set(self,
            key: StrictStr | LiteStashData,
            value: Union[StrictStr, Json, None] = None):
        """Inserts or updates a key-value pair.

        Args:
            key: Either a `LiteStashData` object or a string key.
            value: The JSON value to store

        Raises:
            ValidationError: If the `LiteStashData` object fails validation.
            Exception: For unexpected errors
        """
        try:
            if isinstance(key, LiteStashData):
                if value is not None:
                    logger.error(f'Value supplied with LiteStashData')
                    raise ValidationError(
                        'Possible duplicate values for a key.')

                logger.debug(f'litestash data type check: {type(data)}')
                data = get_datastore(key)

            else:
                if value is None:
                    raise TypeError(f'{StashError.KEY_TYPE.value} ')

                data = LiteStashData(key=data, value=value)
                logger.debug(f'data: {data}')
                data = get_datastore(data)
                logger.debug(f'data2store: {data}')

            table_name = get_table_name(data.key_hash[0])
            logger.debug(f'table_name for data: {table_name}')
            db_name = get_db_name(data.key_hash[0])
            logger.debug(f'db _name for data: {db_name}')
            metadata = self.metadata.get(db_name).metadata
            logger.debug(f'metadata tables: {metadata.tables}')
            session = self.db_session.get(db_name).session
            logger.debug(f'session: {session.kw}')
            table = metadata.tables[table_name]
            sql_statement = (
                insert(table)
                .values(
                    key_hash=data.key_hash,
                    key=data.key,
                    value=data.value,
                    timestamp=data.timestamp,
                    microsecond=data.microsecond
                )
            )
            with session() as set_session:
                set_session.execute(sql_statement)
                set_session.commit()
        except ValidationError as invalid_error:
            logger.error(f'Validation error: {invalid_error}')
            raise
        except Exception as error:
            logger.error(f'An unexpected error: {error}')
            raise


    @overload
    def get(self, data: LiteStashData) -> LiteStashData | None:
        """Overload get using LiteStashData type"""


    @overload
    def get(self, data: str) -> LiteStashData | None:
        """Overload get using string type"""


    def get(self, data: str | LiteStashData) -> LiteStashData | None:
        """Retrieves a value from the cache by key.

        Args:
            key_or_data (str | LiteStashData): The key (string) or a
            `LiteStashData` object containing the key.

        Returns:
            LiteStashData: The retrieved key-value pair, or None if not found.
        """
        if isinstance(data, LiteStashData):
            data = get_datastore(data)
        elif isinstance(data, str):
            data = LiteStashData(key=data)
        else:
            raise TypeError(
                f'{StashError.KEY_TYPE.value} not {type(data).__name__}'
            )

        hash_key = get_primary_key(data.key)
        table_name = get_table_name(hash_key[0])
        db_name = get_db_name(hash_key[0])
        metadata = self.metadata.get(db_name).metadata
        session = self.db_session.get(db_name).session
        table = metadata.tables[table_name]
        sql_statement = select(table).where(table.c.key_hash == hash_key)

        with session() as get_session:
            result = get_session.execute(sql_statement).first()
            get_session.commit()

        if result:
            return LiteStashData(
                key=result[1],
                value=orjson.loads(result[2])
            )
        else:
            return None

    @overload
    def mget(self, keys: List[LiteStashData]) -> List[LiteStashData]:
        """Get many keys using LiteStashData Objects"""


    @overload
    def mget(self, keys: List[str]) -> List[LiteStashData]:
        """Get many keys by string list of key names"""


    def mget(self,
             keys: List[str] | List[LiteStashData]) -> List[LiteStashData]:
        """Bulk get of multiple keys"""
        pass

    @overload
    def mset(self, data: List[LiteStashData], ttl: int) -> None:
        """"""


    @overload
    def mset(self, data: List[Dict], ttl: int) -> None:
        """"""


    @overload
    def mset(self, data: List[str], ttl: int) -> None:
        """"""


    def mset(
        self,
        data: List[str] | List[Dict] | List[LiteStashData],
        ttl: int) -> None:
        """

        todo
        """
        pass


    def expire(self,
               keys: str | List[str] | None = None,
               ttl: int = None) -> int:
        """Expire a key, some keys, or all keys

        Todo
        """
        pass


    def search(text: str = None):
        """Search all of the JSON stored for a key and return the value"""
        pass


    def keys(self) -> list[str]:
        """Returns a list of all keys in the database."""
        keys = []
        for db_name in All_Tables:
            table_names = mk_table_names(db_name.value)
            metadata = self.metadata.get(db_name.value).metadata
            session = self.db_session.get(db_name.value).session
            for table_name in table_names:
                table = metadata.tables[table_name]
                table_keys = get_keys(session, table)
                keys.append(table_keys)
        return keys


    def values(self) -> list[dict]:
        """Returns a list of all values (as dictionaries) in the database."""
        values = []
        for db_name in All_Tables:
            table_names = mk_table_names(db_name.value)
            metadata = self.metadata.get(db_name.value).metadata
            session = self.db_session.get(db_name.value).session
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
        if not isinstance(key, str):
            raise TypeError(
                f'{StashError.KEY_TYPE.value} not {type(key).__name__}'
            )

        if isinstance(key, str):
            key = LiteStashData(key=key)

        hash_key = get_primary_key(key.key)
        table_name = get_table_name(hash_key[0])
        db_name = get_db_name(hash_key[0])
        metadata = self.metadata.get(db_name).metadata
        session = self.db_session.get(db_name).session
        table = metadata.tables[table_name]
        sql_statement = (
            select(table).where(table.c.key_hash == hash_key)
        )

        with session() as exist_session:
            data = exist_session.execute(sql_statement).first()
            exist_session.commit()

        if data:
            return True
        else:
            return False


    @overload
    def delete(self, data: LiteStashData):
        """LiteStash Delete

        Remove a key-value pair from the stash
        Args:
            data (LiteStashData): Remove stored data with DTO
        """


    def delete(self, key: str):
        """Deletes a key-value pair from the database.

        Args:
            data: Either a `LiteStashData` object or a string key to delete.
        """
        if not isinstance(key, str):
            raise TypeError(
                f'{StashError.KEY_TYPE.value} not {type(key).__name__}'
            )

        if isinstance(key, str):
            key = LiteStashData(key=key)

        hash_key = get_primary_key(key.key)
        table_name = get_table_name(hash_key[0])
        db_name = get_db_name(hash_key[0])
        metadata = self.metadata.get(db_name).metadata
        session = self.db_session.get(db_name).session
        table = metadata.tables[table_name]

        with session() as delete_session:
            delete_session.execute(
                delete(table).where(table.c.key_hash == hash_key)
            )
            delete_session.commit()


    def clear(self) -> None:
        """Clears all entries from the database."""
        for db in self.metadata.__slots__:
            metadata = self.metadata.get(db).metadata
            engine = self.engine.get(db).engine
            metadata.drop_all(bind=engine)

        self.engine = Engine()
        self.metadata = Metadata(self.engine)
        self.db_session = Session(self.engine)


    def __repr__(self) -> str:
        """Detailed string representation of the LiteStash instance"""
        repr_str = 'LiteStash('

        repr_str += '\n  Databases:'
        for db_name in self.metadata.__slots__:
            metadata = self.metadata.get(db_name).metadata
            repr_str += f'\n    - {db_name}: {list(metadata.tables.keys())}'
        repr_str += '\n)'
        return repr_str


    def __str__(self) -> str:
        """Returns a concise string representation of the LiteStash instance."""
        return f'LiteStash(databases={len(self.metadata.__slots__)})'
