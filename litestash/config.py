"""Package Configuration

The config module enumerates the common required strings.
"""
from enum import Enum
from enum import unique
from typing import Self

class Valid(Enum):
    """Valid Root"""
    pass


class StashSlots(Valid):
    """all slots for the LiteStash"""
    DB_NAME = f'db_name'
    ENGINE = f'engine'
    METADATA = f'metadata'
    DB_SESSION = f'db_session'


class SetupDB(Valid):
    """SetupDB

    Provide the configuation to setup a database engine.
    """
    SQLITE = f'sqlite://'
    FILENAME = f'litestash.db'
    MEMORY = f':memory:'
    ECHO = True
    FUTURE = True
    NO_ECHO = False
    NO_FUTURE = False

    @staticmethod
    def sqlite() -> str:
        return f'{SetupDB.SQLITE.value}'

    @staticmethod
    def filename() -> str:
        return f'{SetupDB.FILENAME.value}'

    @staticmethod
    def memory() -> str:
        return f'{SetupDB.MEMORY.value}'

    @staticmethod
    def echo() -> str:
        return f'{SetupDB.ECHO.value}'

    @staticmethod
    def future() -> str:
        return f'{SetupDB.FUTURE.value}'

    @staticmethod
    def no_echo() -> str:
        return f'{SetupDB.NO_ECHO.value}'

    @staticmethod
    def no_future() -> str:
        return f'{SetupDB.NO_FUTURE.value}'


class Pragma(Valid):
    """Sqlite Pragma

    The default pragma configuration.
    """
    PRAGMA = f'PRAGMA'
    JOURNAL_MODE = f'journal_mode=WAL'
    SYNCHRONOUS = f'synchronous=NORMAL'
    FOREIGN_KEYS = f'foreign_keys=ON'

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
    ROW_ID = f'rowid'
    HASH = f'key_hash'
    KEY = f'key'
    VALUE = f'value'
    DATE_CREATED = f'date_created'


class TableFiles(Valid):
    """Table & File Names

    Default file names for each group of tables.
    And the sufficx for each table in database file.
    """
    ROOT = f'_hash'


class ZF_Tables(Valid):
    """Zero to Four

    The tables for hashes that start with zero, one, two, three, and four.
    """
    ZERO = f'0'
    ONE = f'1'
    TWO = f'2'
    THREE = f'3'
    FOUR = f'4'


class FN_Tables(Valid):
    """Five to Nine tables

    The tables for hashes that start with five, six, seven, eight, and nine.
    """
    FIVE = f'5'
    SIX = f'6'
    SEVEN = f'7'
    EIGHT = f'8'
    NINE = f'9'


class AM_Lower(Valid):
    """am lower

    For hashes that begin with lowercase letters a through m.
    """
    A = f'a'
    B = f'b'
    C = f'c'
    D = f'd'
    E = f'e'
    F = f'f'
    G = f'g'
    H = f'h'
    I = f'i'
    J = f'j'
    K = f'k'
    L = f'l'
    M = f'm'


class NZ_Lower(Valid):
    """nz lower

    For hashes that begin with lowercase letters n through z.
    """
    N = f'n'
    O = f'o'
    P = f'p'
    Q = f'q'
    R = f'r'
    S = f's'
    T = f't'
    U = f'u'
    V = f'v'
    W = f'w'
    X = f'x'
    Y = f'y'
    Z = f'z'


class AM_Upper(Valid):
    """AM Upper

    For hashes that begin with uppercase letters A through M.
    """
    A = f'A'
    B = f'B'
    C = f'C'
    D = f'D'
    E = f'E'
    F = f'F'
    G = f'G'
    H = f'H'
    I = f'I'
    J = f'J'
    K = f'K'
    L = f'L'
    M = f'M'


class NZ_Upper(Valid):
    """NZ Upper

    For hashes that begin with uppercase letters N through Z.
    """
    N = f'N'
    O = f'O'
    P = f'P'
    Q = f'Q'
    R = f'R'
    S = f'S'
    T = f'T'
    U = f'U'
    V = f'V'
    W = f'W'
    X = f'X'
    Y = f'Y'
    Z = f'Z'
