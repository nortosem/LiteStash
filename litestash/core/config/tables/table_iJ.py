"""The tables_ijIJ Table Module

Enumerate the valid chars for keys with hash[:0] equal to i,j,I,J.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_iJ(Valid):
    """Enumeration with access methods"""
    I_LOW = 'i'
    J_LOW = 'j'
    I_UP = 'I'
    J_UP = 'J'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_iJ.I_LOW.value:
                return Tables_iJ.i_low()
            case Tables_iJ.J_LOW.value:
                return Tables_iJ.j_low()
            case Tables_iJ.I_UP.value:
                return Tables_iJ.i_upper()
            case Tables_iJ.J_UP.value:
                return Tables_iJ.j_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def i_low() -> str:
        """Get the full table name for hash[i:]"""
        return str(Tables_iJ.I_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def j_low() -> str:
        """Get the full table name for hash[j:]"""
        return str(Tables_iJ.J_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def i_upper() -> str:
        """Get the full table name for hash[I:]"""
        return str(Tables_iJ.I_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def j_upper() -> str:
        """Get the full table name for hash[J:]"""
        return str(Tables_iJ.J_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
