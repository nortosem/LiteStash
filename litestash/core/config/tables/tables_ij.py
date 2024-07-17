"""The TablesIJIJ Table Module

Enumerate the valid chars for keys with hash[:0] equal to i,j,I,J.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesIJ(Valid):
    """Enumeration with access methods"""
    I_LOW = 'i'
    J_LOW = 'j'
    I_UP = 'I'
    J_UP = 'J'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesIJ.I_LOW.value:
                return TablesIJ.i_low()
            case TablesIJ.J_LOW.value:
                return TablesIJ.j_low()
            case TablesIJ.I_UP.value:
                return TablesIJ.i_upper()
            case TablesIJ.J_UP.value:
                return TablesIJ.j_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def i_low() -> str:
        """Get the full table name for hash[i:]"""
        return str(Tables.TABLES_IJ.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesIJ.I_LOW.value
                   )

    @staticmethod
    def j_low() -> str:
        """Get the full table name for hash[j:]"""
        return str(Tables.TABLES_IJ.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesIJ.J_LOW.value
                   )

    @staticmethod
    def i_upper() -> str:
        """Get the full table name for hash[I:]"""
        return str(Tables.TABLES_IJ.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesIJ.I_LOW.value
                   )

    @staticmethod
    def j_upper() -> str:
        """Get the full table name for hash[J:]"""
        return str(Tables.TABLES_IJ.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesIJ.J_LOW.value
                   )
