"""LiteStash Session Manager

Creates and provides access to session factories for each database in
LiteStash.
"""
from litestash.core.engine import Engine
from litestash.core.config.root import Tables
from litestash.core.config.root import ErrorMessage
from litestash.core.util.core_util import setup_sessions


class Session:
    """LiteStash Session

    This class manages the creation and access of SQLAlchemy sessions for each
    SQLite database file used in the LiteStash key-value store. Each database
    file is associated with a specific session.

    Attributes:

        __slots__ (tuple): A tuple of attribute names for memory optimization.

    Methods:

        __init__(): Initializes the Engine object, creating engine instances
        for each database file.

        get(name): Retrieves a specific SQLAlchemy engine session by its name.

        __iter__(): Returns an iterator that yields all the sesssion
        attributes.
    """
    __slots__ = Tables.slots()

    def __init__(self, engine: Engine):
        """Initializes session factories for each database.

        Args:
            engine (EngineStash): An instance of the `EngineStash` class
            containing the database engines.
        """
        for table in self.__slots__:
            setattr(self, table, setup_sessions(engine.get(table)))


    def get(self, db_name):
        """Gets the session factory for the specified database.

        Args:
            db_name (str): The name of the database (e.g., "tables_03").

        Returns:
            sessionmaker: The SQLAlchemy session factory for the given
            database.

        Raises:
            AttributeError: If no session factory exists for the given
            database name.
        """
        if db_name not in self.__slots__:
            raise ValueError(f'{ErrorMessage.GET_ENGINE.value} {db_name}')
        attribute = getattr(self, db_name)
        return attribute


    def __iter__(self):
        """
        Yields all session attributes (database name, session factory tuples).
        """

        yield from (getattr(self, slot) for slot in self.__slots__)


    def __repr__(self):
        """TODO"""
        pass

    def __str__(self):
        """TODO"""
        pass
