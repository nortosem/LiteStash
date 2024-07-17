"""The tables_uUvV Table Module

Enumerate the valid chars for keys with hash[:0] equal to u,U,v,V.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesUV(Valid):
    """Enumeration with access methods"""
    U_LOW = 'u'
    V_LOW = 'v'
    U_UP = 'U'
    V_UP = 'V'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesUV.U_LOW.value:
                return TablesUV.U_LOW_low()
            case TablesUV.V_LOW.value:
                return TablesUV.V_LOW_low()
            case TablesUV.U_UP.value:
                return TablesUV.U_UP_upper()
            case TablesUV.V_UP.value:
                return TablesUV.V_UP_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def u_low() -> str:
        """Get the full table name for hash[u:]"""
        return str(Tables.TABLES_UV.value
                   +Tables.LOW.value
                   +Tables.HASH.value
                   +TablesUV.U_LOW.value
                   )

    @staticmethod
    def v_low() -> str:
        """Get the full table name for hash[v:]"""
        return str(Tables.TABLES_UV.value
                   +Tables.LOW.value
                   +Tables.HASH.value
                   +TablesUV.V_LOW.value
                   )

    @staticmethod
    def u_upper() -> str:
        """Get the full table name for hash[U:]"""
        return str(Tables.TABLES_UV.value
                   +Tables.UP.value
                   +Tables.HASH.value
                   +TablesUV.U_UP.value
                   )

    @staticmethod
    def v_upper() -> str:
        """Get the full table name for hash[V:]"""
        return str(Tables.TABLES_UV.value
                   +Tables.UP.value
                   +Tables.HASH.value
                   +TablesUV.V_UP.value
                   )
