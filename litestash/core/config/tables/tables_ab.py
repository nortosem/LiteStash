"""tables_ab Table Module

This module defines an enumeration (`TablesAB`) for accessing table names
within the SQLite database associated with hash values starting with 'a', 'A',
'b', or 'B'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesAB(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        A_LOW: Represents a lowercase 'a' as the first hash character.
        B_LOW: Represents a lowercase 'b' as the first hash character.
        A_UP: Represents an uppercase 'A' as the first hash character.
        B_UP: Represents an uppercase 'B' as the first hash character.
    """
    A_LOW = 'a'
    A_UP = 'A'
    B_LOW = 'b'
    B_UP = 'B'

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
            case TablesAB.A_LOW.value:
                return TablesAB.a_low()
            case TablesAB.B_LOW.value:
                return TablesAB.b_low()
            case TablesAB.A_UP.value:
                return TablesAB.a_upper()
            case TablesAB.B_UP.value:
                return TablesAB.b_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def a_low() -> str:
        """Returns the full table name for lowercase 'a' hash prefixes."""
        return str(Tables.TABLES_AB.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesAB.A_LOW.value
                   )

    @staticmethod
    def b_low() -> str:
        """Returns the full table name for lowercase 'b' hash prefixes."""
        return str(Tables.TABLES_AB.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesAB.B_LOW.value
                   )

    @staticmethod
    def a_upper() -> str:
        """Returns the full table name for uppercase 'A' hash prefixes."""
        return str(Tables.TABLES_AB.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesAB.A_LOW.value
                   )

    @staticmethod
    def b_upper() -> str:
        """Returns the full table name for uppercase 'B' hash prefixes."""
        return str(Tables.TABLES_AB.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesAB.B_LOW.value
                   )
