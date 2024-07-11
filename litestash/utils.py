"""The Utilities

Functions:
    setup_engine
    setup_metadata
    setup_sessions
    check_key

"""
from hashlib import blake2b
from litestash.config import Utils
from litestash.config import Names
from litestash.config import Digitables
from litestash.config import LowerTables
from litestash.config import DataScheme
from litestash.config import UpperTables
from litestash.config import ColumnSetup as Col
from litestash.models import StashColumns
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import BLOB
from sqlalchemy import MetaData
from typing import Generator

def check_key(key: str) -> bytes:
    """Validates and encodes an ASCII string key to bytes."""
    if key.isacii():
        if key.isalnum():
            return key.encode()
        else:
            raise ValueError(DataScheme.ALNUM_ERROR.value)
    else:
        raise ValueError(DataScheme.ASCII_ERROR.value)


def hash_key(key: bytes) -> bytes:
    """Get the hashed str bytes for a key"""
    return blake2b(key, digest_size=Utils.SIZE.value).hexdigest().encode()


def mk_hash_column() -> Column:
    """Return a Column for the hash"""
    return StashColumns.column(
        Col.HASH.value,
        BLOB,
        primary_key=True,
        nullable=False
    )


def mk_key_column() -> Column:
    """Return a Column for the key being stored."""
    return StashColumns.column(
        Col.KEY.value,
        BLOB,
        unique=True,
        index=True,
        nullable=False
    )


def mk_value_column() -> Column:
    """Return a Column for the value being stored."""
    return StashColumns.column(
        Col.VALUE.value,
        JSON,
        nullable=True
    )


def mk_time_column() -> Column:
    """Return a Column for the date the data was added."""
    return StashColumns.get_column(
        Col.TIME.value,
        Integer,
        nullable=True
        )


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


def zf_db() -> Generator[bytes,None,None]:
    """Prefix generator for zero through four database"""
    for n in (Digitables.ZERO.value,
              Digitables.ONE.value,
              Digitables.TWO.value,
              Digitables.THREE.value,
              Digitables.FOUR.value
    ):
        yield n

def fn_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for n in (Digitables.FIVE.value,
              Digitables.SIX.value,
              Digitables.SEVEN.value,
              Digitables.EIGHT.value,
              Digitables.NINE.value
    ):
        yield n

def ael_db() -> Generator[bytes,None,None]:
    """Prefix generator for a through e database"""
    for l in (LowerTables.A.value,
              LowerTables.B.value,
              LowerTables.C.value,
              LowerTables.D.value,
              LowerTables.E.value
    ):
        yield l

def fil_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.F.value,
              LowerTables.G.value,
              LowerTables.H.value,
              LowerTables.I.value
    ):
        yield l

def jml_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.J.value,
              LowerTables.K.value,
              LowerTables.L.value,
              LowerTables.M.value
    ):
        yield l

def nrl_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.N.value,
              LowerTables.O.value,
              LowerTables.P.value,
              LowerTables.Q.value,
              LowerTables.R.value
    ):
        yield l

def svl_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.S.value,
              LowerTables.T.value,
              LowerTables.U.value,
              LowerTables.V.value
    ):
        yield l

def wzl_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.W.value,
              LowerTables.X.value,
              LowerTables.Y.value,
              LowerTables.Z.value
    ):
        yield l

def aeu_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.A.value,
              UpperTables.B.value,
              UpperTables.C.value,
              UpperTables.D.value,
              UpperTables.E.value
    ):
        yield l

def fiu_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.F.value,
              UpperTables.G.value,
              UpperTables.H.value,
              UpperTables.I.value
    ):
        yield l

def jmu_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.J.value,
              UpperTables.K.value,
              UpperTables.L.value,
              UpperTables.M.value
    ):
        yield l

def nru_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.N.value,
              UpperTables.O.value,
              UpperTables.P.value,
              UpperTables.Q.value,
              UpperTables.R.value
    ):
        yield l

def svu_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.S.value,
              UpperTables.T.value,
              UpperTables.U.value,
              UpperTables.V.value
    ):
        yield l

def wzu_db() -> Generator[bytes,None,None]:
    """Prefix generator for W through Z database"""
    for l in (UpperTables.W.value,
              UpperTables.X.value,
              UpperTables.Y.value,
              UpperTables.Z.value
    ):
        yield l

def get_db_name(char: bytes) -> bytes:
    """Find database for given char"""
    match char:
        case char if char in zf_db():
            return Names.ZFD.value
        case char if char in fn_db():
            return Names.FND.value
        case char if char in ael_db():
            return Names.AEL.value
        case char if char in fil_db():
            return Names.FIL.value
        case char if char in jml_db():
            return Names.JML.value
        case char if char in nrl_db():
            return Names.NRL.value
        case char if char in svl_db():
            return Names.SVL.value
        case char if char in wzl_db():
            return Names.WZL.value
        case char if char in aeu_db():
            return Names.AEU.value
        case char if char in fiu_db():
            return Names.FIU.value
        case char if char in jmu_db():
            return Names.JMU.value
        case char if char in nru_db():
            return Names.NRU.value
        case char if char in svu_db():
            return Names.SVU.value
        case char if char in wzu_db():
            return Names.WZU.value
        case _:
            raise ValueError(Utils.DB_NAME_ERROR.value)


def get_table_name(char: bytes) -> str:
    """Given a char get the table's name"""
    if char in Digitables:
        return Digitables.get_table_name(char)
    elif char in LowerTables:
        return LowerTables.get_table_name(char)
    elif char in UpperTables:
        return UpperTables.get_table_name(char)
    else:
        raise ValueError("NO!")


def mk_table_names() -> Generator[str, None, None]:
    """Make all valid Table names

    Generate names for all tables in cache
    Return a generator.
    """
    for chars in (Digitables,LowerTables,UpperTables):
        for char in chars:
            yield f'{char.value}{Names.HASH.value}'


def mk_tables(metadata: MetaData) -> MetaData:
    """Make Tables

    Create all tables using preset columns and names.
    """
    for table_name in mk_table_names():
        Table(
            table_name,
            metadata,
            *(column for column in mk_columns())
        )
    return metadata
