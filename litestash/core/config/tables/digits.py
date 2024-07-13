"""Numeric Table Configuration Module

TODO: docs
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Digitables(Valid):
    """Digitables

    The table prefix for hashes that start with a digit.
    """
    ZERO = b'0'
    ONE = b'1'
    TWO = b'2'
    THREE = b'3'
    FOUR = b'4'
    FIVE = b'5'
    SIX = b'6'
    SEVEN = b'7'
    EIGHT = b'8'
    NINE = b'9'

    @staticmethod
    def get_table_name(char: bytes) -> str:
        """Match on char and return table name"""
        match char:
            case Digitables.ZERO.value:
                return Digitables.zero()
            case Digitables.ONE.value:
                return Digitables.one()
            case Digitables.TWO.value:
                return Digitables.two()
            case Digitables.THREE.value:
                return Digitables.three()
            case Digitables.FOUR.value:
                return Digitables.four()
            case Digitables.FIVE.value:
                return Digitables.five()
            case Digitables.SIX.value:
                return Digitables.six()
            case Digitables.SEVEN.value:
                return Digitables.seven()
            case Digitables.EIGHT.value:
                return Digitables.eight()
            case Digitables.NINE.value:
                return Digitables.nine()
            case _:
                raise ValueError('NO!')

    @staticmethod
    def zero() -> str:
        """Get the full table name for hash[0:]"""
        return f'{Digitables.ZERO.value.decode()}{Names.HASH.value}'

    @staticmethod
    def one() -> str:
        """Get the full table name for hash[1:]"""
        return f'{Digitables.ONE.value.decode()}{Names.HASH.value}'

    @staticmethod
    def two() -> str:
        """Get the full table name for hash[2:]"""
        return f'{Digitables.TWO.value.decode()}{Names.HASH.value}'

    @staticmethod
    def three() -> str:
        """Get the full table name for hash[3:]"""
        return f'{Digitables.THREE.value.decode()}{Names.HASH.value}'

    @staticmethod
    def four() -> str:
        """Get the full table name for hash[4:]"""
        return f'{Digitables.FOUR.value.decode()}{Names.HASH.value}'

    @staticmethod
    def five() -> str:
        """Get the full table name for hash[5:]"""
        return f'{Digitables.FIVE.value.decode()}{Names.HASH.value}'

    @staticmethod
    def six() -> str:
        """Get the full table name for hash[6:]"""
        return f'{Digitables.SIX.value.decode()}{Names.HASH.value}'

    @staticmethod
    def seven() -> str:
        """Get the full table name for hash[7:]"""
        return f'{Digitables.SEVEN.value.decode()}{Names.HASH.value}'

    @staticmethod
    def eight() -> str:
        """Get the full table name for hash[8:]"""
        return f'{Digitables.EIGHT.value.decode()}{Names.HASH.value}'

    @staticmethod
    def nine() -> str:
        """Get the full table name for hash[9:]"""
        return f'{Digitables.NINE.value.decode()}{Names.HASH.value}'
