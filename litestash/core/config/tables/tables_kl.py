"""The tables_kKlL Table Module

Enumerate the valid chars for keys with hash[:0] equal to k,K,l,L.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesKL(Valid):
    """Enumeration with access methods"""
    K_LOW = 'k'
    L_LOW = 'l'
    K_UP = 'K'
    L_UP = 'L'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesKL.K_LOW.value:
                return TablesKL.k_low()
            case TablesKL.L_LOW.value:
                return TablesKL.l_low()
            case TablesKL.K_UP.value:
                return TablesKL.k_upper()
            case TablesKL.L_UP.value:
                return TablesKL.l_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def k_low() -> str:
        """Get the full table name for hash[k:]"""
        return str(Tables.TABLES_KL.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesKL.K_LOW.value
                   )

    @staticmethod
    def l_low() -> str:
        """Get the full table name for hash[l:]"""
        return str(Tables.TABLES_KL.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesKL.L_LOW.value
                   )

    @staticmethod
    def k_upper() -> str:
        """Get the full table name for hash[K:]"""
        return str(Tables.TABLES_KL.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesKL.K_LOW.value
                   )

    @staticmethod
    def l_upper() -> str:
        """Get the full table name for hash[L:]"""
        return str(Tables.TABLES_KL.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesKL.L_LOW.value
                   )
