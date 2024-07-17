"""Eight,9,-,_ Table Module

Enumerate the valid chars for keys with hash[:0] equal to 8,9,-,_.
"""
from litestash.core.config.root import Valid
from litestash.core.config.root import Tables
from litestash.core.config.schema_conf import Names

class Tables89hu(Valid):
    """Enumerate char 8,9,-,_"""
    EIGHT = '8'
    NINE = '9'
    HYPHEN = '-'
    UNDERSCORE = '_'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
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
        """Get the full table name for hash[:0] equal to '8'"""
        return str(Tables.TABLES_89HU.value
                   +Names.HASH.value
                   +Tables89hu.EIGHT.value
                   )

    @staticmethod
    def nine() -> str:
        """Get the full table name for hash[:0] equal to '9'"""
        return str(Tables.TABLES_89HU.value
                   +Names.HASH.value
                   +Tables89hu.NINE.value
                   )

    @staticmethod
    def hyphen() -> str:
        """Get the full table name for hash[:0] equal to '-'"""
        return str(Tables.TABLES_89HU.value
                   +Names.HASH.value
                   +Names.HYPHEN.value
                   )

    @staticmethod
    def underscore() -> str:
        """Get the full table name for hash[:0] equal to '_'"""
        return str(Tables.TABLES_89HU.value
                   +Names.HASH.value
                   +Names.UNDER.value
                   )
