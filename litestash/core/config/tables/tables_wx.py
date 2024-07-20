"""tables_wx Table Module

This module defines an enumeration (`TablesWX`) for accessing table names
within the SQLite database associated with hash values starting with 'w', 'W',
'x', or 'X'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a
specific hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesWX(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        W_LOW: Represents a lowercase 'w' as the first hash character.
        X_LOW: Represents a lowercase 'x' as the first hash character.
        W_UP: Represents an uppercase 'W' as the first hash character.
        X_UP: Represents an uppercase 'X' as the first hash character.
    """
    W_LOW = 'w'
    X_LOW = 'x'
    W_UP = 'W'
    X_UP = 'X'

    @staticmethod
    def get_table_name(char: str) -> str:
        """
        Returns the full table name based on the provided initial hash
        character.

        Args:
            char: The initial character of the hash value.

        Returns:
            The full table name corresponding to the hash character.

        Raises:
            ValueError: If the provided character is not a valid hash prefix
            for this module.
        """
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
        """Returns the full table name for lowercase 'w' hash prefixes."""
        return str(Tables.TABLES_WX.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesWX.W_LOW.value
                   )

    @staticmethod
    def x_low() -> str:
        """Returns the full table name for lowercase 'x' hash prefixes."""
        return str(Tables.TABLES_WX.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesWX.X_LOW.value
                   )

    @staticmethod
    def w_upper() -> str:
        """Returns the full table name for uppercase 'W' hash prefixes."""
        return str(Tables.TABLES_WX.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesWX.W_LOW.value
                   )

    @staticmethod
    def x_upper() -> str:
        """Returns the full table name for uppercase 'X' hash prefixes."""
        return str(Tables.TABLES_WX.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesWX.X_LOW.value
                   )
