"""Package Configuration

The config module enumerates the common required strings.
#from pydantic import ValidationError, validator
"""
from enum import Enum

class Valid(Enum):
    """Valid Root"""
    pass


class Core(Valid):
    """The Core __all__ modules"""
    CONFIG = 'config'
    UTIL = 'util'
    ENGINE = 'engine'
    SCHEMA = 'schema'
    SESSION = 'session'
