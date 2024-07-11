"""The LiteStash Session Module

This module provide the core session module for creating a LiteStash.
Every instance of a LiteStash has a session attribute to access the sessions
associated with that instance.

This class is intended for use in a LiteStash:
    def __init__(self):
        self.session = Session
"""
from litestash.core.engine import Engine
from litestash.config import MetaSlots
from litestash.utils import StashSession
from litestash.utils import setup_sessions

class Session:
    """The Session Manager

    All databases have a dedicated session factory.
    The LiteStashSession class encapsulates the creation and access to these
    factories.
    #TODO: finish docs
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

    def __init__(self, engine: Engine):
        """Default init

        TODO: docs
        """
        self.zfd = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.ZFD.value)
            )
        )
        self.fnd = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.FND.value)
            )
        )
        self.ael = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.AEL.value)
            )
        )
        self.fil = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.FIL.value)
            )
        )
        self.jml = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.JML.value)
            )
        )
        self.nrl = StashSession(
            *setup_sessions(
                getattr(engine,
                MetaSlots.NRL.value)
            )
        )
        self.svl = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.SVL.value)
            )
        )
        self.wzl = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.WZL.value)
            )
        )
        self.aeu = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.AEU.value)
            )
        )
        self.fiu = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.FIU.value)
            )
        )
        self.jmu = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.JMU.value)
            )
        )
        self.nru = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.NRUvalue)
            )
        )
        self.svu = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.SVU.value)
            )
        )
        self.wzu = StashSession(
            *setup_sessions(
                getattr(engine, MetaSlots.WZU.value)
            )
        )

    def __iter__(self):
        """Iterator for all database session factories"""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """TODO"""
        pass

    def __str__(self):
        """TODO"""
        pass
