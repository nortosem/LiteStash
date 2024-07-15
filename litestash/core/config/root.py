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
    MODEL = 'model_util'


class Config(Valid):
    """The config subpackage __all__"""
    LITESTASH = 'litestash_conf'
    ROOT = 'root'
    SCHEMA = 'schema_conf'
    TABLES = 'tables'


class Tables(Valid):
    """The tables subpackage__all__"""
    TABLES_03 = 'tables_03'
    TABLES_47 = 'tables_47'
    TABLES_89HU = 'tables_89hu'
    TABLES_AB = 'tables_ab'
    TABLES_CD = 'tables_cd'
    TABLES_EF = 'tables_ef'
    TABLES_GH = 'tables_gh'
    TABLES_IJ = 'tables_ij'
    TABLES_KL = 'tables_kl'
    TABLES_MN = 'tables_mn'
    TABLES_OP = 'tables_op'
    TABLES_QR = 'tables_qr'
    TABLES_ST = 'tables_st'
    TABLES_UV = 'tables_uv'
    TABLES_WX = 'tables_wx'
    TABLES_YZ = 'tables_yz'
