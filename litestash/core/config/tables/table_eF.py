"""The tables_eEfF Table Module

Enumerate the valid chars for keys with hash[:0] equal to e,E,f,F.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_eF(Valid):
    """Enumeration with access methods"""
    E_LOW = 'e'
    F_LOW = 'f'
    E_UP = 'E'
    F_UP = 'F'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_eF.E_LOW.value:
                return Tables_eF.e_low()
            case Tables_eF.F_LOW.value:
                return Tables_eF.f_low()
            case Tables_eF.E_UP.value:
                return Tables_eF.e_upper()
            case Tables_eF.F_UP.value:
                return Tables_eF.f_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def e_low() -> str:
        """Get the full table name for hash[e:]"""
        return str(Tables_eF.E_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def f_low() -> str:
        """Get the full table name for hash[f:]"""
        return str(Tables_eF.F_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def e_upper() -> str:
        """Get the full table name for hash[E:]"""
        return str(Tables_eF.E_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def f_upper() -> str:
        """Get the full table name for hash[F:]"""
        return str(Tables_eF.F_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
