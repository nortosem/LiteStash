"""The tables_cCdD Table Module

Enumerate the valid chars for keys with hash[:0] equal to c,C,d,D.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_cD(Valid):
    """Enumeration with access methods"""
    C_LOW = b'c'
    D_LOW = b'd'
    C_UP = b'C'
    D_UP = b'D'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_cD.C.value:
                return Tables_cD.c_low()
            case Tables_cD.D.value:
                return Tables_cD.d_low()
            case Tables_cD.C.value:
                return Tables_cD.c_upper()
            case Tables_cD.D.value:
                return Tables_cD.d_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def c_low() -> str:
        """Get the full table name for hash[:0] equal to 'c'"""
        return str(Tables_cD.C.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def d_low() -> str:
        """Get the full table name for hash[:0] equal to 'd'"""
        return  str(Tables_cD.D.value
                    +Names.LOW.value
                    +Names.HASH.value
                    )

    @staticmethod
    def c_upper() -> str:
        """Get the full table name for hash[:0] equal to 'C'"""
        return str(Tables_cD.C.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def d_upper() -> str:
        """Get the full table name for hash[:0] equal to 'D'"""
        return str(Tables_cD.D.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
