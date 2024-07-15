"""The TablesQRrR Table Module

Enumerate the valid chars for keys with hash[:0] equal to q,Q,r,R.
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

class TablesQR(Valid):
    """Enumeration with access methods"""
    Q_LOW = 'q'
    R_LOW = 'r'
    Q_UP = 'Q'
    R_UP = 'R'

    @staticmethod
    def get_table_name(char: str) -> str:
        """Match on char and return table name"""
        match char:
            case TablesQR.Q_LOW.value:
                return TablesQR.Q_LOW_low()
            case TablesQR.R_LOW.value:
                return TablesQR.R_LOW_low()
            case TablesQR.Q_UP.value:
                return TablesQR.Q_UP_upper()
            case TablesQR.R_UP.value:
                return TablesQR.R_UP_upper()
            case _:
                raise ValueError(Names.ERROR.value)

    @staticmethod
    def q_low() -> str:
        """Get the full table name for """
        return(
            f'{TablesQR.Q_LOW.value}{Names.LOW.value}{Names.HASH.value}'
        )

    @staticmethod
    def r_low() -> str:
        """Get the full table name for """
        return(
            f'{TablesQR.R_LOW.value}{Names.LOW.value}{Names.HASH.value}'
        )

    @staticmethod
    def q_upper() -> str:
        """Get the full table name for Q"""
        return(
            f'{TablesQR.Q_UP.value}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def r_upper() -> str:
        """Get the full table name for R"""
        return(
            f'{TablesQR.R_UP.value}{Names.UP.value}{Names.HASH.value}'
        )