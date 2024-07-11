"""The


"""
from litestash.config import MetaSlots
from litestash.utils import setup_engine
from litestash.utils import StashEngine

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
        self.zfd = StashEngine(
            *setup_engine(MetaSlots.ZFD.value)
        )
        self.fnd = StashEngine(
            *setup_engine(MetaSlots.FND.value)
        )
        self.ael = StashEngine(
            *setup_engine(MetaSlots.AEL.value)
        )
        self.fil = StashEngine(
            *setup_engine(MetaSlots.FIL.value)
        )
        self.jml = StashEngine(
            *setup_engine(MetaSlots.JML.value)
        )
        self.nrl = StashEngine(
            *setup_engine(MetaSlots.NRL.value)
        )
        self.svl = StashEngine(
            *setup_engine(MetaSlots.SVL.value)
        )
        self.wzl = StashEngine(
            *setup_engine(MetaSlots.WZL.value)
        )
        self.aeu = StashEngine(
            *setup_engine(MetaSlots.AEU.value)
        )
        self.fiu = StashEngine(
            *setup_engine(MetaSlots.FIU.value)
        )
        self.jmu = StashEngine(
            *setup_engine(MetaSlots.JMU.value)
        )
        self.nru = StashEngine(
            *setup_engine(MetaSlots.NRU.value)
        )
        self.svu = StashEngine(
            *setup_engine(MetaSlots.SVU.value)
        )
        self.wzu = StashEngine(
            *setup_engine(MetaSlots.WFU.value)
        )


    def __iter__(self):
        """Iterator for all database engines"""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """"""
        pass

    def __str__(self):
        """"""
        pass
