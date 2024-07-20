"""tables_ij Table Module

This module defines an enumeration (`TablesIJ`) for accessing table names
within the SQLite database associated with hash values starting with 'i', 'I',
'j', or 'J'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesIJ(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        I_LOW: Represents a lowercase 'i' as the first hash character.
        J_LOW: Represents a lowercase 'j' as the first hash character.
        I_UP: Represents an uppercase 'I' as the first hash character.
        J_UP: Represents an uppercase 'J' as the first hash character.
    """
    I_LOW = 'i'
    J_LOW = 'j'
    I_UP = 'I'
    J_UP = 'J'

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
            case TablesIJ.I_LOW.value:
                return TablesIJ.i_low()
            case TablesIJ.J_LOW.value:
                return TablesIJ.j_low()
            case TablesIJ.I_UP.value:
                return TablesIJ.i_upper()
            case TablesIJ.J_UP.value:
                return TablesIJ.j_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def i_low() -> str:
        """Returns the full table name for lowercase 'i' hash prefixes."""
        return str(Tables.TABLES_IJ.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesIJ.I_LOW.value
                   )

    @staticmethod
    def j_low() -> str:
        """Returns the full table name for lowercase 'j' hash prefixes."""
        return str(Tables.TABLES_IJ.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesIJ.J_LOW.value
                   )

    @staticmethod
    def i_upper() -> str:
        """Returns the full table name for uppercase 'I' hash prefixes."""
        return str(Tables.TABLES_IJ.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesIJ.I_LOW.value
                   )

    @staticmethod
    def j_upper() -> str:
        """Returns the full table name for uppercase 'J' hash prefixes."""
        return str(Tables.TABLES_IJ.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesIJ.J_LOW.value
                   )
