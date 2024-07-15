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
    TABLES_AB = 'table_ab'
    TABLES_CD = 'table_cd'
    TABLES_EF = 'table_ef'
    TABLES_GH = 'table_gh'
    TABLES_IJ = 'table_ij'
    TABLES_KL = 'table_kl'
    TABLES_MN = 'table_mn'
    TABLES_OP = 'table_op'
    TABLES_QR = 'table_qr'
    TABLES_ST = 'table_st'
    TABLES_UV = 'table_uv'
    TABLES_WX = 'table_wx'
    TABLES_YZ = 'table_yz'
