"""The Tables subpackage

Modules:
    Pull in the names of all databases and the access enumerations for the
    tables in each database.
"""
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
from litestash.core.config.root import Tables

__all__ = [
    Tables.TABLES_03.value,
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
    Tables.TABLES_YZ.value,
]
