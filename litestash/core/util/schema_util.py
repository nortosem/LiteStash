"""The LiteStash Core Metadata Utilities

#TODO docs
"""
from sqlalchemy import MetaData
from sqlalchemy import Table

from litestash.core.config.litestash_conf import Utils
from litestash.core.config.schema_conf import MetaSlots
from litestash.core.config.schema_conf import Names
from litestash.core.config.tables.digits import Digitables
from litestash.core.config.tables.lowercase import LowerTables
from litestash.core.config.tables.uppercase import UpperTables

from litestash.core.util import prefix_util
from litestash.core.util.table_util import mk_columns
from litestash.core.util.table_util import create_zfd_tables
from litestash.core.util.table_util import create_fnd_tables
from litestash.core.util.table_util import create_ael_tables
from litestash.core.util.table_util import create_fil_tables
from litestash.core.util.table_util import create_jml_tables
from litestash.core.util.table_util import create_nrl_tables
from litestash.core.util.table_util import create_svl_tables
from litestash.core.util.table_util import create_wzl_tables
from litestash.core.util.table_util import create_aeu_tables
from litestash.core.util.table_util import create_fiu_tables
from litestash.core.util.table_util import create_jmu_tables
from litestash.core.util.table_util import create_nru_tables
from litestash.core.util.table_util import create_svu_tables
from litestash.core.util.table_util import create_wzu_tables


def mk_table_names(db_name: str):
    """Make valid Table names

    Generate names for all tables in the given database name.
    Return a generator.
    """
    if db_name == MetaSlots.ZFD.value:
        return create_zfd_tables()

    elif db_name == MetaSlots.FND.value:
        return create_fnd_tables()

    elif db_name == MetaSlots.AEL.value:
        return create_ael_tables()

    elif db_name == MetaSlots.FIL.value:
        return create_fil_tables()

    elif db_name == MetaSlots.JML.value:
        return create_jml_tables()

    elif db_name == MetaSlots.NRL.value:
        return create_nrl_tables()

    elif db_name == MetaSlots.SVL.value:
        return create_svl_tables()

    elif db_name == MetaSlots.WZL.value:
        return create_wzl_tables()

    elif db_name == MetaSlots.AEU.value:
        return create_aeu_tables()

    elif db_name == MetaSlots.FIU.value:
        return create_fiu_tables()

    elif db_name == MetaSlots.JMU.value:
        return create_jmu_tables()

    elif db_name == MetaSlots.NRU.value:
        return create_nru_tables()

    elif db_name == MetaSlots.SVU.value:
        return create_svu_tables()

    elif db_name == MetaSlots.WZU.value:
        return create_wzu_tables()


def mk_tables(db_name: str, metadata: MetaData) -> MetaData:
    """Make Tables

    Create all tables using preset columns and names.
    """
    for table_name in mk_table_names(db_name):
        print(f'tablename: {table_name}')
        Table(
            table_name,
            metadata,
            *(column for column in mk_columns())
        )
    return metadata


def get_db_name(char: bytes) -> bytes:
    """Find database for given char"""
    match char:
        case char if char in prefix_util.zf_db():
            return Names.ZFD.value
        case char if char in prefix_util.fn_db():
            return Names.FND.value
        case char if char in prefix_util.ael_db():
            return Names.AEL.value
        case char if char in prefix_util.fil_db():
            return Names.FIL.value
        case char if char in prefix_util.jml_db():
            return Names.JML.value
        case char if char in prefix_util.nrl_db():
            return Names.NRL.value
        case char if char in prefix_util.svl_db():
            return Names.SVL.value
        case char if char in prefix_util.wzl_db():
            return Names.WZL.value
        case char if char in prefix_util.aeu_db():
            return Names.AEU.value
        case char if char in prefix_util.fiu_db():
            return Names.FIU.value
        case char if char in prefix_util.jmu_db():
            return Names.JMU.value
        case char if char in prefix_util.nru_db():
            return Names.NRU.value
        case char if char in prefix_util.svu_db():
            return Names.SVU.value
        case char if char in prefix_util.wzu_db():
            return Names.WZU.value
        case _:
            raise ValueError(Utils.DB_NAME_ERROR.value)


def get_table_name(char: bytes) -> str:
    """Given a char get the table's name"""
    if char in Digitables:
        return Digitables.get_table_name(char)
    elif char in LowerTables:
        return LowerTables.get_table_name(char)
    elif char in UpperTables:
        return UpperTables.get_table_name(char)
    else:
        raise ValueError("NO!")
