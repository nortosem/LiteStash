"""The tables_uUvV Table Module

Enumerate the valid chars for keys with hash[:0] equal to u,U,v,V.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_uV(Valid):
    """Enumeration with access methods"""
    U_LOW = 'u'
    V_LOW = 'v'
    U_UP = 'U'
    V_UP = 'V'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case LowerTables.U.value:
                return LowerTables.u_low()
            case LowerTables.V.value:
                return LowerTables.v_low()
            case UpperTables.U.value:
                return UpperTables.u_upper()
            case UpperTables.V.value:
                return UpperTables.v_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def u_low() -> str:
        """Get the full table name for hash[u:]"""
        return str(LowerTables.U.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def v_low() -> str:
        """Get the full table name for hash[v:]"""
        return str(LowerTables.V.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def u_upper() -> str:
        """Get the full table name for hash[U:]"""
        return str(UpperTables.U.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def v_upper() -> str:
        """Get the full table name for hash[V:]"""
        return str(UpperTables.V.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
