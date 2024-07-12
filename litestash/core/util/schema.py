"""The LiteStash Core Metadata Utilities

#TODO docs
"""
from litestash.core.config.schema import Names
from litestash.core.config.tables import Digitables
from litestash.core.config.tables import LowerTables
from litestash.core.config.tables import UpperTables
from litestash.core.config.litestash import Utils
from litestash.core.util.table import mk_columns
from litestash.core.util import prefix
from sqlalchemy import MetaData
from sqlalchemy import Table
from typing import Generator

def mk_table_names() -> Generator[str, None, None]:
    """Make all valid Table names

    Generate names for all tables in cache
    Return a generator.
    """
    for chars in (Digitables,LowerTables,UpperTables):
        for char in chars:
            yield f'{char.value}{Names.HASH.value}'


def mk_tables(metadata: MetaData) -> MetaData:
    """Make Tables

    Create all tables using preset columns and names.
    """
    for table_name in mk_table_names():
        Table(
            table_name,
            metadata,
            *(column for column in mk_columns())
        )
    return metadata


def get_db_name(char: bytes) -> bytes:
    """Find database for given char"""
    match char:
        case char if char in prefix.zf_db():
            return Names.ZFD.value
        case char if char in prefix.fn_db():
            return Names.FND.value
        case char if char in prefix.ael_db():
            return Names.AEL.value
        case char if char in prefix.fil_db():
            return Names.FIL.value
        case char if char in prefix.jml_db():
            return Names.JML.value
        case char if char in prefix.nrl_db():
            return Names.NRL.value
        case char if char in prefix.svl_db():
            return Names.SVL.value
        case char if char in prefix.wzl_db():
            return Names.WZL.value
        case char if char in prefix.aeu_db():
            return Names.AEU.value
        case char if char in prefix.fiu_db():
            return Names.FIU.value
        case char if char in prefix.jmu_db():
            return Names.JMU.value
        case char if char in prefix.nru_db():
            return Names.NRU.value
        case char if char in prefix.svu_db():
            return Names.SVU.value
        case char if char in prefix.wzu_db():
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
