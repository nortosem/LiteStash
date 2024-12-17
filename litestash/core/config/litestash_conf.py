"""LiteStash Configuration Module

Provides core configuration for the LiteStash key-value store.

This module defines classes and constants for configuring various aspects of
LiteStash, including:

- **DataScheme:**  Constraints and options for key-value data validation.
- **StashSlots:** Attribute names used in the main `LiteStash` class.
- **Utils:**  Default values and error messages for utility functions.
- **EngineAttr/MetaAttr/SessionAttr/TimeAttr:** Named tuple structures for
organizing engine, metadata, session, and time-related information.
- **EngineConf:** Configuration parameters for setting up the SQLAlchemy engine.
"""
from litestash.core.config.root import Valid


class Key(Valid):
    """Key Error

    Configuration strings for key errors.
    """
    LOG_ERROR = 'Expected a string, but got incorrect type: '
    TYPE_ERROR = 'Key must be a string'

    @staticmethod
    def log_error():
        return f'{Key.LOG_ERROR.value}'

    @staticmethod
    def type_error():
        return f'{Key.TYPE_ERROR.value}'


class MkHash(Valid):
    """mk_hash digest

    Configuration strings for logging and errors of the mk_hash function.
    """
    NONE_LOG = ''
    VALUE_ERROR = ''
    BYTES_LOG = ''
    BYTES_ERROR = ''
    DIGEST_LOG = ''


class DigestKey(Valid):
    """Digest Key


    """
    DIGEST_KEY_LOG = ''
    DIGETS_KEY_ERROR = ''

class StashError(Valid):
    """StashError

    Configuriaton of LiteStash error strings.
    """
    SET_TYPE = 'value must be JSON serializable'
    KEY_TYPE = 'Key must be a string'


class DataScheme(Valid):
    """LiteStashData Scheme

    Define the config and schema for the data transfer object.
    """
    TITLE = 'Data'
    DESCRIPTION = 'The key name and JSON data for the given key.'
    MIN_LENGTH = 3
    MAX_LENGTH = 999
    FORBID_EXTRA = 'forbid'
    FROM_ATTRIBUTES = False


class StashSlots(Valid):
    """all slots for the LiteStash"""
    ENGINE = 'engine'
    METADATA = 'metadata'
    DB_SESSION = 'db_session'

    @staticmethod
    def slots():
        return tuple(slot.value for slot in StashSlots)

class Utils(Valid):
    """Defaults for util functions

    SIZE (int): digest_size for hash_key
    """
    SIZE = 41
    DB_NAME_ERROR = 'Invalid character'
    INVALID_CHAR_LENGTH = 'Incorrect number characters'


class EngineAttr(Valid):
    """The namedtuple config for all engine attributes of a LiteStash"""
    TYPE_NAME = 'EngineAttributes'
    DB_NAME = 'db_name'
    ENGINE = 'engine'
    DOC = '''Defines a namedtuple for tuple returned by utils.setup_engine.
    Attributes:
        db_name (str): name of the database for this engine
        engine (Engine): the sqlalchemy engine object
    '''
    VALUE_ERROR = 'No such engine found'


class MetaAttr(Valid):
    """The namedtuple config for all metadata attributes of a LiteStash"""
    TYPE_NAME = 'MetaAttributes'
    DB_NAME = f'{EngineAttr.DB_NAME.value}'
    METADATA = 'metadata'
    DOC = '''Defines a namedtuple for all metadata attributes of a LiteStash.
    Attributes:
        db_name (str): name of the database for this metadata
        metadata (Metadata): the sqlalchemy metadata object
    '''


class SessionAttr(Valid):
    """The namedtuple config for all session attribues of a LiteStash """
    TYPE_NAME = 'SessionAttributes'
    DB_NAME = f'{EngineAttr.DB_NAME.value}'
    SESSION = 'session'
    VALUE_ERROR = 'Invalid database: no tables found'
    DOC = '''Defines a namedtuple for all session attributes of a LiteStash.
    Attributes:
        db_name (str): nameo fthe database for this session
        session (Session): the sqlalchemy session object
    '''


class EngineConf(Valid):
    """The Engine Config

    Provide the configuation to setup a database engine.
    """
    SQLITE = 'sqlite:///'
    DIR_NAME = 'data'#/mnt/ram/data'
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 128
    ECHO = True
    FUTURE = True
    NO_ECHO = False
    NO_FUTURE = False
    POOL_SIZE = 50
    MAX_OVERFLOW = 10
    DB_NAME_SPACE = 'No spaces permitted in database name'
    DB_NAME_ASCII = 'Database name permits only ASCII characters'
    DB_NAME_LENGTH = 'Invalid database name length provided'
    DIR_NOT_FOUND = 'No such file or directory'
    NO_DIR_ACCESS = 'Directory inaccessible'
    DIR_PATH_ERROR = 'Path Exception'


    @staticmethod
    def sqlite() -> str:
        return EngineConf.SQLITE.value

    @staticmethod
    def dirname() -> str:
        return EngineConf.DIR_NAME.value

    @staticmethod
    def min_name_length() -> int:
        return EngineConf.NAME_MIN_LENGTH.value

    @staticmethod
    def max_name_length() -> int:
        return EngineConf.NAME_MAX_LENGTH.value

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

    @staticmethod
    def db_name_space() -> str:
        return EngineConf.DB_NAME_SPACE.value

    @staticmethod
    def db_name_ascii() -> str:
        return EngineConf.DB_NAME_ASCII.value

    @staticmethod
    def db_name_length() -> str:
        return EngineConf.DB_NAME_LENGTH.value

    @staticmethod
    def dir_not_found() -> str:
        return EngineConf.DIR_NOT_FOUND.value

    @staticmethod
    def no_dir_access() -> str:
        return EngineConf.NO_DIR_ACCESS.value

    @staticmethod
    def dir_path_error() -> str:
        return EngineConf.DIR_PATH_ERROR.value
