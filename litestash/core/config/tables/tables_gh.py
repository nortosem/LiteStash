"""tables_gh Table Module

This module defines an enumeration (`TablesGH`) for accessing table names
within the SQLite database associated with hash values starting with 'g', 'G',
'h', or 'H'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesGH(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        G_LOW: Represents a lowercase 'g' as the first hash character.
        H_LOW: Represents a lowercase 'h' as the first hash character.
        G_UP: Represents an uppercase 'G' as the first hash character.
        H_UP: Represents an uppercase 'H' as the first hash character.
    """
    G_LOW = 'g'
    H_LOW = 'h'
    G_UP = 'G'
    H_UP = 'H'

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
            case TablesGH.G_LOW.value:
                return TablesGH.g_low()
            case TablesGH.H_LOW.value:
                return TablesGH.h_low()
            case TablesGH.G_UP.value:
                return TablesGH.g_upper()
            case TablesGH.H_UP.value:
                return TablesGH.h_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def g_low() -> str:
        """Returns the full table name for lowercase 'g' hash prefixes."""
        return str(Tables.TABLES_GH.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesGH.G_LOW.value
                   )

    @staticmethod
    def h_low() -> str:
        """Returns the full table name for lowercase 'h' hash prefixes."""
        return str(Tables.TABLES_GH.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesGH.H_LOW.value
                   )

    @staticmethod
    def g_upper() -> str:
        """Returns the full table name for uppercase 'G' hash prefixes."""
        return str(Tables.TABLES_GH.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesGH.G_LOW.value
                   )

    @staticmethod
    def h_upper() -> str:
        """Returns the full table name for uppercase 'H' hash prefixes."""
        return str(Tables.TABLES_GH.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesGH.H_LOW.value
                   )
