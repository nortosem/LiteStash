"""The tables_yz Table Module

This module defines an enumeration (`TablesYZ`) for accessing table names
within the SQLite database associated with hash values starting with 'y', 'Y',
'z', or 'Z'.

Each member of the enum represents a valid hash prefix, and provides methods for
retrieving the corresponding full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesYZ(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        Y_LOW: Represents a lowercase 'y' as the first hash character.
        Z_LOW: Represents a lowercase 'z' as the first hash character.
        Y_UP: Represents an uppercase 'Y' as the first hash character.
        Z_UP: Represents an uppercase 'Z' as the first hash character.
    """
    Y_LOW = 'y'
    Z_LOW = 'z'
    Y_UP = 'Y'
    Z_UP = 'Z'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Gets the full table name based on the provided initial hash
        character.

        Args:
            char (str): The initial character of the hash value.

        Returns:
            str: The full table name corresponding to the hash character.

        Raises:
            ValueError: If the provided character is not a valid hash prefix.
        """
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
        """Returns the full table name for lowercase 'y' hash prefixes."""
        return str(Tables.TABLES_YZ.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesYZ.Y_LOW.value
                   )

    @staticmethod
    def z_low() -> str:
        """Returns the full table name for lowercase 'z' hash prefixes."""
        return str(Tables.TABLES_YZ.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesYZ.Z_LOW.value
                   )

    @staticmethod
    def y_upper() -> str:
        """Returns the full table name for uppercase 'Y' hash prefixes."""
        return str(Tables.TABLES_YZ.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesYZ.Y_LOW.value
                   )

    @staticmethod
    def z_upper() -> str:
        """Returns the full table name for uppercase 'Z' hash prefixes."""
        return str(Tables.TABLES_YZ.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesYZ.Z_LOW.value
                   )
