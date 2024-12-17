"""Connection Utilities

The Connection Utility module provides a set of classes to manage LiteStash
Database connections and data transfer.
"""
from abc import ABC

from collections import namedtuple

from sqlalchemy.orm import Session

from typing import List
from typing import Union
from typing import Set

from pydantic import StrictStr

from litestash.core.config.connection_conf import GetConnectionAttr
from litestash.core.config.connection_conf import SetConnectionAttr
from litestash.core.config.connection_conf import TimeAttr
from litestash.core.config.root import Tables
from litestash.core.session import Session as Manager
from litestash.models import LiteStashData
from litestash.models import LiteStashStore


# Time info for get_time function
GetTime = namedtuple(
    TimeAttr.TYPE_NAME.value,
    [
        TimeAttr.TIMESTAMP.value,
        TimeAttr.MICROSECOND.value
    ]
)
GetTime.__doc__ = TimeAttr.DOC.value


class Connection(ABC):
    """Connection

    An abstract base class for connections. This class is used to define
    the connection type for all connection types.
    """
    pass


GetConnection = namedtuple(
    GetConnectionAttr.TYPE_NAME.value,
    [
        GetConnectionAttr.HASH_KEY.value,
        GetConnectionAttr.TABLE.value,
        GetConnectionAttr.SESSION.value
    ]
)
GetConnectionAttr.__doc__ = GetConnectionAttr.DOC.value


SetConnection = namedtuple(
    SetConnectionAttr.TYPE_NAME.value,
    [
        SetConnectionAttr.DATA_STORE.value,
        SetConnectionAttr.TABLE.value,
        SetConnectionAttr.SESSION.value
    ]
)
SetConnectionAttr.__doc__ = SetConnectionAttr.DOC.value


class DatabaseConnections:
    """Database Connections

    Database Connections

    The Base class to manage connections for each database of a LiteStash.

    Attributes:
        __slots__ (tuple): Tuple of database names.

    Methods:
        __contains__(self, db_name: StrictStr) -> bool:
            Return boolean if database name is found.
        __getitem__(self, db_name: StrictStr) -> List[Union[
            LiteStashData, LiteStashStore]]:
                Return the self[database] connection list.
        __setitem__(self, db_name: StrictStr, value: Union[LiteStashData,
            LiteStashStore,
            List[LiteStashData],
            List[LiteStashStore]]) -> None:
                Update the self[database] connection list.
        clear(self) -> None:
            Remove all connections from all databases.
        get(self, db_name: StrictStr) -> List[Union[LiteStashData,
            LiteStashStore]]:
                Return the connection list for the given database.
        is_data(self, item) -> bool:
            Return True if the item is LiteStashData.
        is_store(self, item) -> bool:
            Return True if the item is LiteStashStore.
        items(self) -> List[Union[str, List[Union[LiteStashData,
            LiteStashStore]]]]:
            Return a list of all database and connection lists.
        keys(self) -> Set[str]:
            Return a set of all the databases available.
        session(self, database: StrictStr, manager: Manager) -> Session:
            Return a session for the database.
        values(self) -> List[Union[List[LiteStashData], List[LiteStashStore]]]:
            Return a list of all the connections for each database.
    """
    __slots__ = Tables.slots()

    def __init__(self):
        """Constructor to initialize database references."""
        for database in self.__slots__:
            setattr(self, database, None)


    def __contains__(self, db_name: StrictStr) -> bool:
        """Return boolean if database name is found."""
        return bool(db_name in self.__slots__)


    def __getitem__(self, db_name: StrictStr) -> List[Union[
            LiteStashData, LiteStashStore]]:
        """Return the self[database] connection list."""
        return getattr(self, db_name)


    def __setitem__(self, db_name: StrictStr,
                    value: Union[LiteStashData,
                                 LiteStashStore,
                                 List[LiteStashData],
                                 List[LiteStashStore]]
                    ) -> None:
        """Update the self[database] connection list."""
        if getattr(self, db_name) is None:
            setattr(self, db_name, [])

        conn = getattr(self, db_name)
        if isinstance(value, LiteStashData):
            conn.append(value)
        elif isinstance(value, LiteStashStore):
            conn.append(value)
        elif all(isinstance(item, LiteStashData) for item in value):
            conn.extend(value)
        elif all(isinstance(item, LiteStashStore) for item in value):
            conn.extend(value)


    def clear(self) -> None:
        """Remove all connections from all databases."""
        for database in self.__slots__:
            setattr(self, database, None)

    def get(self, db_name: StrictStr) -> List[Union[
            LiteStashData, LiteStashStore]]:
        """Return the coonnection list for the given database."""
        return getattr(self, db_name)


    def is_data(self, item) -> bool:
        """Return True if the item is LiteStashData"""
        return True if isinstance(item, LiteStashData) else False


    def is_store(self, item) -> bool:
        """Return True if the item is LiteStashStore"""
        return True if isinstance(item, LiteStashStore) else False


    def items(self) -> List[Union[str, List[Union[LiteStashData,
                                                  LiteStashStore]]]]:
        """Return a list of all database and connection lists."""
        return [[slot, getattr(self, slot)] for slot in self.__slots__]


    def keys(self) -> Set[str]:
        """Return a set of all the databases available."""
        return set(slot for slot in self.__slots__)


    def session(self, database: StrictStr, manager: Manager) -> Session:
        """Return a session for the database."""
        return manager.get(database).session


    def values(self) -> List[Union[List[LiteStashData],
                                   List[LiteStashStore]]]:
        """Return a list of all the connections for each database."""
        return [getattr(self, slot) for slot in self.__slots__]


class GetDataConnections(DatabaseConnections):
    """Get Database Connections

    The database connections for getting database values.
    """
    pass


class SetDataConnections(DatabaseConnections):
    """Set Database Connections

    The database connections for setting database values.
    """
    pass


class DataResults(DatabaseConnections):
    """Container for mget results."""
    pass
