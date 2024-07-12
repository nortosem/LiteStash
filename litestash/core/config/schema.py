"""The LiteStash Core Metadata Config

TODO: docs
"""
from enum import Enum

class Valid(Enum):
    """Valid Root"""
    pass


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
