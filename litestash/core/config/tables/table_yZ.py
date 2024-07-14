"""The tables_yYzZ Table Module

Enumerate the valid chars for keys with hash[:0] equal to y,Y,z,Z.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class Tables_yZ(Valid):
    """Enumeration with access methods"""
    Y_LOW = 'y'
    Z_LOW = 'z'
    Y_UP = 'Y'
    Z_UP = 'Z'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case Tables_yZ.Y_LOW.value:
                return Tables_yZ.Y_LOW_low()
            case Tables_yZ.Z_LOW.value:
                return Tables_yZ.Z_LOW_low()
            case Tables_yZ.Y_UP.value:
                return Tables_yZ.Y_UP_upper()
            case Tables_yZ.Z_UP.value:
                return Tables_yZ.Z_UP_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def y_low() -> str:
        """Get the full table name for hash[y:]"""
        return str(Tables_yZ.Y_LOW.value
                   +Names.LOW.value
                   ++Names.HASH.value
                   )

    @staticmethod
    def z_low() -> str:
        """Get the full table name for hash[z:]"""
        return str(Tables_yZ.Z_LOW.value
                   +Names.LOW.value
                   +Names.HASH.value
                   )

    @staticmethod
    def y_upper() -> str:
        """Get the full table name for hash[Y:]"""
        return str(Tables_yZ.Y_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )

    @staticmethod
    def z_upper() -> str:
        """Get the full table name for hash[Z:]"""
        return str(Tables_yZ.Z_UP.value
                   +Names.UP.value
                   +Names.HASH.value
                   )
