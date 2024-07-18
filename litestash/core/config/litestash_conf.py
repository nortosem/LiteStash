"""The LiteStash Attribue Module

#TODO doc
"""
from litestash.core.config.root import Valid

class DataScheme(Valid):
    """LiteStashData Scheme

    Define the config and schema for the data transfer object.
    """
    TITLE = 'Data'
    DESCRIPTION = 'The key name and JSON data for the given key.'
    MIN_LENGTH = 4
    MAX_LENGTH = 41
    FORBID_EXTRA = 'forbid'


class StashSlots(Valid):
    """all slots for the LiteStash"""
    ENGINE = 'engine'
    METADATA = 'metadata'
    DB_SESSION = 'db_session'


class Utils(Valid):
    """Defaults for util functions

    SIZE (int): digest_size for hash_key
    """
    SIZE = 17
    DB_NAME_ERROR = 'Invalid character'


class EngineAttr(Valid):
    """The namedtuple config for all engine attributes of a LiteStash"""
    TYPE_NAME = 'EngineAttr'
    DB_NAME = 'db_name'
    ENGINE = 'engine'
    DOC = '''Defines a named tuple for tuple returned by utils.setup_engine.
    Attributes:
        db_name (str): name of the database for this engine
        engine (Engine): the sqlalchemy engine itself
    '''
    VALUE_ERROR = 'No such engine found'


class MetaAttr(Valid):
    """The namedtuple config for all metadata attributes of a LiteStash"""
    TYPE_NAME = 'MetaAttr'
    DB_NAME = f'{EngineAttr.DB_NAME.value}'
    METADATA = 'metadata'
    DOC = '''todo'''


class SessionAttr(Valid):
    """The namedtuple config for all session attribues of a LiteStash """
    TYPE_NAME = 'SessionAttr'
    DB_NAME = f'{EngineAttr.DB_NAME.value}'
    SESSION = 'session'
    VALUE_ERROR = 'Invalid database: no tables found'
    DOC = '''todo'''


class TimeAttr(Valid):
    """The namedtuple config for the unix timestamp from datetime"""
    TYPE_NAME = 'GetTime'
    TIMESTAMP = 'timestamp'
    MICROSECOND = 'microsecond'
    VALUE_ERROR = 'Valid time in integer only'
    DOC = '''todo'''


class EngineConf(Valid):
    """The Engine Config

    Provide the configuation to setup a database engine.
    """
    SQLITE = 'sqlite:///'
    DIR_NAME = 'data'
    ECHO = True
    FUTURE = True
    NO_ECHO = False
    NO_FUTURE = False
    POOL_SIZE = 50
    MAX_OVERFLOW = 10


    @staticmethod
    def sqlite() -> str:
        return EngineConf.SQLITE.value

    @staticmethod
    def dirname() -> str:
        return EngineConf.DIR_NAME.value

    @staticmethod
    def echo() -> str:
        return EngineConf.ECHO.value

    @staticmethod
    def future() -> str:
        return EngineConf.FUTURE.value

    @staticmethod
    def no_echo() -> str:
        return EngineConf.NO_ECHO.value

    @staticmethod
    def no_future() -> str:
        return EngineConf.NO_FUTURE.value

    @staticmethod
    def pool_size() -> int:
        return EngineConf.POOL_SIZE.value

    @staticmethod
    def max_overflow() -> int:
        return EngineConf.MAX_OVERFLOW.value
