"""tables_mn Table Module

This module defines an enumeration (`TablesMN`) for accessing table names
within the SQLite database associated with hash values starting with 'm', 'M',
'n', or 'N'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesMN(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        M_LOW: Represents a lowercase 'm' as the first hash character.
        N_LOW: Represents a lowercase 'n' as the first hash character.
        M_UP: Represents an uppercase 'M' as the first hash character.
        N_UP: Represents an uppercase 'N' as the first hash character.
    """
    N_LOW = 'n'
    M_LOW = 'm'
    M_UP = 'M'
    N_UP = 'N'

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
            case TablesMN.M_LOW.value:
                return TablesMN.m_low()
            case TablesMN.N_LOW.value:
                return TablesMN.n_low()
            case TablesMN.M_UP.value:
                return TablesMN.m_upper()
            case TablesMN.N_UP.value:
                return TablesMN.n_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def m_low() -> str:
        """Returns the full table name for lowercase 'm' hash prefixes."""
        return str(Tables.TABLES_MN.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesMN.M_LOW.value
                   )

    @staticmethod
    def n_low() -> str:
        """Returns the full table name for lowercase 'n' hash prefixes."""
        return str(Tables.TABLES_MN.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesMN.N_LOW.value
                   )

    @staticmethod
    def m_upper() -> str:
        """Returns the full table name for uppercase 'M' hash prefixes."""
        return str(Tables.TABLES_MN.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesMN.M_LOW.value
                   )

    @staticmethod
    def n_upper() -> str:
        """Returns the full table name for uppercase 'N' hash prefixes."""
        return str(Tables.TABLES_MN.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesMN.N_LOW.value
                   )
