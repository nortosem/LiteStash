"""tables_uv Table Module

This module defines an enumeration (`TablesUV`) for accessing table names
within the SQLite database associated with hash values starting with 'u', 'U',
'V', or 'V'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesUV(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        U_LOW: Represents a lowercase 'u' as the first hash character.
        V_LOW: Represents a lowercase 'v' as the first hash character.
        U_UP: Represents an uppercase 'U' as the first hash character.
        V_UP: Represents an uppercase 'V' as the first hash character.
    """
    U_LOW = 'u'
    V_LOW = 'v'
    U_UP = 'U'
    V_UP = 'V'

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
            case TablesUV.U_LOW.value:
                return TablesUV.u_low()
            case TablesUV.V_LOW.value:
                return TablesUV.v_low()
            case TablesUV.U_UP.value:
                return TablesUV.u_upper()
            case TablesUV.V_UP.value:
                return TablesUV.v_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def u_low() -> str:
        """Returns the full table name for lowercase 'u' hash prefixes."""
        return str(Tables.TABLES_UV.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesUV.U_LOW.value
                   )

    @staticmethod
    def v_low() -> str:
        """Returns the full table name for lowercase 'v' hash prefixes."""
        return str(Tables.TABLES_UV.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesUV.V_LOW.value
                   )

    @staticmethod
    def u_upper() -> str:
        """Returns the full table name for uppercase 'U' hash prefixes."""

        return str(Tables.TABLES_UV.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesUV.U_LOW.value
                   )

    @staticmethod
    def v_upper() -> str:
        """Returns the full table name for uppercase 'V' hash prefixes."""

        return str(Tables.TABLES_UV.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesUV.V_LOW.value
                   )
