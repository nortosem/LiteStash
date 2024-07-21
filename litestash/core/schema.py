"""LiteStash Metadata Manager

Creates and provides access to metadata objects for each database in
LiteStash.
"""
from litestash.core.engine import Engine as EngineStash
from litestash.core.config.root import Tables
from litestash.core.config.litestash_conf import StashSlots
from litestash.core.util.litestash_util import setup_metadata

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
    __slots__ = (Tables.TABLES_03.value,
                 Tables.TABLES_47.value,
                 Tables.TABLES_89HU.value,
                 Tables.TABLES_AB.value,
                 Tables.TABLES_CD.value,
                 Tables.TABLES_EF.value,
                 Tables.TABLES_GH.value,
                 Tables.TABLES_IJ.value,
                 Tables.TABLES_KL.value,
                 Tables.TABLES_MN.value,
                 Tables.TABLES_OP.value,
                 Tables.TABLES_QR.value,
                 Tables.TABLES_ST.value,
                 Tables.TABLES_UV.value,
                 Tables.TABLES_WX.value,
                 Tables.TABLES_YZ.value
                )

    def __init__(self, engine_stash: EngineStash):
        """Create and bind each metadata object for each database to a
        matching engine.

        Args:
            engine_stash (EngineStash): The EngineStash object containing the
            database engines.
        """
        self.tables_03 = setup_metadata(
            engine_stash.get(Tables.TABLES_03.value)
        )
        self.tables_47 = setup_metadata(
            engine_stash.get(Tables.TABLES_47.value)
        )
        self.tables_89hu = setup_metadata(
            engine_stash.get(Tables.TABLES_89HU.value)
        )
        self.tables_ab = setup_metadata(
            engine_stash.get(Tables.TABLES_AB.value)
        )
        self.tables_cd = setup_metadata(
            engine_stash.get(Tables.TABLES_CD.value)
        )
        self.tables_ef = setup_metadata(
            engine_stash.get(Tables.TABLES_EF.value)
        )
        self.tables_gh = setup_metadata(
            engine_stash.get(Tables.TABLES_GH.value)
        )
        self.tables_ij = setup_metadata(
            engine_stash.get(Tables.TABLES_IJ.value)
        )
        self.tables_kl = setup_metadata(
            engine_stash.get(Tables.TABLES_KL.value)
        )
        self.tables_mn = setup_metadata(
            engine_stash.get(Tables.TABLES_MN.value)
        )
        self.tables_op = setup_metadata(
            engine_stash.get(Tables.TABLES_OP.value)
        )
        self.tables_qr = setup_metadata(
            engine_stash.get(Tables.TABLES_QR.value)
        )
        self.tables_st = setup_metadata(
            engine_stash.get(Tables.TABLES_ST.value)
        )
        self.tables_uv = setup_metadata(
            engine_stash.get(Tables.TABLES_UV.value)
        )
        self.tables_wx = setup_metadata(
            engine_stash.get(Tables.TABLES_WX.value)
        )
        self.tables_yz = setup_metadata(
            engine_stash.get(Tables.TABLES_YZ.value)
        )


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
