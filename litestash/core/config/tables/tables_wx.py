"""The tables_wWxX Table Module

Enumerate the valid chars for keys with hash[:0] equal to w,W,x,W.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesWX(Valid):
    """Enumeration with access methods"""
    W_LOW = 'w'
    X_LOW = 'x'
    W_UP = 'W'
    X_UP = 'X'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesWX.W_LOW.value:
                return TablesWX.w_low()
            case TablesWX.X_LOW.value:
                return TablesWX.x_low()
            case TablesWX.W_UP.value:
                return TablesWX.w_upper()
            case TablesWX.X_UP.value:
                return TablesWX.x_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def w_low() -> str:
        """Get the full table name for hash[w:]"""
        return str(Tables.TABLES_WX.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesWX.W_LOW.value
                   )

    @staticmethod
    def x_low() -> str:
        """Get the full table name for hash[x:]"""
        return str(Tables.TABLES_WX.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesWX.X_LOW.value
                   )

    @staticmethod
    def w_upper() -> str:
        """Get the full table name for hash[W:]"""
        return str(Tables.TABLES_WX.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesWX.W_LOW.value
                   )

    @staticmethod
    def x_upper() -> str:
        """Get the full table name for hash[X:]"""
        return str(Tables.TABLES_WX.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesWX.X_LOW.value
                   )
