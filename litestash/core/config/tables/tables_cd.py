"""The tables_cCdD Table Module

Enumerate the valid chars for keys with hash[:0] equal to c,C,d,D.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesCD(Valid):
    """Enumeration with access methods"""
    C_LOW = 'c'
    D_LOW = 'd'
    C_UP = 'C'
    D_UP = 'D'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesCD.C_LOW.value:
                return TablesCD.c_low()
            case TablesCD.D_LOW.value:
                return TablesCD.d_low()
            case TablesCD.C_UP.value:
                return TablesCD.c_upper()
            case TablesCD.D_UP.value:
                return TablesCD.d_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def c_low() -> str:
        """Get the full table name for hash[:0] equal to 'c'"""
        return str(Tables.TABLES_CD.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesCD.C_LOW.value
                   )

    @staticmethod
    def d_low() -> str:
        """Get the full table name for hash[:0] equal to 'd'"""
        return  str(Tables.TABLES_CD.value
                    +Names.LOW.value
                    +Names.HASH.value
                    +TablesCD.D_LOW.value
                    )

    @staticmethod
    def c_upper() -> str:
        """Get the full table name for hash[:0] equal to 'C'"""
        return str(Tables.TABLES_CD.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesCD.C_LOW.value
                   )

    @staticmethod
    def d_upper() -> str:
        """Get the full table name for hash[:0] equal to 'D'"""
        return str(Tables.TABLES_CD.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesCD.D_LOW.value
                   )
