"""The tables_aAbB Table Module

Enumerate the valid chars for keys with hash[:0] equal to a,A,b,B.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_aB(Valid):
    """Enumeration with access methods"""
    A_LOW = 'a'
    A_UP = 'A'
    B_LOW = 'B'
    B_UP = 'b'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_aB.A_LOW.value:
                return Tables_aB.a_low()
            case Tables_aB.B_LOW.value:
                return Tables_aB.b_low()
            case Tables_aB.A_UP.value:
                return Tables_aB.a_upper()
            case Tables_aB.B_UP.value:
                return Tables_aB.b_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def a_low() -> str:
        """Get the full table name for hash[:0] equal to 'a'"""
        return str(Tables_aB.A_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def b_low() -> str:
        """Get the full table name for hash[:0] equal to 'b'"""
        return str(Tables_aB.B_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def a_upper() -> str:
        """Get the full table name for hash[:0] equal to 'A'"""
        return str(Tables_aB.A_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def b_upper() -> str:
        """Get the full table name for hash[:0] equal to 'B'"""
        return str(Tables_aB.B_UPB.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
