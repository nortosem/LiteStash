"""The LiteStash Attribue Module

#TODO doc
"""
from litestash.config import Valid

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


class EngineConf(Valid):
    """The Engine Config

    Provide the configuation to setup a database engine.
    """
    SQLITE = 'sqlite://'
    DIR_NAME = 'litestash'
    ECHO = True
    FUTURE = True
    NO_ECHO = False
    NO_FUTURE = False

    @staticmethod
    def sqlite() -> str:
        return f'{EngineConf.SQLITE.value}'

    @staticmethod
    def dirname() -> str:
        return f'{EngineConf.DIR_NAME.value}'

    @staticmethod
    def echo() -> str:
        return f'{EngineConf.ECHO.value}'

    @staticmethod
    def future() -> str:
        return f'{EngineConf.FUTURE.value}'

    @staticmethod
    def no_echo() -> str:
        return f'{EngineConf.NO_ECHO.value}'

    @staticmethod
    def no_future() -> str:
        return f'{EngineConf.NO_FUTURE.value}'
