"""tables_qr Table Module

This module defines an enumeration (`TablesQR`) for accessing table names
within the SQLite database associated with hash values starting with 'q', 'Q',
'r', or 'R'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesQR(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        Q_LOW: Represents a lowercase 'q' as the first hash character.
        R_LOW: Represents a lowercase 'r' as the first hash character.
        Q_UP: Represents an uppercase 'Q' as the first hash character.
        R_UP: Represents an uppercase 'R' as the first hash character.
    """
    Q_LOW = 'q'
    R_LOW = 'r'
    Q_UP = 'Q'
    R_UP = 'R'

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
            case TablesQR.Q_LOW.value:
                return TablesQR.q_low()
            case TablesQR.R_LOW.value:
                return TablesQR.r_low()
            case TablesQR.Q_UP.value:
                return TablesQR.q_upper()
            case TablesQR.R_UP.value:
                return TablesQR.r_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def q_low() -> str:
        """Returns the full table name for lowercase 'q' hash prefixes."""
        return str(Tables.TABLES_QR.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesQR.Q_LOW.value
                   )

    @staticmethod
    def r_low() -> str:
        """Returns the full table name for lowercase 'r' hash prefixes."""
        return str(Tables.TABLES_QR.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesQR.R_LOW.value
                   )

    @staticmethod
    def q_upper() -> str:
        """Returns the full table name for uppercase 'Q' hash prefixes."""
        return str(Tables.TABLES_QR.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesQR.Q_LOW.value
                   )

    @staticmethod
    def r_upper() -> str:
        """Returns the full table name for uppercase 'R' hash prefixes."""
        return str(Tables.TABLES_QR.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesQR.R_LOW.value
                   )
