"""The LiteStash Core Metadata Config

TODO: docs
"""
from litestash.core.config.root import Valid

class Pragma(Valid):
    """Sqlite Pragma

    The default pragma configuration.
    """
    CONNECT = 'connect'
    PRAGMA = 'PRAGMA'
    JOURNAL_MODE = 'journal_mode=WAL;'
    SYNCHRONOUS = 'synchronous=NORMAL;'
    FOREIGN_KEYS = 'foreign_keys=ON;'
    JSON = 'json_valid = 1;'
    BEGIN = 'BEGIN'

    @staticmethod
    def journal_mode() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.JOURNAL_MODE.value}'

    @staticmethod
    def synchronous() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.SYNCHRONOUS.value}'

    @staticmethod
    def foreign_keys() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.FOREIGN_KEYS.value}'

    @staticmethod
    def valid_json() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.JSON.value}'



class ColumnSetup(Valid):
    """The Column Setup

    Define the column attributes for each table
    """
    HASH = 'key_hash'
    KEY = 'key'
    VALUE = 'value'
    TIMESTAMP = 'timestamp'
    MICROSECOND = 'microsecond'


class ColumnConfig(Valid):
    """The namedtuple Column config

    A config for mapping literal type string to sqlite database type.
    """
    TYPE_NAME = 'ColumnTypes'
    TYPE_STR = 'literal'
    TYPE_DB = 'sqlite'
    STR = 'String'
    INT = 'Integer'
    JSON = 'JSON'
    STASH_COLUMN = 'type_'
    DATA_KEY = 'key'
    DATA_VALUE = 'value'
    DOC = 'todo'
    ERROR = 'Value must be a valid column type'

class Names(Valid):
    """Various Names

    Also the Table name suffix as HASH
    """
    HYPHEN = 'hyphen'
    UNDER = 'underscore'
    HASH = '_hash_'
    LOW = '_lower'
    UP = '_upper'
    DB = '.db'
    ERROR = 'Invalid character request'
