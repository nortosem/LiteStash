"""tables_ef Table Module

This module defines an enumeration (`TablesEF`) for accessing table names
within the SQLite database associated with hash values starting with 'e', 'E',
'f', or 'F'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesEF(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        E_LOW: Represents a lowercase 'e' as the first hash character.
        F_LOW: Represents a lowercase 'f' as the first hash character.
        E_UP: Represents an uppercase 'E' as the first hash character.
        F_UP: Represents an uppercase 'F' as the first hash character.
    """
    E_LOW = 'e'
    F_LOW = 'f'
    E_UP = 'E'
    F_UP = 'F'

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
            case TablesEF.E_LOW.value:
                return TablesEF.e_low()
            case TablesEF.F_LOW.value:
                return TablesEF.f_low()
            case TablesEF.E_UP.value:
                return TablesEF.e_upper()
            case TablesEF.F_UP.value:
                return TablesEF.f_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def e_low() -> str:
        """Returns the full table name for lowercase 'e' hash prefixes."""
        return str(Tables.TABLES_EF.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesEF.E_LOW.value
                   )

    @staticmethod
    def f_low() -> str:
        """Returns the full table name for lowercase 'f' hash prefixes."""
        return str(Tables.TABLES_EF.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesEF.F_LOW.value
                   )

    @staticmethod
    def e_upper() -> str:
        """Returns the full table name for uppercase 'E' hash prefixes."""
        return str(Tables.TABLES_EF.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesEF.E_LOW.value
                   )

    @staticmethod
    def f_upper() -> str:
        """Returns the full table name for uppercase 'F' hash prefixes."""
        return str(Tables.TABLES_EF.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesEF.F_LOW.value
                   )
