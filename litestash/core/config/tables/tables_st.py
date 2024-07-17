"""The tables_sStT Table Module

Enumerate the valid chars for keys with hash[:0] equal to s,S,t,T.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesST(Valid):
    """Enumeration with access methods"""
    S_LOW = 's'
    T_LOW = 't'
    S_UP = 'S'
    T_UP = 'T'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesST.S_LOW.value:
                return TablesST.s_low()
            case TablesST.T_LOW.value:
                return TablesST.t_low()
            case TablesST.S_UP.value:
                return TablesST.s_upper()
            case TablesST.T_UP.value:
                return TablesST.t_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def s_low() -> str:
        """Get the full table name for hash[s:]"""
        return str(Tables.TABLES_ST.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesST.S_LOW.value
                   )

    @staticmethod
    def t_low() -> str:
        """Get the full table name for hash[t:]"""
        return str(Tables.TABLES_ST.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesST.T_LOW.value
                   )

    @staticmethod
    def s_upper() -> str:
        """Get the full table name for hash[S:]"""
        return str(Tables.TABLES_ST.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesST.S_LOW.value
                   )

    @staticmethod
    def t_upper() -> str:
        """Get the full table name for hash[T:]"""
        return str(Tables.TABLES_ST.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesST.T_LOW.value
                   )
