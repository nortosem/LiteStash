"""The tables_eEfF Table Module

Enumerate the valid chars for keys with hash[:0] equal to e,E,f,F.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesEF(Valid):
    """Enumeration with access methods"""
    E_LOW = 'e'
    F_LOW = 'f'
    E_UP = 'E'
    F_UP = 'F'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesEF.E_LOW.value:
                return TablesEF.e_low()
            case TablesEF.F_LOW.value:
                return TablesEF.f_low()
            case TablesEF.E_UP.value:
                return TablesEF.e_upper()
            case TablesEF.F_UP.value:
                return TablesEF.f_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def e_low() -> str:
        """Get the full table name for hash[e:]"""
        return str(Tables.TABLES_EF.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesEF.E_LOW.value
                   )

    @staticmethod
    def f_low() -> str:
        """Get the full table name for hash[f:]"""
        return str(Tables.TABLES_EF.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesEF.F_LOW.value
                   )

    @staticmethod
    def e_upper() -> str:
        """Get the full table name for hash[E:]"""
        return str(Tables.TABLES_EF.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesEF.E_LOW.value
                   )

    @staticmethod
    def f_upper() -> str:
        """Get the full table name for hash[F:]"""
        return str(Tables.TABLES_EF.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesEF.F_LOW.value
                   )
