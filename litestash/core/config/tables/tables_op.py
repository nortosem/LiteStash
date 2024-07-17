"""The tables_oOpP Table Module

Enumerate the valid chars for keys with hash[:0] equal to o,O,p,P.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesOP(Valid):
    """Enumeration with access methods"""
    O_LOW = 'o'
    P_LOW = 'p'
    O_UP = 'O'
    P_UP = 'P'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesOP.O_LOW.value:
                return TablesOP.o_low()
            case TablesOP.P_LOW.value:
                return TablesOP.p_low()
            case TablesOP.O_UP.value:
                return TablesOP.o_upper()
            case TablesOP.P_UP.value:
                return TablesOP.p_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def o_low() -> str:
        """Get the full table name for hash[o:]"""
        return str(Tables.TABLES_OP.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesOP.O_LOW.value
                   )

    @staticmethod
    def p_low() -> str:
        """Get the full table name for hash[p:]"""
        return str(Tables.TABLES_OP.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesOP.P_LOW.value
                   )

    @staticmethod
    def o_upper() -> str:
        """Get the full table name for hash[O:]"""
        return str(Tables.TABLES_OP.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesOP.O_LOW.value
                   )

    @staticmethod
    def p_upper() -> str:
        """Get the full table name for hash[P:]"""
        return str(Tables.TABLES_OP.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesOP.P_LOW.value
                   )
