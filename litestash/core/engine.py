"""LiteStash Engine Manager

This module provides engines for all SQLite databases used in the LiteStash
key-value store.
"""
from sqlalchemy import Engine as SQL_Engine
from litestash.core.config.root import Tables
from litestash.core.util.litestash_util import setup_engine

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


    def __init__(self):
        """Initializes the Engine object by creating SQLAlchemy engines for
        each database file.
        """
        self.tables_03 = setup_engine(Tables.TABLES_03.value)
        self.tables_47 = setup_engine(Tables.TABLES_47.value)
        self.tables_89hu = setup_engine(Tables.TABLES_89HU.value)
        self.tables_ab = setup_engine(Tables.TABLES_AB.value)
        self.tables_cd = setup_engine(Tables.TABLES_CD.value)
        self.tables_ef = setup_engine(Tables.TABLES_EF.value)
        self.tables_gh = setup_engine(Tables.TABLES_GH.value)
        self.tables_ij = setup_engine(Tables.TABLES_IJ.value)
        self.tables_kl = setup_engine(Tables.TABLES_KL.value)
        self.tables_mn = setup_engine(Tables.TABLES_MN.value)
        self.tables_op = setup_engine(Tables.TABLES_OP.value)
        self.tables_qr = setup_engine(Tables.TABLES_QR.value)
        self.tables_st = setup_engine(Tables.TABLES_ST.value)
        self.tables_uv = setup_engine(Tables.TABLES_UV.value)
        self.tables_wx = setup_engine(Tables.TABLES_WX.value)
        self.tables_yz = setup_engine(Tables.TABLES_YZ.value)


    def get(self, name: str) -> SQL_Engine:
        """Retrieves a specific SQLAlchemy engine by its name.

        Args:
            name: The name of the database (e.g., 'tables_03').

        Returns:
            The SQLAlchemy engine associated with the specified database.

        Raises:
            AttributeError: If no engine is found with the given name.
        """
        attribute = getattr(self, name)
        return attribute


    def __iter__(self):
        """Yields all engine attributes (name, engine tuples)."""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """"""
        pass

    def __str__(self):
        """"""
        pass
