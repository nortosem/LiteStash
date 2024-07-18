"""LiteStash Schema Module

#TODO
"""
from litestash.core.engine import Engine as EngineStash
from litestash.core.config.root import Tables
from litestash.core.config.litestash_conf import StashSlots
from litestash.core.util.litestash_util import setup_metadata
from litestash.core.util.litestash_util import MetaAttributes

class Metadata:
    """LiteStash Metadata

    Encapsulate metadata for all of the sqlite databases.
    This handles the setup of new metadata and enables access.
    #TODO docs
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
        """LiteStash Metadata __init__

        Create metadata objects for all of the databases
        """
        self.tables_03 = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_03.value))
        )

        self.tables_47 = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_47.value))
        )

        self.tables_89hu = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_89HU.value))
        )

        self.tables_ab = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_AB.value))
        )

        self.tables_cd = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_CD.value))
        )

        self.tables_ef = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_EF.value))
        )

        self.tables_gh = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_GH.value))
        )

        self.tables_ij = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_IJ.value))
        )

        self.tables_kl = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_KL.value))
        )

        self.tables_mn = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_MN.value))
        )

        self.tables_op = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_OP.value))
        )

        self.tables_qr = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_QR.value))
        )

        self.tables_st = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_ST.value))
        )

        self.tables_uv = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_UV.value))
        )

        self.tables_wx = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_WX.value))
        )

        self.tables_yz = MetaAttributes(
            *setup_metadata(getattr(engine_stash, Tables.TABLES_YZ.value))
        )

    def get(self, db_name):
        """Get metadata for a database"""
        attribute = getattr(self, db_name)
        return attribute.metadata

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
