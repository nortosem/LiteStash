"""The


"""
from litestash.core.config.root import Tables
from litestash.core.util.litestash_util import setup_engine
from litestash.core.util.litestash_util import EngineAttributes
from sqlalchemy import Engine as SQL_Engine

class Engine:
    """LiteStash Engine

    Each database file defines its own dedicated sqlalchemy engine.
    The LiteStashEngine class encapsulates the setup
    and access to these engines.
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
        """Default DB & Engine setup

        Each database stored as name, engine.
        """
        self.tables_03 = EngineAttributes(
            *setup_engine(Tables.TABLES_03.value)
        )
        self.tables_47 = EngineAttributes(
            *setup_engine(Tables.TABLES_47.value)
        )
        self.tables_89hu = EngineAttributes(
            *setup_engine(Tables.TABLES_89HU.value)
        )
        self.tables_ab = EngineAttributes(
            *setup_engine(Tables.TABLES_AB.value)
        )
        self.tables_cd = EngineAttributes(
            *setup_engine(Tables.TABLES_CD.value)
        )
        self.tables_ef = EngineAttributes(
            *setup_engine(Tables.TABLES_EF.value)
        )
        self.tables_gh = EngineAttributes(
            *setup_engine(Tables.TABLES_GH.value)
        )
        self.tables_ij = EngineAttributes(
            *setup_engine(Tables.TABLES_IJ.value)
        )
        self.tables_kl = EngineAttributes(
            *setup_engine(Tables.TABLES_KL.value)
        )
        self.tables_mn = EngineAttributes(
            *setup_engine(Tables.TABLES_MN.value)
        )
        self.tables_op = EngineAttributes(
            *setup_engine(Tables.TABLES_OP.value)
        )
        self.tables_qr = EngineAttributes(
            *setup_engine(Tables.TABLES_QR.value)
        )
        self.tables_st = EngineAttributes(
            *setup_engine(Tables.TABLES_ST.value)
        )
        self.tables_uv = EngineAttributes(
            *setup_engine(Tables.TABLES_UV.value)
        )
        self.tables_wx = EngineAttributes(
            *setup_engine(Tables.TABLES_WX.value)
        )
        self.tables_yz = EngineAttributes(
            *setup_engine(Tables.TABLES_YZ.value)
        )


    def get(self, name: str) -> SQL_Engine:
        """Engine Getter

        Args:
            name (str): The name of the engine to get
        Result:
            engine (Engine): Return the sqlalchemy engine
        """
        attribute = getattr(self, name)
        return attribute.engine

    def __iter__(self):
        """Iterator for all database engines"""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """"""
        pass

    def __str__(self):
        """"""
        pass
