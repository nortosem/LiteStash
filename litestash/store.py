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
from litestash.confim import EngineStash
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
        self.metadata = build_db(self.engine)
        self.db_session = LiteStashSession()

    def build_db(self, engine: LiteStashEngine):
        """Initiate all database files.

        Arg:
            engine (LiteStashEngine): The engines for the stash
        """
        return(LiteStashMeta(engine))

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

    def __init__(self, engine_stash: LiteStashEngine):
        """LiteStash Metadata __init__

        Create fresh empty metadata objects for all of the databases
        """
        self.zfn = bond_to_engine(engine_stash.get_engine(MetaSlots.ZFN.value))
        self.fnn = bond_to_engine(engine_stash.get_engine(MetaSlots.FNN.value))
        self.ael = bond_to_engine(engine_stash.get_engine(MetaSlots.AEN.value))
        self.fil = bond_to_engine(engine_stash.get_engine(MetaSlots.FIL.value))
        self.jml = bond_to_engine(engine_stash.get_engine(MetaSlots.JML.value))
        self.nrl = bond_to_engine(engine_stash.get_engine(MetaSlots.NRL.value))
        self.svl = bond_to_engine(engine_stash.get_engine(MetaSlots.SVL.value))
        self.wzl = bond_to_engine(engine_stash.get_engine(MetaSlots.EZL.value))
        self.aeu = bond_to_engine(engine_stash.get_engine(MetaSlots.AEU.value))
        self.fiu = bond_to_engine(engine_stash.get_engine(MetaSlots.FIU.value))
        self.jmu = bond_to_engine(engine_stash.get_engine(MetaSlots.JMU.value))
        self.nru = bond_to_engine(engine_stash.get_engine(MetaSlots.NRU.value))
        self.svu = bond_to_engine(engine_stash.get_engine(MetaSlots.SVU.value))
        self.wzu = bond_to_engine(engine_stash.get_engine(MetaSlots.WZU.value))

    def bond_to_engine(self, engine: Engine) -> Metadata:
        """Bond with specific engine

        Used to specify a bind to an engine and create tables for that engine.

        Args (Engine): The engine to create tables for
        """
        metadata = Metadata()
        metadata = mk_tables(metadata)
        metadata.create_all(bind=engine, checkfirst=True)
        return metadata

    def __iter__(self):
        """Iterator for all database metadata"""
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
        """Default DB & Engine setup"""
        StashEngine = namedtuple(EngineStash.TYPE_NAME.value,
                                 [EngineStash.DB_NAME.value,
                                  EngineStash.ENGINE.value
                                 ]
                                )
        self.zfn = StashEngine(*setup_engine(MetaSlots.ZFN.value))
        self.fnn = StashEngine(*setup_engine(MetaSlots.FNN.value))
        self.ael = StashEngine(*setup_engine(MetaSlots.AEL.value))
        self.fil = StashEngine(*setup_engine(MetaSlots.FIL.value))
        self.jml = StashEngine(*setup_engine(MetaSlots.JML.value))
        self.nrl = StashEngine(*setup_engine(MetaSlots.NRL.value))
        self.svl = StashEngine(*setup_engine(MetaSlots.SVL.value))
        self.wzl = StashEngine(*setup_engine(MetaSlots.WZL.value))
        self.aeu = StashEngine(*setup_engine(MetaSlots.AEU.value))
        self.fiu = StashEngine(*setup_engine(MetaSlots.FIU.value))
        self.jmu = StashEngine(*setup_engine(MetaSlots.JMU.value))
        self.nru = StashEngine(*setup_engine(MetaSlots.NRU.value))
        self.svu = StashEngine(*setup_engine(MetaSlots.SVU.value))
        self.wzu = StashEngine(*setup_engine(MetaSlots.WFU.value))


    def get_engine(self, name: str):
        """Get DB Engine by name

        Args:
            name (str): database filename & db engine
        """
        if hasattr(self, name):
            return getattr(getattr(self, name),
                            EngineStash.ENGINE.value
                            )
        else:
            raise ValueError(f'{EngineStash.VALUE_ERROR.value}')


    def __iter__(self):
        """Iterator for all database engines"""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """"""
        pass

    def __str__(self):
        """"""
        pass


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

    def __init__(self, engine_stash: LiteStashEngine):
        """Default init

        Given an instance of the LiteStashEngine match
        all
        """
        self.zfn =
        self.fnn = getattr(engine_stash, MetaSlots.FNN.value)
        self.ael = getattr(engine_stash, MetaSlots.AEL.value)
        self.fil = getattr(engine_stash, MetaSlots.FIL.value)
        self.jml = getattr(engine_stash, MetaSlots.JML.value)
        self.nrl = getattr(engine_stash, MetaSlots.NRL.value)
        self.svl = getattr(engine_stash, MetaSlots.SVL.value)
        self.wzl = getattr(engine_stash, MetaSlots.WZL.value)
        self.aeu = getattr(engine_stash, MetaSlots.AEU.value)
        self.fiu = getattr(engine_stash, MetaSlots.FIU.value)
        self.jmu = getattr(engine_stash, MetaSlots.JMU.value)
        self.nru = getattr(engine_stash, MetaSlots.NRU.value)
        self.svu = getattr(engine_stash, MetaSlots.SVU.value)
        self.wzu = getattr(engine_stash, MetaSlots.WFU.value)


    def mk_session(self, engine_stash: LiteStashEngine) -> Session:
        """Make a sesssion

        Given a LiteStashEngine instance make a session factory
        for each database engine.
        """
        getattr(engine_stash, MetaSlots.ZFN.value)

    def __iter__(self):
        """Iterator for all database session factories"""
        yield from (getattr(self, slot) for slot in self.__slots__)

    def __repr__(self):
        """"""
        pass

    def __str__(self):
        """"""
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
