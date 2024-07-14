"""The tables_gGhH Table Module

Enumerate the valid chars for keys with hash[:0] equal to g,G,h,H.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_gH(Valid):
    """Enumeration with access methods"""
    G_LOW = 'g'
    H_LOW = 'h'
    G_UP = 'G'
    H_UP = 'H'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_gH.G_LOW.value:
                return Tables_gH.g_low()
            case Tables_gH.H_LOW.value:
                return Tables_gH.h_low()
            case Tables_gH.G_UP.value:
                return Tables_gH.g_upper()
            case Tables_gH.H_UP.value:
                return Tables_gH.h_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def g_low() -> str:
        """Get the full table name for hash[g:]"""
        return str(Tables_gH.G_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def h_low() -> str:
        """Get the full table name for hash[h:]"""
        return str(Tables_gH.H_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def g_upper() -> str:
        """Get the full table name for hash[G:]"""
        return str(Tables_gH.G_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def h_upper() -> str:
        """Get the full table name for hash[H:]"""
        return str(Tables_gH.H_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
