"""LiteStash Schema Module

#TODO
"""
from litestash.core.engine import Engine
from litestash.config import MetaSlots
from litestash.config import StashSlots
from litestash.utils import StashMeta
from litestash.utils import setup_metadata
from litestash.utils import setup_fts

class Metadata:
    """LiteStash Metadata

    Encapsulate metadata for all of the sqlite databases.
    This handles the setup of new metadata and enables access.
    #TODO docs
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
        """LiteStash Metadata __init__

        Create metadata objects for all of the databases
        """
        self.zfd = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.ZFD.value)
                )
            )
        )
        self.fnd = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.FND.value)
                )
            )
        )
        self.ael = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.AEN.value)
                )
            )
        )
        self.fil = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.FIL.value)
                )
            )
        )
        self.jml = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.JML.value)
                )
            )
        )
        self.nrl = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.NRL.value)
                )
            )
        )
        self.svl = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.SVL.value)
                )
            )
        )
        self.wzl = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.EZL.value)
                )
            )
        )
        self.aeu = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.AEU.value)
                )
            )
        )
        self.fiu = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.FIU.value)
                )
            )
        )
        self.jmu = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.JMU.value)
                )
            )
        )
        self.nru = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.NRU.value)
                )
            )
        )
        self.svu = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.SVU.value)
                )
            )
        )
        self.wzu = StashMeta(
            *setup_fts(
                setup_metadata(
                    getattr(engine, MetaSlots.WZU.value)
                )
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
        repr_str = ''
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
                metadata_str += f'   - {table_name}: {table.columns.keys()}\n'
        return metadata_str
