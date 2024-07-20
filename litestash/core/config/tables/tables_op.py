"""tables_op Table Module

This module defines an enumeration (`TablesOP`) for accessing table names
within the SQLite database associated with hash values starting with 'o', 'O',
'p', or 'P'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesOP(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        O_LOW: Represents a lowercase 'o' as the first hash character.
        P_LOW: Represents a lowercase 'p' as the first hash character.
        O_UP: Represents an uppercase 'O' as the first hash character.
        P_UP: Represents an uppercase 'P' as the first hash character.
    """
    O_LOW = 'o'
    P_LOW = 'p'
    O_UP = 'O'
    P_UP = 'P'

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
            case TablesOP.O_LOW.value:
                return TablesOP.o_low()
            case TablesOP.P_LOW.value:
                return TablesOP.p_low()
            case TablesOP.O_UP.value:
                return TablesOP.o_upper()
            case TablesOP.P_UP.value:
                return TablesOP.p_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def o_low() -> str:
        """Returns the full table name for lowercase 'o' hash prefixes."""
        return str(Tables.TABLES_OP.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesOP.O_LOW.value
                   )

    @staticmethod
    def p_low() -> str:
        """Returns the full table name for lowercase 'p' hash prefixes."""
        return str(Tables.TABLES_OP.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesOP.P_LOW.value
                   )

    @staticmethod
    def o_upper() -> str:
        """Returns the full table name for uppercase 'O' hash prefixes."""
        return str(Tables.TABLES_OP.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesOP.O_LOW.value
                   )

    @staticmethod
    def p_upper() -> str:
        """Returns the full table name for uppercase 'P' hash prefixes."""
        return str(Tables.TABLES_OP.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesOP.P_LOW.value
                   )
