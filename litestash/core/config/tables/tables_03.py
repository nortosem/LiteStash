"""Zero2Three Table Module

Enumerate the valid chars for keys with hash[:0] equal to 0-3.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class Tables03(Valid):
    """Enumerate 0 to 3"""
    ZERO = '0'
    ONE = '1'
    TWO = '2'
    THREE = '3'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables03.ZERO.value:
                return Tables03.zero()
            case Tables03.ONE.value:
                return Tables03.one()
            case Tables03.TWO.value:
                return Tables03.two()
            case Tables03.THREE.value:
                return Tables03.three()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def zero() -> str:
        """Get the full table name for hash[:0] equal to '0'"""
        return str(Tables.TABLES_03.value
                   +Names.HASH.value
                   +Tables03.ZERO.value
                   )

    @staticmethod
    def one() -> str:
        """Get the full table name for hash[:0] equal to '1'"""
        return str(Tables.TABLES_03.value
                   +Names.HASH.value
                   +Tables03.ONE.value
                   )

    @staticmethod
    def two() -> str:
        """Get the full table name for hash[:0] equal to '2'"""
        return str(Tables.TABLES_03.value
                   +Names.HASH.value
                   +Tables03.TWO.value
                   )

    @staticmethod
    def three() -> str:
        """Get the full table name for hash[:0] equal to '3'"""
        return str(Tables.TABLES_03.value
                   +Names.HASH.value
                   +Tables03.THREE.value
                   )
