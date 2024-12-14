"""LiteStash Engine Manager

This module provides engines for all SQLite databases used in the LiteStash
key-value store.
"""
from sqlalchemy import Engine as SQL_Engine
from litestash.core.config.root import Tables
from litestash.core.config.root import ErrorMessage
from litestash.core.util.engine_util import setup_engine

class Engine:
    """LiteStash Engine Class

    This class manages the creation and access of SQLAlchemy engines for each
    SQLite database file used in the LiteStash key-value store. Each database
    file is associated with a specific range of hash prefixes, ensuring
    efficient data distribution.

    Attributes:

        __slots__ (tuple): A tuple of attribute names for memory optimization.

    Methods:

        __init__(): Initializes the Engine object, creating engine instances
        for each database file.

        get(name): Retrieves a specific SQLAlchemy engine by its name.

        __iter__(): Returns an iterator that yields all the engine attributes.
    """
    __slots__ = Tables.slots()


    def __init__(self):
        """Initializes the Engine object by creating SQLAlchemy engines for
        each database file.
        """
        for table in self.__slots__:
            setattr(self, table, setup_engine(table))


    def get(self, name: str) -> SQL_Engine:
        """Retrieves a specific SQLAlchemy engine by its name.

        Args:
            name: The name of the database (e.g., 'tables_03').

        Returns:
            The SQLAlchemy engine associated with the specified database.

        Raises:
            AttributeError: If no engine is found with the given name.
        """
        if name not in self.__slots__:
            raise ValueError(f'{ErrorMessage.GET_ENGINE.value} {name}')
        attribute = getattr(self, name)
        return attribute


    def __iter__(self):
        """Yields all engine attributes (name, engine tuples)."""
        yield from (getattr(self, slot) for slot in self.__slots__)


    def __repr__(self):
        """Return the details for each engine stored in the Engine object."""
        rstr = "Engine(\n"
        for table in Tables:
            engine_attr = getattr(self, table.value)
            name = table.value
            db = engine_attr.db_name
            url = engine_attr.engine
            rstr += f"{name}: {db}.db, {url}\n"
        rstr += ")"
        return rstr


    def __str__(self):
        """Concise string representation of the LiteStash Engine"""
        data = self.__slots__
        s = f'Engine(databases={data},length={len(data)})'
        return s
