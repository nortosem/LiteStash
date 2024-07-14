"""The Database Table Build Functions

TODO: docs
"""
from litestash.core.config.schema_conf import ColumnSetup as Col
from litestash.core.config.schema_conf import ColumnConfig as Conf
from litestash.core.config.tables.digits import Digitables
from litestash.core.config.tables.lowercase import LowerTables
from litestash.core.config.tables.uppercase import UpperTables
from litestash.models import StashColumn
from sqlalchemy import Column
from typing import Generator

def create_zfd_tables() -> Generator[str, None, None]:
    """Generate all table names for 0-4"""
    for char in (Digitables.ZERO.value,
                 Digitables.ONE.value,
                 Digitables.TWO.value,
                 Digitables.THREE.value,
                 Digitables.FOUR.value
                 ):
        table_name = Digitables.get_table_name(char)
        yield table_name


def create_fnd_tables() -> Generator[str, None, None]:
    """Generate all table names for 5-9"""
    for char in (Digitables.FIVE.value,
                 Digitables.SIX.value,
                 Digitables.SEVEN.value,
                 Digitables.EIGHT.value,
                 Digitables.NINE.value
                 ):
        yield Digitables.get_table_name(char)


def create_ael_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (LowerTables.A.value,
                 LowerTables.B.value,
                 LowerTables.C.value,
                 LowerTables.D.value,
                 LowerTables.E.value
                 ):
        yield LowerTables.get_table_name(char)


def create_fil_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (LowerTables.F.value,
                 LowerTables.G.value,
                 LowerTables.H.value,
                 LowerTables.I.value,
                 ):
        yield LowerTables.get_table_name(char)


def create_jml_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (LowerTables.J.value,
                 LowerTables.K.value,
                 LowerTables.L.value,
                 LowerTables.M.value,
                 ):
        yield LowerTables.get_table_name(char)


def create_nrl_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (LowerTables.N.value,
                 LowerTables.O.value,
                 LowerTables.P.value,
                 LowerTables.Q.value,
                 LowerTables.R.value
                 ):
        yield LowerTables.get_table_name(char)


def create_svl_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (LowerTables.S.value,
                 LowerTables.T.value,
                 LowerTables.U.value,
                 LowerTables.V.value,
                 ):
        yield LowerTables.get_table_name(char)


def create_wzl_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (LowerTables.W.value,
                 LowerTables.X.value,
                 LowerTables.Y.value,
                 LowerTables.Z.value,
                 ):
        yield LowerTables.get_table_name(char)


def create_aeu_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (UpperTables.A.value,
                 UpperTables.B.value,
                 UpperTables.C.value,
                 UpperTables.D.value,
                 UpperTables.E.value
                 ):
        yield UpperTables.get_table_name(char)


def create_fiu_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (UpperTables.F.value,
                 UpperTables.G.value,
                 UpperTables.H.value,
                 UpperTables.I.value,
                 ):
        yield UpperTables.get_table_name(char)


def create_jmu_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (UpperTables.J.value,
                 UpperTables.K.value,
                 UpperTables.L.value,
                 UpperTables.M.value,
                 ):
        yield UpperTables.get_table_name(char)


def create_nru_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (UpperTables.N.value,
                 UpperTables.O.value,
                 UpperTables.P.value,
                 UpperTables.Q.value,
                 UpperTables.R.value
                 ):
        yield UpperTables.get_table_name(char)


def create_svu_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (UpperTables.S.value,
                 UpperTables.T.value,
                 UpperTables.U.value,
                 UpperTables.V.value,
                 ):
        yield UpperTables.get_table_name(char)


def create_wzu_tables() -> Generator[str, None, None]:
    """Generate all table names for a-e"""
    for char in (UpperTables.W.value,
                 UpperTables.X.value,
                 UpperTables.Y.value,
                 UpperTables.Z.value,
                 ):
        yield UpperTables.get_table_name(char)


def create_column(stash_column: StashColumn) -> Column:
    """Create columns for database tables"""
    column = Column(
        stash_column.name,
        stash_column.type_,
        primary_key=stash_column.primary_key,
        index=stash_column.index,
        unique=stash_column.unique,
    )
    return column

def mk_hash_column() -> Column:
    """Return a Column for the hash"""
    hash_column = StashColumn(
        Col.HASH.value,
        Conf.BLOB.value,
        primary_key=True,
    )
    return create_column(hash_column)


def mk_key_column() -> Column:
    """Return a Column for the key being stored."""
    key_column = StashColumn(
        Col.KEY.value,
        Conf.BLOB.value,
        unique=True,
        index=True,
    )
    return create_column(key_column)


def mk_value_column() -> Column:
    """Return a Column for the value being stored."""
    value_column = StashColumn(
        Col.VALUE.value,
        Conf.JSON.value,
    )
    return create_column(value_column)


def mk_time_column() -> Column:
    """Return a Column for the date the data was added."""
    time_column = StashColumn(Col.TIME.value,Conf.INT.value)
    return create_column(time_column)


def mk_columns() -> Generator[Column, None, None]:
    """Make Columns

    Return a generator for all columns used in each table.
    """
    for column in (
        mk_hash_column(),
        mk_key_column(),
        mk_value_column(),
        mk_time_column()
    ):
        yield column
