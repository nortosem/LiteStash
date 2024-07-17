"""The tables_gGhH Table Module

Enumerate the valid chars for keys with hash[:0] equal to g,G,h,H.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesGH(Valid):
    """Enumeration with access methods"""
    G_LOW = 'g'
    H_LOW = 'h'
    G_UP = 'G'
    H_UP = 'H'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesGH.G_LOW.value:
                return TablesGH.g_low()
            case TablesGH.H_LOW.value:
                return TablesGH.h_low()
            case TablesGH.G_UP.value:
                return TablesGH.g_upper()
            case TablesGH.H_UP.value:
                return TablesGH.h_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def g_low() -> str:
        """Get the full table name for hash[g:]"""
        return str(Tables.TABLES_GH.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesGH.G_LOW.value
                   )

    @staticmethod
    def h_low() -> str:
        """Get the full table name for hash[h:]"""
        return str(Tables.TABLES_GH.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesGH.H_LOW.value
                   )

    @staticmethod
    def g_upper() -> str:
        """Get the full table name for hash[G:]"""
        return str(Tables.TABLES_GH.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesGH.G_LOW.value
                   )

    @staticmethod
    def h_upper() -> str:
        """Get the full table name for hash[H:]"""
        return str(Tables.TABLES_GH.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesGH.H_LOW.value
                   )
