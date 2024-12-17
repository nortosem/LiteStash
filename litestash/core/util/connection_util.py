"""Connection Utilities


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

    The Base class to manage connections for each database of a LiteStash.
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
