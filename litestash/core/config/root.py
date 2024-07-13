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
    DIGITS = 'digits'
    LOWER = 'lowercase'
    UPPER = 'uppercase'
