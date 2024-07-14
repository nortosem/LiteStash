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
    KEY = 'key'
    VALUE = 'value'
    TIME = 'timedate'


class ColumnConfig(Valid):
    """The namedtuple Column config

    A config for mapping literal type string to sqlite database type.
    """
    TYPE_NAME = 'ColumnTypes'
    TYPE_STR = 'literal'
    TYPE_DB = 'sqlite'
    BLOB = 'BLOB'
    INT = 'INTEGER'
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
    TABLES_03 = 'tables_0-3'
    TABLES_47 = 'tables_4-7'
    TABLES_89HU = 'tablee_89-_'
    TABLES_AB = 'tables_aAbB'
    TABLES_CD = 'tables_cCdD'
    TABLES_EF = 'tables_eEfF'
    TABLES_GH = 'tables_gGhH'
    TABLES_IJ = 'tables_iIjJ'
    TABLES_KL = 'tables_kKlL'
    TABLES_MN = 'tables_mMnN'
    TABLES_OP = 'tables_oOpP'
    TABLES_QR = 'tables_qQrR'
    TABLES_ST = 'tables_sStT'
    TABLES_UV = 'tables_uUvV'
    TABLES_WX = 'tables_wWxX'
    TABLES_YZ = 'tables_yYzZ'
    ERROR = 'Invalid character request'


    @staticmethod
    def db_zft():
        """Filename for database with hashes that start with 0-4"""
        return f'{Names.ZFD.value.decode()}'

    @staticmethod
    def db_fnt():
        """Filename for database with hashes that start with 5-9"""
        return f'{Names.FND.value.decode()}'

    @staticmethod
    def db_ael():
        """Filename for database with hashes that start with a-e"""
        return f'{Names.AEL.value.decode()}'

    @staticmethod
    def db_fil():
        """Filename for database with hashes that start with f-i"""
        return f'{Names.FIL.value.decode()}'

    @staticmethod
    def db_jml():
        """Filename for database with hashes that start with j-m"""
        return f'{Names.JML.value.decode()}'

    @staticmethod
    def db_nrl():
        """Filename for database with hashes that start with n-r"""
        return f'{Names.NRL.value.decode()}'

    @staticmethod
    def db_svl():
        """Filename for database with hashes that start with s-v"""
        return f'{Names.SVL.value.decode()}'

    @staticmethod
    def db_wzl():
        """Filename for database with hashes that start with w-z"""
        return f'{Names.WZL.value.decode()}'
