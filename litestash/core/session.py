"""The LiteStash Session Module

This module provide the core session module for creating a LiteStash.
Every instance of a LiteStash has a session attribute to access the sessions
associated with that instance.

This class is intended for use in a LiteStash:
    def __init__(self):
        self.session = Session
"""
from litestash.core.engine import Engine
from litestash.core.config.schema_conf import MetaSlots
from litestash.core.util.litestash_util import SessionAttributes
from litestash.core.util.litestash_util import setup_sessions

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
        self.zfd = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.ZFD.value)
            )
        )
        self.fnd = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.FND.value)
            )
        )
        self.ael = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.AEL.value)
            )
        )
        self.fil = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.FIL.value)
            )
        )
        self.jml = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.JML.value)
            )
        )
        self.nrl = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.NRL.value)
            )
        )
        self.svl = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.SVL.value)
            )
        )
        self.wzl = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.WZL.value)
            )
        )
        self.aeu = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.AEU.value)
            )
        )
        self.fiu = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.FIU.value)
            )
        )
        self.jmu = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.JMU.value)
            )
        )
        self.nru = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.NRU.value)
            )
        )
        self.svu = SessionAttributes(
            *setup_sessions(
                getattr(engine, MetaSlots.SVU.value)
            )
        )
        self.wzu = SessionAttributes(
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
