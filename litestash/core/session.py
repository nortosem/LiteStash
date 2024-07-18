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
        self.tables_03 = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_03.value))
        )
        self.tables_47 = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_47.value))
        )
        self.tables_89hu = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_89HU.value))
        )
        self.tables_ab = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_AB.value))
        )
        self.tables_cd = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_CD.value))
        )
        self.tables_ef = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_EF.value))
        )
        self.tables_gh = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_GH.value))
        )
        self.tables_ij = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_IJ.value))
        )
        self.tables_kl = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_KL.value))
        )
        self.tables_mn = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_MN.value))
        )
        self.tables_op = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_OP.value))
        )
        self.tables_qr = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_QR.value))
        )
        self.tables_st = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_ST.value))
        )
        self.tables_uv = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_UV.value))
        )
        self.tables_wx = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_WX.value))
        )
        self.tables_yz = SessionAttributes(
            *setup_sessions(getattr(engine_stash, Tables.TABLES_YZ.value))
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
