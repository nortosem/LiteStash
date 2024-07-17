"""The tables_yYzZ Table Module

Enumerate the valid chars for keys with hash[:0] equal to y,Y,z,Z.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesYZ(Valid):
    """Enumeration with access methods"""
    Y_LOW = 'y'
    Z_LOW = 'z'
    Y_UP = 'Y'
    Z_UP = 'Z'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesYZ.Y_LOW.value:
                return TablesYZ.y_low()
            case TablesYZ.Z_LOW.value:
                return TablesYZ.z_low()
            case TablesYZ.Y_UP.value:
                return TablesYZ.y_upper()
            case TablesYZ.Z_UP.value:
                return TablesYZ.z_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def y_low() -> str:
        """Get the full table name for hash[y:]"""
        return str(Tables.TABLES_YZ.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesYZ.Y_LOW.value
                   )

    @staticmethod
    def z_low() -> str:
        """Get the full table name for hash[z:]"""
        return str(Tables.TABLES_YZ.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesYZ.Z_LOW.value
                   )

    @staticmethod
    def y_upper() -> str:
        """Get the full table name for hash[Y:]"""
        return str(Tables.TABLES_YZ.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesYZ.Y_LOW.value
                   )

    @staticmethod
    def z_upper() -> str:
        """Get the full table name for hash[Z:]"""
        return str(Tables.TABLES_YZ.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesYZ.Z_LOW.value
                   )
