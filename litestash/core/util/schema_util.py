"""LiteStash Schema Utilities

Provides functions for generating table names and creating SQLAlchemy tables
for the LiteStash key-value store.
"""
from sqlalchemy import Table
from sqlalchemy import MetaData
from typing import Generator
from litestash.core.util import prefix_util
from litestash.core.util import table_util
from litestash.core.config.root import Tables
from litestash.core.config.litestash_conf import Utils
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

def mk_table_names(db_name: str) -> Generator[str, None, None]:
    """
    Generates table names for the specified database.

    Args:
        db_name: The name of the database (e.g., "tables_03").

    Yields:
        str: The name of each table in the database.

    Raises:
        ValueError: If the database name is invalid.
    """
    match db_name:

        case db_name if db_name == Tables.TABLES_03.value:
            return table_util.get_tables_03()

        case db_name if db_name == Tables.TABLES_47.value:
            return table_util.get_tables_47()

        case db_name if db_name == Tables.TABLES_89HU.value:
            return table_util.get_tables_89hu()

        case db_name if db_name == Tables.TABLES_AB.value:
            return table_util.get_tables_ab()

        case db_name if db_name == Tables.TABLES_CD.value:
            return table_util.get_tables_cd()

        case db_name if db_name == Tables.TABLES_EF.value:
            return table_util.get_tables_ef()

        case db_name if db_name == Tables.TABLES_GH.value:
            return table_util.get_tables_gh()

        case db_name if db_name == Tables.TABLES_IJ.value:
            return table_util.get_tables_ij()

        case db_name if db_name == Tables.TABLES_KL.value:
            return table_util.get_tables_kl()

        case db_name if db_name == Tables.TABLES_MN.value:
            return table_util.get_tables_mn()

        case db_name if db_name == Tables.TABLES_OP.value:
            return table_util.get_tables_op()

        case db_name if db_name == Tables.TABLES_QR.value:
            return table_util.get_tables_qr()

        case db_name if db_name == Tables.TABLES_ST.value:
            return table_util.get_tables_st()

        case db_name if db_name == Tables.TABLES_UV.value:
            return table_util.get_tables_uv()

        case db_name if db_name == Tables.TABLES_WX.value:
            return table_util.get_tables_wx()

        case db_name if db_name == Tables.TABLES_YZ.value:
            return table_util.get_tables_yz()

        case _:
            raise ValueError(Utils.DB_NAME_ERROR.value)

def mk_tables(db_name: str, metadata: MetaData) -> MetaData:
    """
    Creates SQLAlchemy Table objects for the specified database.

    Args:
        db_name: The name of the database.
        metadata: The SQLAlchemy MetaData object to associate the tables with.

    Returns:
        MetaData: The updated MetaData object containing the created tables.
    """
    for table_name in mk_table_names(db_name):
        Table(
            table_name,
            metadata,
            *[column for column in mk_columns()]
        )
    return metadata


def get_db_name(char: str) -> str:
    """
    Determines the database name based on the given character.

    Args:
        char: The character to match against table prefixes.

    Returns:
        The name of the database corresponding to the character.

    Raises:
        ValueError: If the character doesn't match any valid table prefix.
    """
    match char:
        case char if char in prefix_util.tables_03():
            return Tables.TABLES_03.value

        case char if char in prefix_util.tables_47():
            return Tables.TABLES_47.value

        case char if char in prefix_util.tables_89hu():
            return Tables.TABLES_89HU.value

        case char if char in prefix_util.tables_ab():
            return Tables.TABLES_AB.value

        case char if char in prefix_util.tables_cd():
            return Tables.TABLES_CD.value

        case char if char in prefix_util.tables_ef():
            return Tables.TABLES_EF.value

        case char if char in prefix_util.tables_gh():
            return Tables.TABLES_GH.value

        case char if char in prefix_util.tables_ij():
            return Tables.TABLES_IJ.value

        case char if char in prefix_util.tables_kl():
            return Tables.TABLES_KL.value

        case char if char in prefix_util.tables_mn():
            return Tables.TABLES_MN.value

        case char if char in prefix_util.tables_op():
            return Tables.TABLES_OP.value

        case char if char in prefix_util.tables_qr():
            return Tables.TABLES_QR.value

        case char if char in prefix_util.tables_st():
            return Tables.TABLES_ST.value

        case char if char in prefix_util.tables_uv():
            return Tables.TABLES_UV.value

        case char if char in prefix_util.tables_wx():
            return Tables.TABLES_WX.value

        case char if char in prefix_util.tables_yz():
            return Tables.TABLES_YZ.value

        case _:
            raise ValueError(Utils.DB_NAME_ERROR.value)


def get_table_name(char: str) -> str:
    """
    Gets the table name based on the given character.

    Args:
        char: The character to match against table prefixes.

    Returns:
        The name of the table corresponding to the character.

    Raises:
        ValueError: If the character doesn't match any valid table prefix.
    """
    match char:
        case char if char in Tables03:
            return Tables03.get_table_name(char)

        case char if char in Tables47:
            return Tables47.get_table_name(char)

        case char if char in Tables89hu:
            return Tables89hu.get_table_name(char)

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

        case _:
            raise ValueError(Utils.DB_NAME_ERROR.value)
