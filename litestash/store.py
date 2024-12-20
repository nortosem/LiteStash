"""LiteStash Key-Value Store

This module provides the `LiteStash` class, which acts as the main interface for
interacting with the distributed SQLite-based key-value store. It offers methods
for setting, getting, deleting, and listing key-value pairs.
"""
import orjson

from datetime import datetime

from typing import Dict
from typing import List
from typing import Optional
from typing import overload
from typing import Union

from pydantic import Json
from pydantic import StrictFloat
from pydantic import StrictInt
from pydantic import StrictStr
from pydantic import StrictBool
from pydantic import ValidationError

from litestash.core.config.litestash_conf import EngineConf
from litestash.core.config.litestash_conf import StashError
from litestash.core.config.litestash_conf import StashSlots
from litestash.core.config.root import Tables as All_Tables
from litestash.core.engine import Engine
from litestash.core.util import fts
from litestash.core.util.connection_util import GetTime
from litestash.core.util.litestash_util import connect
from litestash.core.util.litestash_util import connections
from litestash.core.util.litestash_util import does_exist
from litestash.core.util.litestash_util import delete_data
from litestash.core.util.litestash_util import get_data
#from litestash.core.util.litestash_util import get_datastore
from litestash.core.util.litestash_util import get_keys
from litestash.core.util.litestash_util import get_time
from litestash.core.util.litestash_util import get_values
from litestash.core.util.litestash_util import mget_data
from litestash.core.util.litestash_util import mset_data
from litestash.core.util.litestash_util import mk_datastore
from litestash.core.util.litestash_util import set_data
from litestash.core.util.schema_util import mk_table_names
from litestash.core.schema import Metadata
from litestash.core.session import Session
from litestash.logging import root_logger as logger
from litestash.models import LiteStashData


class LiteStash:
    """A high-performance key-value store using SQLite."""

    __slots__ = StashSlots.slots()


    def __init__(self,
                 cache: StrictBool = False,
                 data: Optional[StrictStr] = None,
                 search: StrictBool = False):
        """Initiate a new LiteStash

        Creates an empty cache by default.
        """
        self.engine = Engine(cache=cache, data=data)
        self.metadata = Metadata(self.engine)
        self.db_session = Session(self.engine)

        if search:
            fts.create_all_search_tables(
                self.engine,
                self.metadata,
                self.db_session
            )

    @overload
    def get(self, key: LiteStashData) -> Optional[LiteStashData]:
        """Overload get using LiteStashData type"""


    @overload
    def get(self, key: StrictStr) -> Optional[LiteStashData]:
        """Overload get using string type"""


    def get(self, key: StrictStr | LiteStashData) -> Optional[LiteStashData]:
        """Retrieves a value from the cache by key.

        Args:
            key (str | LiteStashData): The key (string) or a
            `LiteStashData` object containing the key.

        Returns:
            LiteStashData: The retrieved key-value pair, or None if not found.
        """
        try:
            data = None
            if isinstance(key, str):
                data = LiteStashData(key=key)
            elif isinstance(key, LiteStashData):
                data = key

            return get_data(connect(
                data=data,
				metadata=self.metadata,
                db_session=self.db_session
            ))
        except ValidationError as error:
            logger.error('invalid: %s', error)
            raise
        except ValueError as error:
            logger.error('invalid: %s', error)
            raise


    @overload
    def mget(self, keys: List[StrictStr]) -> Optional[LiteStashData]:
        """"""

    @overload
    def mget(self, keys: List[LiteStashData]) -> Optional[LiteStashData]:
        """"""

    def mget(self,
        keys: List[StrictStr | LiteStashData]) -> Optional[LiteStashData]:
        """mget

        Retrieves multiple values from the key-value store.

        Args:
            keys (List[StrictStr | LiteStashData]): A list of keys to retrieve.

        Returns:
            List[LiteStashData | None]:
                A list of retrieved LiteStashData objects or None for keys not
                found.

        Raises:

        """
        def setup_keys(keys):
            to_connect = []
            if all(isinstance(item, str) for item in keys):
                to_connect = [LiteStashData(key=key) for key in keys]
                return to_connect
            elif all(isinstance(key, LiteStashData) for key in keys):
                return keys

        try:
            return mget_data(connections(setup_keys(keys)),
                             self.metadata,
                             self.db_session)

        except TypeError as error:
            logger.error('%s is not a %s: %s',
                         type(keys).__name__,
                         StashError.KEY_TYPE.value,
                         error)
            raise
        except ValidationError as error:
            logger.error('invalid: %s', error)
            raise


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
        value: Union[StrictStr, Json, None] = None) -> None:
        """Inserts or updates a key-value pair.

        Args:
            key: Either a `LiteStashData` object or a string key.
            value: The JSON value to store

        Returns:
            True: On successfully setting a key-value to the database.

        Raises:
            ValidationError: If the `LiteStashData` object fails validation.
            Exception: For unexpected errors
        """
        try:
            if isinstance(key, LiteStashData):
                data = key
                logger.debug('litestash data type check: %s', type(data))

            else:
                data = LiteStashData(key=key, value=value)
                logger.debug('stashdata: %s', data)

            data = mk_datastore(data)
            logger.debug('litestash datastore: %s', data)

            set_data(connect(
                data=data, metadata=self.metadata, db_session=self.db_session
            ))

        except ValueError as invalid:
            logger.error('ValueError: %s', invalid)
            raise
        except ValidationError as invalid:
            logger.error('Unexpected type of argument: %s', invalid)
            raise


    @overload
    def mset(self, data: List[LiteStashData]) -> None:
        """"""


    @overload
    def mset(self, data: List[Dict]) -> None:
        """"""


    @overload
    def mset(self, data: List[StrictStr]) -> None:
        """"""


    def mset(
        self,
        data: List[Union[StrictStr | Dict | LiteStashData]]
        ) -> None:
        """mset

        Batch multiple key-value entries.
        """
        def parse_str(data):
            parsed = []
            try:
                for element in data:
                    e = orjson.loads(element)
                    if isinstance(e, dict):
                        raise ValueError(f'invalid json: {type(e)} for {e}')
                    parsed.append(e.popitem())
                return parsed
            except ValueError as error:
                logger.error('Expected JSON, not: %s', error)
                raise
            except ValidationError as error:
                logger.error('Invalid string input: %s', error)
                raise

        def setup_data(data):
            to_connect = []
            if all(isinstance(item, dict) for item in data):
                to_connect = [
                    mk_datastore(LiteStashData(key=k, value=orjson.dumps(v))) \
                        for d in data for k, v in d.items()
                ]

            elif all(isinstance(item, str) for item in data):
                to_connect = [
                    mk_datastore(LiteStashData(key=e[0],
                                              value=orjson.dumps(e[1]))) \
                        for e in parse_str(data)
                ]
            elif all(isinstance(item, LiteStashData) for item in data):
                to_connect = [
                    mk_datastore(item) for item in data
                ]
            return to_connect

        try:

            mset_data(connections(setup_data(data)),
                      self.metadata,
                      self.db_session)

        except ValueError as invalid:
            logger.error('Invalid data: %s', invalid)
            raise
        except ValidationError as error:
            logger.error('An invalid argument: %s', error)
            raise


    def expire(self, keys: Union[StrictStr | List[StrictStr] | None] = None,
               ttl: Union[StrictFloat | StrictInt | GetTime] = None) -> None:
        """Expire

        Check the time age of a key with a time-to-live value.
        One or more keys may be provided to check specific keys.
        Otherwise if only a time-to-live is given all keys are checked.
        String keys may be separated by spaces.

        Args:
Args:
        keys (Optional[Union[StrictStr, List[StrictStr]]]):
            Zero or more strings for checking JSON expiration time.

        ttl (Optional[Union[StrictFloat, StrictInt, GetTime]]):
            A Unix timestamp with or without microseconds or a LiteStash
            GetTime tuple.

        Raises:
            TypeError:
                If ttl is not provided or cannot be converted to GetTime.
            ValidationError:
                todo
        """
        try:
            if ttl is None:
                raise TypeError('Time to live required to expire data')

            if isinstance(ttl, datetime):
                ttl = GetTime(int(ttl.timestamp()), ttl.microsecond)

            elif isinstance(ttl, (float, int)):
                ttl = datetime.fromtimestamp(ttl)
                ttl = GetTime(int(ttl.timestamp()), ttl.microsecond)

            if keys is None:
                keys = self.keys()
                if keys is None:
                    return None

            elif isinstance(keys, str):
                keys = keys.split()

            if isinstance(keys, list) and all(
                    isinstance(k, str) for k in keys
            ):
                for key in keys:
                    data = get_time(key)
                    if data.timestamp >= ttl.timestamp:
                        self.delete(key)
        except ValidationError as invalid:
            logger.error('todo: %s', invalid)
            raise
        except TypeError as error:
            logger.error('ttl required: %s', error)
            raise

    def search(text: str = None):
        """Search all of the JSON stored for a key and return the value"""
        pass


    def keys(self) -> Optional[List[StrictStr]]:
        """Returns a list of all keys in the database."""
        keys = []
        for db_name in All_Tables:
            table_names = mk_table_names(db_name.value)
            metadata = self.metadata.get(db_name.value).metadata
            session = self.db_session.get(db_name.value).session
            for table_name in table_names:
                table = metadata.tables[table_name]
                table_keys = get_keys(session, table)
                keys.extend(table_keys)
        return keys


    def values(self) -> Optional[List[Json]]:
        """Returns a list of all values (as dictionaries) in the database."""
        values = []
        for db_name in All_Tables:
            table_names = mk_table_names(db_name.value)
            metadata = self.metadata.get(db_name.value).metadata
            session = self.db_session.get(db_name.value).session
            for table_name in table_names:
                table = metadata.tables[table_name]
                table_values = get_values(session, table)
                values.extend(table_values)
        return values


    def exists(self, key: StrictStr) -> StrictBool:
        """Checks if a key exists in the database.

        Args:
            key (str): The key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        try:
            if isinstance(key, str):
                data = LiteStashData(key=key)
                return does_exist(connect(
                    data=data,
                    metadata=self.metadata,
                    db_session=self.db_session
                ))
        except ValidationError as error:
            logger.error(
                '%s is not %s: %s',
                StashError.KEY_TYPE.value,
                type(key).__name__,
				error
            )


    @overload
    def delete(self, data: LiteStashData) -> None:
        """LiteStash Delete

        Remove a key-value pair from the stash
        Args:
            data (LiteStashData): Remove stored data with DTO
        """


    def delete(self, key: StrictStr) -> None:
        """Deletes a key-value pair from the database.

        Args:
            data: Either a `LiteStashData` object or a string key to delete.
        """
        try:
            data = None
            if isinstance(key, str):
                data = LiteStashData(key=key)

            delete_data(connect(
                data=data, metadata=self.metadata, db_session=self.db_session
	        ))
        except ValidationError as error:
            logger.error('%s not %s: %s',
                         StashError.KEY_TYPE.value,
                         type(key).__name__,
                         error)

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
        return f'LiteStash(databases={len(self.__slots__)})'
