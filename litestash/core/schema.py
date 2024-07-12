"""LiteStash Schema Module

#TODO
"""
from litestash.core.engine import Engine
from litestash.core.config.schema_conf import MetaSlots
from litestash.core.config.litestash_conf StashSlots
from litestash.core.util.litestash_util import setup_metadata
from litestash.core.util.litestash_util import MetaAttributes

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
        self.zfd = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.ZFD.value)
            )
        )
        self.fnd = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.FND.value)
            )
        )
        self.ael = MetaAttributes(
            *setup_metadata(
               getattr(engine, MetaSlots.AEN.value)
            )
        )
        self.fil = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.FIL.value)
            )
        )
        self.jml = MetaAttributes(
            *setup_metadata(
               getattr(engine, MetaSlots.JML.value)
            )
        )
        self.nrl = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.NRL.value)
            )
        )
        self.svl = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.SVL.value)
            )
        )
        self.wzl = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.EZL.value)
            )
        )
        self.aeu = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.AEU.value)
            )
        )
        self.fiu = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.FIU.value)
            )
        )
        self.jmu = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.JMU.value)
            )
        )
        self.nru = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.NRU.value)
            )
        )
        self.svu = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.SVU.value)
            )
        )
        self.wzu = MetaAttributes(
            *setup_metadata(
                getattr(engine, MetaSlots.WZU.value)
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
