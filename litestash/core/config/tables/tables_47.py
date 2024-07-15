"""Four2Seven Table Module

Enumerate the valid chars for keys with hash[:0] equal to 4-7.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables47(Valid):
    """Enumerate 4 to 7"""
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables47.FOUR.value:
                return Tables47.four()
            case Tables47.FIVE.value:
                return Tables47.five()
            case Tables47.SIX.value:
                return Tables47.six()
            case Tables47.SEVEN.value:
                return Tables47.seven()

    @staticmethod
    def four() -> str:
        """Get the full table name for hash[:0] equal to '4'"""
        return f'{Tables47.FOUR.value}{Names.HASH.value}'

    @staticmethod
    def five() -> str:
        """Get the full table name for hash[:0] equal to '5'"""
        return f'{Tables47.FIVE.value}{Names.HASH.value}'

    @staticmethod
    def six() -> str:
        """Get the full table name for hash[:0] equal to '6'"""
        return f'{Tables47.SIX.value}{Names.HASH.value}'

    @staticmethod
    def seven() -> str:
        """Get the full table name for hash[:0] equal to '7'"""
        return f'{Tables47.SEVEN.value}{Names.HASH.value}'