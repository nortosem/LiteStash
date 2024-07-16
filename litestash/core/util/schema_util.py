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
        return table_util.create_tables_03()

    elif db_name in Tables47:
        return create_tables_47()

    elif db_name in Tables89hu:
        return create_tables_89hu()

    elif db_name in TablesAB :
        return create_tables_ab()

    elif db_name in TablesCD :
        return create_tables_cd()

    elif db_name in TablesEF :
        return create_tables_ef()

    elif db_name in TablesGH:
        return create_tables_gh()

    elif db_name in TablesIJ:
        return create_tables_ij()

    elif db_name in TablesKL:
        return create_tables_kl()

    elif db_name in TablesMN:
        return create_tables_mn()

    elif db_name in TablesOP:
        return create_tables_op()

    elif db_name in TablesQR:
        return create_tables_qr()

    elif db_name in TablesST:
        return create_tables_st()

    elif db_name in TablesUV:
        return create_tables_uv()

    elif db_name in TablesWX:
        return create_tables_wx()

    elif db_name in TablesYZ:
        return create_tables_yz()

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
    if char in Tables03:
        return create_tables_03()

    elif char in Tables47:
        return create_tables_47()

    elif char in Tables89hu:
        return create_tables_89hu()

    elif char in TablesAB :
        return create_tables_ab()

    elif char in TablesCD :
        return create_tables_cd()

    elif char in TablesEF :
        return create_tables_ef()

    elif char in TablesGH:
        return create_tables_gh()

    elif char in TablesIJ:
        return create_tables_ij()

    elif char in TablesKL:
        return create_tables_kl()

    elif char in TablesMN:
        return create_tables_mn()

    elif char in TablesOP:
        return create_tables_op()

    elif char in TablesQR:
        return create_tables_qr()

    elif char in TablesST:
        return create_tables_st()

    elif char in TablesUV:
        return create_tables_uv()

    elif char in TablesWX:
        return create_tables_wx()

    elif char in TablesYZ:
        return create_tables_yz()

