"""The LiteStash Core Metadata Config

TODO: docs
"""
from litestash.core.config.root import Valid

class MetaSlots(Valid):
    """Slots for the LiteStashMetadata"""
    ZFD = 'zfd'
    FND = 'fnd'
    AEL = 'ael'
    FIL = 'fil'
    JML = 'jml'
    NRL = 'nrl'
    SVL = 'svl'
    WZL = 'wzl'
    AEU = 'aeu'
    FIU = 'fiu'
    JMU = 'jmu'
    NRU = 'nru'
    SVU = 'svu'
    WZU = 'wzu'


class Pragma(Valid):
    """Sqlite Pragma

    The default pragma configuration.
    """
    PRAGMA = 'PRAGMA'
    JOURNAL_MODE = 'journal_mode=WAL'
    SYNCHRONOUS = 'synchronous=NORMAL'
    FOREIGN_KEYS = 'foreign_keys=ON'

    @staticmethod
    def journal_mode() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.JOURNAL_MODE.value}'

    @staticmethod
    def synchronous() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.SYNCHRONOUS.value}'

    @staticmethod
    def foreign_keys() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.FOREIGN_KEYS.value}'


class ColumnSetup(Valid):
    """The Column Setup

    Define the column attributes for each table
    """
    HASH = 'key_hash'
    LOT = 'lot'
    DIGEST = 'key_diges'
    KEY = 'key'
    VALUE = 'value'
    DATE_TIME = 'datetime'
    MS_TIME = 'microseconds'


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
    DOC = 'todo'
    ERROR = 'Value must be a valid column type'

class Names(Valid):
    """Various Names

    Default filenames for each database.
    Also the Table name suffix as HASH
    """
    HASH = '_hash'
    LOW = '_lower'
    UP = '_upper'
    DB = '.db'
    TABLES_03 = 'tables_03'
    TABLES_47 = 'tables_47'
    TABLES_89HU = 'tablee_89hu'
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
    ERROR = 'Invalid character request'
