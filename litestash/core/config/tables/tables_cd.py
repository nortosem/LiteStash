"""tables_cd Table Module

This module defines an enumeration (`TablesCD`) for accessing table names
within the SQLite database associated with hash values starting with 'c', 'C',
'd', or 'D'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class TablesCD(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        C_LOW: Represents a lowercase 'c' as the first hash character.
        D_LOW: Represents a lowercase 'd' as the first hash character.
        C_UP: Represents an uppercase 'C' as the first hash character.
        D_UP: Represents an uppercase 'D' as the first hash character.
    """
    C_LOW = 'c'
    D_LOW = 'd'
    C_UP = 'C'
    D_UP = 'D'

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
            case TablesCD.C_LOW.value:
                return TablesCD.c_low()
            case TablesCD.D_LOW.value:
                return TablesCD.d_low()
            case TablesCD.C_UP.value:
                return TablesCD.c_upper()
            case TablesCD.D_UP.value:
                return TablesCD.d_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def c_low() -> str:
        """Get the full table name for hash[:0] equal to 'c'"""
        return str(Tables.TABLES_CD.value
                   +Names.LOW.value
                   +Names.HASH.value
                   +TablesCD.C_LOW.value
                   )

    @staticmethod
    def d_low() -> str:
        """Get the full table name for hash[:0] equal to 'd'"""
        return  str(Tables.TABLES_CD.value
                    +Names.LOW.value
                    +Names.HASH.value
                    +TablesCD.D_LOW.value
                    )

    @staticmethod
    def c_upper() -> str:
        """Get the full table name for hash[:0] equal to 'C'"""
        return str(Tables.TABLES_CD.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesCD.C_LOW.value
                   )

    @staticmethod
    def d_upper() -> str:
        """Get the full table name for hash[:0] equal to 'D'"""
        return str(Tables.TABLES_CD.value
                   +Names.UP.value
                   +Names.HASH.value
                   +TablesCD.D_LOW.value
                   )
