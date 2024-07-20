"""tables_kl Table Module

This module defines an enumeration (`TablesKL`) for accessing table names
within the SQLite database associated with hash values starting with 'k', 'K',
'l', or 'L'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesKL(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        K_LOW: Represents a lowercase 'k' as the first hash character.
        L_LOW: Represents a lowercase 'l' as the first hash character.
        K_UP: Represents an uppercase 'K' as the first hash character.
        L_UP: Represents an uppercase 'L' as the first hash character.
    """
    K_LOW = 'k'
    L_LOW = 'l'
    K_UP = 'K'
    L_UP = 'L'

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
            case TablesKL.K_LOW.value:
                return TablesKL.k_low()
            case TablesKL.L_LOW.value:
                return TablesKL.l_low()
            case TablesKL.K_UP.value:
                return TablesKL.k_upper()
            case TablesKL.L_UP.value:
                return TablesKL.l_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def k_low() -> str:
        """Returns the full table name for lowercase 'k' hash prefixes."""
        return str(Tables.TABLES_KL.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesKL.K_LOW.value
                   )

    @staticmethod
    def l_low() -> str:
        """Returns the full table name for lowercase 'l' hash prefixes."""
        return str(Tables.TABLES_KL.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesKL.L_LOW.value
                   )

    @staticmethod
    def k_upper() -> str:
        """Returns the full table name for uppercase 'K' hash prefixes."""
        return str(Tables.TABLES_KL.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesKL.K_LOW.value
                   )

    @staticmethod
    def l_upper() -> str:
        """Returns the full table name for uppercase 'L' hash prefixes."""
        return str(Tables.TABLES_KL.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesKL.L_LOW.value
                   )
