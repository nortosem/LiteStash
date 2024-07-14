"""Package Configuration

The config module enumerates the common required strings.
#from pydantic import ValidationError, validator
"""
from enum import Enum

class Valid(Enum):
    """Valid Root"""
    pass


class Main(Valid):
    """The main __all__"""
    CORE = 'core'
    DATA = 'LiteStashData'
    STORE = 'LiteStashStore'
    STASH = 'LiteStash'


class Core(Valid):
    """The core __all__"""
    CONFIG = 'config'
    UTIL = 'util'
    ENGINE = 'engine'
    SCHEMA = 'schema'
    SESSION = 'session'


class Util(Valid):
    """The util __all__"""
    LITESTASH = 'litestash_util'
    PREFIX = 'prefix_util'
    SCHEMA = 'schema_util'
    TABLE = 'table_util'


class Config(Valid):
    """The config subpackage __all__"""
    LITESTASH = 'litestash_conf'
    ROOT = 'root'
    SCHEMA = 'schema_conf'
    TABLES = 'tables'


class Tables(Valid):
    """The tables subpackage__all__"""
    TABLES_03 = 'table_03'
    TABLES_47 = 'table_47'
    TABLES_89HU = 'table_89hu'
    TABLES_AB = 'table_aB'
    TABLES_CD = 'table_cD'
    TABLES_EF = 'table_eF'
    TABLES_GH = 'table_gH'
    TABLES_IJ = 'table_iJ'
    TABLES_KL = 'table_kL'
    TABLES_MN = 'table_mN'
    TABLES_OP = 'table_oP'
    TABLES_QR = 'table_qR'
    TABLES_ST = 'table_sT'
    TABLES_UV = 'table_uV'
    TABLES_WX = 'table_wX'
    TABLES_YZ = 'table_yZ'
