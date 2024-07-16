"""The LiteStash Core Metadata Utilities

#TODO docs
"""
from sqlalchemy import MetaData
from sqlalchemy import Table
from litestash.core.util import prefix_util
from litestash.core.util import table_util
from litestash.core.config.litestash_conf import Utils
from litestash.core.config.schema_conf import Names
from litestash.core.util.table_util import mk_columns
from litestash.core.config.tables.tables_03 import Tables03
from litestash.core.config.tables.tables_47 import Tables47
from litestash.core.config.tables.tables_89hu import Tables89hu
from litestash.core.config.tables.tables_ab import TablesAB
from litestash.core.config.tables.tables_cd import TablesCD
from litestash.core.config.tables.tables_ef import TablesEF
from litestash.core.config.tables.tables_gh import TablesGH
from litestash.core.config.tables.tables_ij import TablesIJ
from litestash.core.config.tables.tables_kl import TablesKL
from litestash.core.config.tables.tables_mn import TablesMN
from litestash.core.config.tables.tables_op import TablesOP
from litestash.core.config.tables.tables_qr import TablesQR
from litestash.core.config.tables.tables_st import TablesST
from litestash.core.config.tables.tables_uv import TablesUV
from litestash.core.config.tables.tables_wx import TablesWX
from litestash.core.config.tables.tables_yz import TablesYZ

def mk_table_names(db_name: str):
    """Make valid Table names

    Generate names for all tables in the given database name.
    Return a generator.
    """
    if db_name in Tables03:
        return table_util.get_tables_03()

    elif db_name in Tables47:
        return table_util.get_tables_47()

    elif db_name in Tables89hu:
        return table_util.get_tables_89hu()

    elif db_name in TablesAB :
        return table_util.get_tables_ab()

    elif db_name in TablesCD :
        return table_util.get_tables_cd()

    elif db_name in TablesEF :
        return table_util.get_tables_ef()

    elif db_name in TablesGH:
        return table_util.get_tables_gh()

    elif db_name in TablesIJ:
        return table_util.get_tables_ij()

    elif db_name in TablesKL:
        return table_util.get_tables_kl()

    elif db_name in TablesMN:
        return table_util.get_tables_mn()

    elif db_name in TablesOP:
        return table_util.get_tables_op()

    elif db_name in TablesQR:
        return table_util.get_tables_qr()

    elif db_name in TablesST:
        return table_util.get_tables_st()

    elif db_name in TablesUV:
        return table_util.get_tables_uv()

    elif db_name in TablesWX:
        return table_util.get_tables_wx()

    elif db_name in TablesYZ:
        return table_util.get_tables_yz()

def mk_tables(db_name: str, metadata: MetaData) -> MetaData:
    """Make Tables

    Create all tables using preset columns and names.
    """
    for table_name in mk_table_names(db_name):
        Table(
            table_name,
            metadata,
            *(column for column in mk_columns())
        )
    return metadata


def get_db_name(char: bytes) -> bytes:
    """Find database for given char"""
    match char:
        case char if char in prefix_util.tables_03():
            return Names.TABLES_03.value

        case char if char in prefix_util.tables_47():
            return Names.TABLES_47.value

        case char if char in prefix_util.tables_89hu():
            return Names.TABLES_89HU.value

        case char if char in prefix_util.tables_ab():
            return Names.TABLES_AB.value

        case char if char in prefix_util.tables_cd():
            return Names.TABLES_CD.value

        case char if char in prefix_util.tables_ef():
            return Names.TABLES_EF.value

        case char if char in prefix_util.tables_gh():
            return Names.TABLES_GH.value

        case char if char in prefix_util.tables_ij():
            return Names.TABLES_IJ.value

        case char if char in prefix_util.tables_kl():
            return Names.TABLES_KL.value

        case char if char in prefix_util.tables_mn():
            return Names.TABLES_MN.value

        case char if char in prefix_util.tables_op():
            return Names.TABLES_OP.value

        case char if char in prefix_util.tables_qr():
            return Names.TABLES_QR.value

        case char if char in prefix_util.tables_st():
            return Names.TABLES_ST.value

        case char if char in prefix_util.tables_uv():
            return Names.TABLES_UV.value

        case char if char in prefix_util.tables_wx():
            return Names.TABLES_WX.value

        case char if char in prefix_util.tables_yz():
            return Names.TABLES_YZ.value

        case _:
            raise ValueError(Utils.DB_NAME_ERROR.value)


def get_table_name(char: str) -> str:
    """Given a char get the table's name"""
    match char:
        case char if char in Tables03:
            return Tables03.get_table_name(char)

        case char if char in Tables47:
            return Tables47.get_table_name(char)

        case char if char in Tables89hu:
            return Tables47.get_table_name(char)

        case char if char in TablesAB :
            return TablesAB.get_table_name(char)

        case char if char in TablesCD :
            return TablesCD.get_table_name(char)

        case char if char in TablesEF :
            return TablesEF.get_table_name(char)

        case char if char in TablesGH:
            return TablesGH.get_table_name(char)

        case char if char in TablesIJ:
            return TablesIJ.get_table_name(char)

        case char if char in TablesKL:
            return TablesKL.get_table_name(char)

        case char if char in TablesMN:
            return TablesMN.get_table_name(char)

        case char if char in TablesOP:
            return TablesOP.get_table_name(char)

        case char if char in TablesQR:
            return TablesQR.get_table_name(char)

        case char if char in TablesST:
            return TablesST.get_table_name(char)

        case char if char in TablesUV:
            return TablesUV.get_table_name(char)

        case char if char in TablesWX:
            return TablesWX.get_table_name(char)

        case char if char in TablesYZ:
            return TablesYZ.get_table_name(char)
