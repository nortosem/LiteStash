"""tables_03 Table Module

This module defines an enumeration (`Tables03`) for accessing table names within
the SQLite database associated with hash values starting with '0', '1', '2', or
'3'.

The module facilitates consistent and type-safe access to these table names
within the LiteStash library. Each member of the enum corresponds to a specific
hash prefix and provides a method to construct the full table name.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class Tables03(Valid):
    """
    Enumeration for table names based on the initial character of the hash.

    Members:
        ZERO: Represents the number '0' as the first hash character.
        ONE: Represents the number '1' as the first hash character.
        TWO: Represents the number '2' as the first hash character.
        THREE: Represents the number '3' as the first hash character.
    """
    ZERO = '0'
    ONE = '1'
    TWO = '2'
    THREE = '3'

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
            case Tables03.ZERO.value:
                return Tables03.zero()
            case Tables03.ONE.value:
                return Tables03.one()
            case Tables03.TWO.value:
                return Tables03.two()
            case Tables03.THREE.value:
                return Tables03.three()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def zero() -> str:
        """Returns the full table name for number '0' hash prefixes."""
        return str(Tables.TABLES_03.value
                   +Names.HASH.value
                   +Tables03.ZERO.value
                   )

    @staticmethod
    def one() -> str:
        """Returns the full table name for number '1' hash prefixes."""
        return str(Tables.TABLES_03.value
                   +Names.HASH.value
                   +Tables03.ONE.value
                   )

    @staticmethod
    def two() -> str:
        """Returns the full table name for number '2' hash prefixes."""
        return str(Tables.TABLES_03.value
                   +Names.HASH.value
                   +Tables03.TWO.value
                   )

    @staticmethod
    def three() -> str:
        """Returns the full table name for number '3' hash prefixes."""
        return str(Tables.TABLES_03.value
                   +Names.HASH.value
                   +Tables03.THREE.value
                   )
