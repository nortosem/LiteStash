"""The


"""
from litestash.core.config.schema_conf import MetaSlots
from litestash.core.util.litestash_util import setup_engine
from litestash.core.util.litestash_util import EngineAttributes
from sqlalchemy import Engine as SQL_Engine

class Engine:
    """LiteStash Engine

    Each database file defines its own dedicated sqlalchemy engine.
    The LiteStashEngine class encapsulates the setup
    and access to these engines.
    """
    __slots__ = (MetaSlots.ZFD.value,
                 MetaSlots.FND.value,
                 MetaSlots.AEL.value,
                 MetaSlots.FIL.value,
                 MetaSlots.JML.value,
                 MetaSlots.NRL.value,
                 MetaSlots.SVL.value,
                 MetaSlots.WZL.value,
                 MetaSlots.AEU.value,
                 MetaSlots.FIU.value,
                 MetaSlots.JMU.value,
                 MetaSlots.NRU.value,
                 MetaSlots.SVU.value,
                 MetaSlots.WZU.value,
                )


    def __init__(self):
        """Default DB & Engine setup

        Each database stored as name, engine.
        """
        self.zfd = EngineAttributes(
            *setup_engine(MetaSlots.ZFD.value)
        )
        self.fnd = EngineAttributes(
            *setup_engine(MetaSlots.FND.value)
        )
        self.ael = EngineAttributes(
            *setup_engine(MetaSlots.AEL.value)
        )
        self.fil = EngineAttributes(
            *setup_engine(MetaSlots.FIL.value)
        )
        self.jml = EngineAttributes(
            *setup_engine(MetaSlots.JML.value)
        )
        self.nrl = EngineAttributes(
            *setup_engine(MetaSlots.NRL.value)
        )
        self.svl = EngineAttributes(
            *setup_engine(MetaSlots.SVL.value)
        )
        self.wzl = EngineAttributes(
            *setup_engine(MetaSlots.WZL.value)
        )
        self.aeu = EngineAttributes(
            *setup_engine(MetaSlots.AEU.value)
        )
        self.fiu = EngineAttributes(
            *setup_engine(MetaSlots.FIU.value)
        )
        self.jmu = EngineAttributes(
            *setup_engine(MetaSlots.JMU.value)
        )
        self.nru = EngineAttributes(
            *setup_engine(MetaSlots.NRU.value)
        )
        self.svu = EngineAttributes(
            *setup_engine(MetaSlots.SVU.value)
        )
        self.wzu = EngineAttributes(
            *setup_engine(MetaSlots.WZU.value)
        )


    def get(self, name: str) -> SQL_Engine:
        """Given a name return the engine"""
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
