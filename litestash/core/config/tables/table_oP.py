"""The tables_oOpP Table Module

Enumerate the valid chars for keys with hash[:0] equal to o,O,p,P.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_oP(Valid):
    """Enumeration with access methods"""
    O_LOW = 'o'
    P_LOW = 'p'
    O_UP = 'O'
    P_UP = 'P'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_oP.O_LOW.value:
                return Tables_oP.o_low()
            case Tables_oP.P_LOW.value:
                return Tables_oP.p_low()
            case Tables_oP.O_UP.value:
                return Tables_oP.o_upper()
            case Tables_oP.P_UP.value:
                return Tables_oP.p_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def o_low() -> str:
        """Get the full table name for hash[o:]"""
        return str(Tables_oP.O_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def p_low() -> str:
        """Get the full table name for hash[p:]"""
        return str(Tables_oP.P_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def o_upper() -> str:
        """Get the full table name for hash[O:]"""
        return str(Tables_oP.O_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def p_upper() -> str:
        """Get the full table name for hash[P:]"""
        return str(Tables_oP.P_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
