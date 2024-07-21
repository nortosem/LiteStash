"""LiteStash Session Manager

Creates and provides access to session factories for each database in
LiteStash.
"""
from litestash.core.engine import Engine as EngineStash
from litestash.core.config.root import Tables
from litestash.core.util.litestash_util import setup_sessions

class Session:
    """LiteStash Session Class

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
        """Initializes session factories for each database.

        Args:
            engine_stash (EngineStash): An instance of the `EngineStash` class
            containing the database engines.
        """
        self.tables_03 = setup_sessions(
            engine_stash.get(Tables.TABLES_03.value)
        )
        self.tables_47 = setup_sessions(
            engine_stash.get(Tables.TABLES_47.value)
        )
        self.tables_89hu = setup_sessions(
            engine_stash.get(Tables.TABLES_89HU.value)
        )
        self.tables_ab = setup_sessions(
            engine_stash.get(Tables.TABLES_AB.value)
        )
        self.tables_cd = setup_sessions(
            engine_stash.get(Tables.TABLES_CD.value)
        )
        self.tables_ef = setup_sessions(
            engine_stash.get(Tables.TABLES_EF.value)
        )
        self.tables_gh = setup_sessions(
            engine_stash.get(Tables.TABLES_GH.value)
        )
        self.tables_ij = setup_sessions(
            engine_stash.get(Tables.TABLES_IJ.value)
        )
        self.tables_kl = setup_sessions(
            engine_stash.get(Tables.TABLES_KL.value)
        )
        self.tables_mn = setup_sessions(
            engine_stash.get(Tables.TABLES_MN.value)
        )
        self.tables_op = setup_sessions(
            engine_stash.get(Tables.TABLES_OP.value)
        )
        self.tables_qr = setup_sessions(
            engine_stash.get(Tables.TABLES_QR.value)
        )
        self.tables_st = setup_sessions(
            engine_stash.get(Tables.TABLES_ST.value)
        )
        self.tables_uv = setup_sessions(
            engine_stash.get(Tables.TABLES_UV.value)
        )
        self.tables_wx = setup_sessions(
            engine_stash.get(Tables.TABLES_WX.value)
        )
        self.tables_yz = setup_sessions(
            engine_stash.get(Tables.TABLES_YZ.value)
        )


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
