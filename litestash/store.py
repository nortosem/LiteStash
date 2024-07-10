"""The Storage module

Define the LiteStash key-value database object.
LiteStash is a text key with JSON value key value store.
"""
from pathlib import Path
from collections import namedtuple
#from litestash.model import
from litestash.utils import mk_hash
from litestash.utils import setup_engine
from litestash.utils import hash_key
from litestash.utils import mk_tables
from litestash.config import Pragma
from litestash.config import StashSlots
from litestash.config import MetaSlots
from litestash.utils import StashEngine
from litestash.utils import StashMeta
from litestash.utils import StashSession
from litestash.config import EngineStash
from litestash.config import MetaStash
from litestash.config import SessionStash
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.schema import Metadata
from sqlalchemy.orm import Session
from pydantic import ValidationError

class LiteStash:
    """The LiteStash

    TODO
    """
    __slots__ = (StashSlots.DB.value,
                 StashSlots.ENGINE.value,
                 StashSlots.METADATA.value,
                 StashSlots.DB_SESSION.value
    )

    def __init__(self):
        """Initiate a new LiteStash

        Creates a new empty cache by default.
        """
        self.engine = LiteStashEngine()
        self.metadata = LiteStashMeta(self.engine)
        self.db_session = LiteStashSession(self.engine)


    def set(self, key: , value: ) -> None:
        """LiteStash Key Setter

        Add a new key to the database.
        If key already exists update the value.
        """
        pass

    def get(self, key: str) -> str | None:
        """LiteStash Get a value.

        Given a key return the value stored.
        """
        key_data = ''
        try:
            get_key = LiteStashData(key=key)
        except ValidationError as e:
            raise ValidationError(f"Invalid key: {e}")

        hashed_key = hash_key(key)



    def import(self, ) -> None:
        """"""
        pass

    def export(self, ) -> json:
        """"""
        pass

    def delete(self) -> bool:
        """LiteStash Delete

        Remove a give key and its value from the database.
        """
        pass

    def keys(self) -> Generator[tuple(str)]:
        """"""
        pass

    def values(self) -> Generator[tuple([str,str])]:
        """Return all values from database in a dictionary."""
        pass

    def exists(self, key: str) -> bool:
        """Check if key exists and return true if it does."""


    def clear(self) -> None:
        """Clear all entries from the database."""
        pass

    def __repr__(self) -> str:
        """"""""
        pass

    def __str__(self) -> str:
        """"""
        pass


class LiteStashEngine:
    """LiteStash Engine

    Each database file defines its own dedicated sqlalchemy engine.
    The LiteStashEngine class encapsualtes the setup and access to these engines.
    """
    __slots__ = (MetaSlots.ZFN.value,
                 MetaSlots.FNN.value,
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
        self.zfn = StashEngine(
            *setup_engine(MetaSlots.ZFN.value)
        )
        self.fnn = StashEngine(
            *setup_engine(MetaSlots.FNN.value)
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


class LiteStashMeta:
    """LiteStash Metadata

    Encapsulate metadata for all of the sqlite databases.
    This handles the setup of new metadata and enables access.
    """
    __slots__ = (MetaSlots.ZFN.value,
                 MetaSlots.FNN.value,
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

    def __init__(self, lite_stash_engine: LiteStashEngine):
        """LiteStash Metadata __init__

        Create metadata objects for all of the databases
        """
        self.zfn = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.ZFN.value
            )
        )
        self.fnn = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.FNN.value
            )
        )
        self.ael = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.AEN.value
            )
        )
        self.fil = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.FIL.value
            )
        )
        self.jml = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.JML.value
            )
        )
        self.nrl = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.NRL.value
            )
        )
        self.svl = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.SVL.value
            )
        )
        self.wzl = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.EZL.value
            )
        )
        self.aeu = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.AEU.value
            )
        )
        self.fiu = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.FIU.value
            )
        )
        self.jmu = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.JMU.value
            )
        )
        self.nru = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.NRU.value
            )
        )
        self.svu = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.SVU.value
            )
        )
        self.wzu = StashMeta(
            *setup_metadata(
                lite_stash_engine,
                MetaSlots.WZU.value
            )
        )

    def __iter__(self):
        """Iterator for all database metadata objects"""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """Metadata Official Representation

        Detailed Metadata Info for all the database tables.
        todo: with logger
        """
        repr_str += f'{StashSlots.METADATA.value}  Tables:\n'
        for prefix, metadata in self.metadata.items():
            repr_str += f'    {prefix}:\n'
            for table_name, table in metadata.tables.items():
                repr_str += f'      - {table_name}: {table.columns.keys()}\n'
        return repr_str

    def __str__(self):
        """Informal metadata string

        Basic String Representation of all Metadata objects.
        todo: for meh
        """
        metadata_str = ''
        for prefix, metadata in self.metadata.items():
            metadata_str += f'    {prefix}:\n'
            for table_name, table in metadata.tables.items():
                metadata_str += f'      - {table_name}: {table.columns.keys()}\n'
        return metadata_str


class LiteStashSession:
    """LiteStash Sessions

    All databases have a dedicated session factory.
    The LiteStashSession class encapsulates the creation and access to these
    factories.
    """
    __slots__ = (MetaSlots.ZFN.value,
                 MetaSlots.FNN.value,
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

    def __init__(self, lite_stash_engine: LiteStashEngine):
        """Default init

        TODO: docs
        """
        self.zfn = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.ZFN.value
            )
        )
        self.fnn = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.FNN.value
            )
        )
        self.ael = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.AEL.value
            )
        )
        self.fil = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.FIL.value
            )
        )
        self.jml = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.JML.value
            )
        )
        self.nrl = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.NRL.value
            )
        )
        self.svl = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.SVL.value
            )
        )
        self.wzl = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.WZL.value
            )
        )
        self.aeu = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.AEU.value
            )
        )
        self.fiu = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.FIU.value
            )
        )
        self.jmu = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.JMU.value
            )
        )
        self.nru = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.NRUvalue
            )
        )
        self.svu = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.SVU.value
            )
        )
        self.wzu = StashSession(
            *setup_sessions(
                lite_stash_engine,
                MetaSlots.WZU.value
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


@event.listens_for(Engine, "connect")
def pragma_setup(db_connection, connection):
    """Pragma setup

    Turn on WAL mode, normal sync, and foreign_keys.
    Leave the reat to sqlite defaults.
    """
    cursor = db_connection.cursor()
    cursor.execute(Pragma.journal_mode())
    cursor.execute(Pragma.synchronous())
    cursor.execute(Pragma.foreign_keys())
    cursor.close()
