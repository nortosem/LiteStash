"""The tables_mMnN Table Module

Enumerate the valid chars for keys with hash[:0] equal to m,M,n,N.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class TablesMN(Valid):
    """Enumeration with access methods"""
    N_LOW = 'm'
    M_LOW = 'n'
    M_UP = 'M'
    N_UP = 'N'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesMN.M_LOW.value:
                return TablesMN.m_low()
            case TablesMN.N_LOW.value:
                return TablesMN.n_low()
            case TablesMN.M_UP.value:
                return TablesMN.m_upper()
            case TablesMN.N_UP.value:
                return TablesMN.n_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def m_low() -> str:
        """Get the full table name for hash[m:]"""
        return str(TablesMN.M_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def n_low() -> str:
        """Get the full table name for hash[n:]"""
        return str(TablesMN.N_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def m_upper() -> str:
        """Get the full table name for hash[M:]"""
        return str(TablesMN.M_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def n_upper() -> str:
        """Get the full table name for hash[N:]"""
        return str(TablesMN.N_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
