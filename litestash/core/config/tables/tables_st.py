"""tables_st Table Module

This module defines an enumeration (`TablesST`) for accessing table names
within the SQLite database associated with hash values starting with 's', 'S',
't', or 'T'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesST(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        S_LOW: Represents a lowercase 's' as the first hash character.
        T_LOW: Represents a lowercase 't' as the first hash character.
        S_UP: Represents an uppercase 'S' as the first hash character.
        T_UP: Represents an uppercase 'T' as the first hash character.
    """
    S_LOW = 's'
    T_LOW = 't'
    S_UP = 'S'
    T_UP = 'T'

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
            case TablesST.S_LOW.value:
                return TablesST.s_low()
            case TablesST.T_LOW.value:
                return TablesST.t_low()
            case TablesST.S_UP.value:
                return TablesST.s_upper()
            case TablesST.T_UP.value:
                return TablesST.t_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def s_low() -> str:
        """Returns the full table name for lowercase 's' hash prefixes."""
        return str(Tables.TABLES_ST.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesST.S_LOW.value
                   )

    @staticmethod
    def t_low() -> str:
        """Returns the full table name for lowercase 't' hash prefixes."""
        return str(Tables.TABLES_ST.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesST.T_LOW.value
                   )

    @staticmethod
    def s_upper() -> str:
        """Returns the full table name for uppercase 'S' hash prefixes."""
        return str(Tables.TABLES_ST.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesST.S_LOW.value
                   )

    @staticmethod
    def t_upper() -> str:
        """Returns the full table name for uppercase 'T' hash prefixes."""
        return str(Tables.TABLES_ST.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesST.T_LOW.value
                   )
