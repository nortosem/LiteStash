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
            case Tables_uV.U_LOW.value:
                return Tables_uV.U_LOW_low()
            case Tables_uV.V_LOW.value:
                return Tables_uV.V_LOW_low()
            case Tables_uV.U_UP.value:
                return Tables_uV.U_UP_upper()
            case Tables_uV.V_UP.value:
                return Tables_uV.V_UP_upper()
            case _f expand("%") == ""|browse confirm w|else|confirm w|endif
            :
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def u_low() -> str:
        """Get the full table name for hash[u:]"""
        return str(Tables_uV.U_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def v_low() -> str:
        """Get the full table name for hash[v:]"""
        return str(Tables_uV.V_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def u_upper() -> str:
        """Get the full table name for hash[U:]"""
        return str(Tables_uV.U_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def v_upper() -> str:
        """Get the full table name for hash[V:]"""
        return str(Tables_uV.V_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
