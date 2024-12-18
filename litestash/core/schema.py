"""LiteStash Metadata Manager

Creates and provides access to metadata objects for each database in
LiteStash.
"""
from litestash.core.engine import Engine
from litestash.core.config.root import Tables
from litestash.core.config.root import ErrorMessage
from litestash.core.config.litestash_conf import StashSlots
from litestash.core.util.core_util import setup_metadata

class Metadata:
    """LiteStash Metadata Class

    This class manages the creation and access of SQLAlchemy Metadata for each
    SQLite database file used in the LiteStash key-value store. Each database
    file is associated with a specific Metadata object.

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
        """Create and bind each metadata object for each database to a
        matching engine.

        Args:
            engine (EngineStash): The EngineStash object containing the
            database engines.
        """
        for table in self.__slots__:
            setattr(self, table, setup_metadata(engine.get(table)))


    def get(self, db_name):
        """Retrieves the metadata for a specific database.

        Args:
            db_name: The name of the database (e.g., "tables_03").

        Returns:
            The SQLAlchemy MetaData object associated with the database.

        Raises:
            AttributeError: If no metadata is found for the given database
            name.
        """
        if db_name not in self.__slots__:
            raise ValueError(f'{ErrorMessage.GET_ENGINE.value} {db_name}')
        attribute = getattr(self, db_name)
        return attribute

    def __iter__(self):
        """Iterates over all database metadata objects."""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """Returns a detailed string representation of the metadata objects."""
        repr_str = ''
        repr_str += f'{StashSlots.METADATA.value}  Tables:\n'
        for prefix, metadata in self.metadata.items():
            repr_str += f'    {prefix}:\n'
            for table_name, table in metadata.tables.items():
                repr_str += f'      - {table_name}: {table.columns.keys()}\n'
        return repr_str

    def __str__(self):
        """Returns a simplified string representation of the metadata objects.
        """
        metadata_str = ''
        for prefix, metadata in self.metadata.items():
            metadata_str += f'    {prefix}:\n'
            for table_name, table in metadata.tables.items():
                metadata_str += f'   - {table_name}: {table.columns.keys()}\n'
        return metadata_str
