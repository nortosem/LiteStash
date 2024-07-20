"""The LiteStash Session Module

This module provide the core session module for creating a LiteStash.
Every instance of a LiteStash has a session attribute to access the sessions
associated with that instance.

This class is intended for use in a LiteStash:
    def __init__(self):
        self.session = Session
"""
from litestash.core.engine import Engine as EngineStash
from litestash.core.config.root import Tables
from litestash.core.util.litestash_util import SessionAttributes
from litestash.core.util.litestash_util import setup_sessions

class Session:
    """The Session Manager

    All databases have a dedicated session factory.
    The LiteStashSession class encapsulates the creation and access to these
    factories.
    #TODO: finish docs
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
        """Default init

        TODO: docs
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
        """Get a session factory for the database name"""
        attribute = getattr(self, db_name)
        return attribute.session

    def __iter__(self):
        """Iterator for all database session factories"""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """TODO"""
        pass

    def __str__(self):
        """TODO"""
        pass
