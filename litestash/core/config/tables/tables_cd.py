"""The tables_cCdD Table Module

Enumerate the valid chars for keys with hash[:0] equal to c,C,d,D.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesCD(Valid):
    """Enumeration with access methods"""
    C_LOW = b'c'
    D_LOW = b'd'
    C_UP = b'C'
    D_UP = b'D'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesCD.C.value:
                return TablesCD.c_low()
            case TablesCD.D.value:
                return TablesCD.d_low()
            case TablesCD.C.value:
                return TablesCD.c_upper()
            case TablesCD.D.value:
                return TablesCD.d_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def c_low() -> str:
        """Get the full table name for hash[:0] equal to 'c'"""
        return str(Tables.TABLES_CD.value
                   +Tables.LOW.value
                   +Tables.HASH.value
                   +TablesCD.C.value
                   )

    @staticmethod
    def d_low() -> str:
        """Get the full table name for hash[:0] equal to 'd'"""
        return  str(Tables.TABLES_CD.value
                    +Tables.LOW.value
                    +Tables.HASH.value
                    +TablesCD.D.value
                    )

    @staticmethod
    def c_upper() -> str:
        """Get the full table name for hash[:0] equal to 'C'"""
        return str(Tables.TABLES_CD.value
                   +Tables.UP.value
                   +Tables.HASH.value
                   +TablesCD.C.value
                   )

    @staticmethod
    def d_upper() -> str:
        """Get the full table name for hash[:0] equal to 'D'"""
        return str(Tables.TABLES_CD.value
                   +Tables.UP.value
                   +Tables.HASH.value
                   +TablesCD.D.value
                   )
