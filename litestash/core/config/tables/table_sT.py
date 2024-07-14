"""The tables_sStT Table Module

Enumerate the valid chars for keys with hash[:0] equal to s,S,t,T.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_sT(Valid):
    """Enumeration with access methods"""
    S_LOW = 's'
    T_LOW = 't'
    S_UP = 'S'
    T_UP = 'T'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_sT.S_LOW.value:
                return Tables_sT.S_LOW_low()
            case Tables_sT.T_LOW.value:
                return Tables_sT.T_LOW_low()
            case Tables_sT.S_UP.value:
                return Tables_sT.S_UP_upper()
            case Tables_sT.T_UP.value:
                return Tables_sT.T_UP_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def s_low() -> str:
        """Get the full table name for hash[s:]"""
        return str(Tables_sT.S_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def t_low() -> str:
        """Get the full table name for hash[t:]"""
        return str(Tables_sT.T_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def s_upper() -> str:
        """Get the full table name for hash[S:]"""
        return str(Tables_sT.S_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def t_upper() -> str:
        """Get the full table name for hash[T:]"""
        return str(Tables_sT.T_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
