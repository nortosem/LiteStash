"""tables_89hu Table Module

This module defines an enumeration (`Tables89hu`) for accessing table names
within the SQLite database associated with hash values starting with '8', '9',
'-', or '_'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a
specific hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class Tables89hu(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        EIGHT: Represents the number '8' as the first hash character.
        NINE: Represents the number '9' as the first hash character.
        HYPHEN: Represents the character '-' as the first hash character.
        UNDERSCORE: Represents the character '_' as the first hash character.
    """
    EIGHT = '8'
    NINE = '9'
    HYPHEN = '-'
    UNDERSCORE = '_'

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
            case Tables89hu.EIGHT.value:
                return Tables89hu.eight()
            case Tables89hu.NINE.value:
                return Tables89hu.nine()
            case Tables89hu.HYPHEN.value:
                return Tables89hu.hyphen()
            case Tables89hu.UNDERSCORE.value:
                return Tables89hu.underscore()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def eight() -> str:
        """Returns the full table name for number '8' hash prefixes."""
        return str(Tables.TABLES_89HU.value
                   +Names.HASH.value
                   +Tables89hu.EIGHT.value
                   )

    @staticmethod
    def nine() -> str:
        """Returns the full table name for number '9' hash prefixes."""
        return str(Tables.TABLES_89HU.value
                   +Names.HASH.value
                   +Tables89hu.NINE.value
                   )

    @staticmethod
    def hyphen() -> str:
        """Returns the full table name for character '-' hash prefixes."""
        return str(Tables.TABLES_89HU.value
                   +Names.HASH.value
                   +Names.HYPHEN.value
                   )

    @staticmethod
    def underscore() -> str:
        """Returns the full table name for character '_' hash prefixes."""
        return str(Tables.TABLES_89HU.value
                   +Names.HASH.value
                   +Names.UNDER.value
                   )
