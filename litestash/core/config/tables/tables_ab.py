"""The tables_aAbB Table Module

Enumerate the valid chars for keys with hash[:0] equal to a,A,b,B.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Name

class TablesAB(Valid):
    """Enumeration with access methods"""
    A_LOW = 'a'
    A_UP = 'A'
    B_LOW = 'B'
    B_UP = 'b'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesAB.A_LOW.value:
                return TablesAB.a_low()
            case TablesAB.B_LOW.value:
                return TablesAB.b_low()
            case TablesAB.A_UP.value:
                return TablesAB.a_upper()
            case TablesAB.B_UP.value:
                return TablesAB.b_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def a_low() -> str:
        """Get the full table name for hash[:0] equal to 'a'"""
        return str(Tables.TABLES_AB.value
                   +Tables.LOW.value
                   +Tables.HASH.value
                   +TablesAB.A_LOW.value
                   )

    @staticmethod
    def b_low() -> str:
        """Get the full table name for hash[:0] equal to 'b'"""
        return str(Tables.TABLES_AB.value
                   +Tables.LOW.value
                   +Tables.HASH.value
                   +TablesAB.B_LOW.value
                   )

    @staticmethod
    def a_upper() -> str:
        """Get the full table name for hash[:0] equal to 'A'"""
        return str(Tables.TABLES_AB.value
                   +Tables.UP.value
                   +Tables.HASH.value
                   +TablesAB.A_UP.value
                   )

    @staticmethod
    def b_upper() -> str:
        """Get the full table name for hash[:0] equal to 'B'"""
        return str(Tables.TABLES_AB.value
                   +Tables.UP.value
                   +Tables.HASH.value
                   +TablesAB.B_UPB.value
                   )
