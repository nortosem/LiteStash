"""The tables_kKlL Table Module

Enumerate the valid chars for keys with hash[:0] equal to k,K,l,L.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_kL(Valid):
    """Enumeration with access methods"""
    K_LOW = 'k'
    L_LOW = 'l'
    K_UP = 'K'
    L_UP = 'L'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_kL.K_LOW.value:
                return Tables_kL.k_low()
            case Tables_kL.L_LOW.value:
                return Tables_kL.l_low()
            case Tables_kL.K_UP.value:
                return Tables_kL.k_upper()
            case Tables_kL.L_UP.value:
                return Tables_kL.l_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def k_low() -> str:
        """Get the full table name for hash[k:]"""
        return str(Tables_kL.K_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def l_low() -> str:
        """Get the full table name for hash[l:]"""
        return str(Tables_kL.L_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def k_upper() -> str:
        """Get the full table name for hash[K:]"""
        return str(Tables_kL.K_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def l_upper() -> str:
        """Get the full table name for hash[L:]"""
        return str(Tables_kL.L_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
