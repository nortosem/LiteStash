"""tables_47 Table Module

This module defines an enumeration (`Tables47`) for accessing table names
within the SQLite database associated with hash values starting with '4', '5',
'6', or '7'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class Tables47(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        FOUR: Represents the number '4' as the first hash character.
        FIVE: Represents the number '5' as the first hash character.
        SIX: Represents the number '6' as the first hash character.
        SEVEN: Represents the number '7' as the first hash character.
    """
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'

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
            case Tables47.FOUR.value:
                return Tables47.four()
            case Tables47.FIVE.value:
                return Tables47.five()
            case Tables47.SIX.value:
                return Tables47.six()
            case Tables47.SEVEN.value:
                return Tables47.seven()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def four() -> str:
        """Returns the full table name for number '4' hash prefixes."""
        return str(Tables.TABLES_47.value
                   +Names.HASH.value
                   +Tables47.FOUR.value
                   )

    @staticmethod
    def five() -> str:
        """Returns the full table name for number '5' hash prefixes."""
        return str(Tables.TABLES_47.value
                   +Names.HASH.value
                   +Tables47.FIVE.value
                   )

    @staticmethod
    def six() -> str:
        """Returns the full table name for number '6' hash prefixes."""
        return str(Tables.TABLES_47.value
                   +Names.HASH.value
                   +Tables47.SIX.value
                   )

    @staticmethod
    def seven() -> str:
        """Returns the full table name for number '7' hash prefixes."""
        return str(Tables.TABLES_47.value
                   +Names.HASH.value
                   +Tables47.SEVEN.value
                   )
