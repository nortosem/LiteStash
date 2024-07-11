"""The Utilities

Functions:
    setup_engine
    setup_metadata
    setup_sessions
    check_key

"""
from collections import namedtuple
from hashlib import blake2b
from litestash.config import Utils
from litestash.config import Names
from litestash.config import Digitables
from litestash.config import LowerTables
from litestash.config import UpperTables
from litestash.config import SetupDB
from litestash.config import ColumnSetup as Col
from litestash.config import EngineStash
from litestash.config import MetaStash
from litestash.config import SessionStash
from litestash.config import DataScheme
from litestash.config import FTS5
from litestash.models import StashColumns
#from litestash.store import LiteStashEngine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import inspect
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import Engine
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import BLOB
from sqlalchemy import text
from sqlalchemy import create_engine
from typing import Generator
from typing import Tuple

def setup_engine(name: str) -> Engine:
    """Setup engine

    Args:
        engine_name (str): match with sqlite.db filename

    Return a tuple of (name, engine)
    """
    return (name,
            create_engine(
                f'{SetupDB.sqlite()}{SetupDB.dirname()}{name}.db',
                echo=SetupDB.echo.value
                )
            )

StashEngine = namedtuple(
    EngineStash.TYPE_NAME.value,
    [EngineStash.DB_NAME.value,
    EngineStash.ENGINE.value]
)
StashEngine.__doc__ = EngineStash.DOC.value


def setup_metadata(*args):
    """Setup Metadata & Tables

    Args:
        stash (LiteStashEngine):  Retrieve name & engine to setup from
        slot (str): datable named attribute slot
    """
    name, engine = args
    metadata = MetaData()
    metadata = mk_tables(metadata)
    metadata.create_all(bind=engine, checkfirst=True)
    return (name, metadata, engine)


StashMeta = namedtuple(
    MetaStash.TYPE_NAME.value,
    [MetaStash.DB_NAME.value,
    MetaStash.METADATA.value]
)
StashMeta.__doc__ = MetaStash.DOC.value


def setup_fts(*args):
    """Setup Full Text Search

    Given the engine stash and metadata stash:
        Add the FTS5 virtual tbles and connections to the database.
    """
    name, metadata, engine = data
    with engine.connect() as connection:
        for table in metadata.sorted_tables:
            fts = f'{FTS5.TABLE_PREFIX.value}{table.name}'
            connection.execute(text(f"""
                {FTS5.MK_TABLE.value} {fts} {FTS5.USING.value} {FTS5.OPEN.value}
                    {Col.KEY.value}, {Col.VALUE.value}, {Col.TIME.value},
                    {FTS5.CONTENT.value}{table.name},
                    {FTS5.ROW_ID.value}{Col.HASH.value}
                {FTS5.CLOSE.value}
            """))
            connection.execute(text(f"""
                {FTS5.MK_TRIGGER.value} {table.name}_ai
                {FTS5.AFTER_INSERT.value} {table.name}
                {FTS5.BEGIN_INSERT.value} {fts}(
                    {Col.KEY.value}, {Col.VALUE.value}, {Col.TIME.value},
                ) {FTS5.VALUES.value} (
                    {FTS5.NEW.value}{Col.KEY.value},
                    {FTS5.NEW.value}{Col.VALUE.value},
                    {FTS5.NEW.value}{Col.TIME.value},
                    );
                {FTS5.END.value}
                {FTS5.MK_TRIGGER.value} {table.name}_ai
                {FTS5.AFTER_UPDATE.value} {table.name}
                {FTS5.BEGIN_INSERT.value} {fts}(
                    {Col.KEY.value}, {Col.VALUE.value}, {Col.TIME.value},
                ) {FTS5.VALUES.value} (
                    {FTS5.NEW.value}{Col.KEY.value},
                    {FTS5.NEW.value}{Col.VALUE.value},
                    {FTS5.NEW.value}{Col.TIME.value},
                    );
                {FTS5.END.value}
                {FTS5.MK_TRIGGER.value} {table.name}_ai
                {FTS5.AFTER_DELETE.value} {table.name}
                {FTS5.BEGIN_INSERT.value} {fts}(
                    {Col.KEY.value}, {Col.VALUE.value}, {Col.TIME.value},
                ) {FTS5.VALUES.value} (
                    {FTS5.NEW.value}{Col.KEY.value},
                    {FTS5.NEW.value}{Col.VALUE.value},
                    {FTS5.NEW.value}{Col.TIME.value},
                    );
                {FTS5.END.value}
            """))
        return (name, metadata)


def setup_sessions(*args):
    """Make a sesssion

    Given a LiteStashEngine make a session factory for a database engine.

    Args:
        slot (str): database name slot
        stash (LiteStashEngine): An Engine with Metadata already setup
    """
    name, engine = args
    if inspect(engine).get_table_name():
        session = sessionmaker(engine)
    else:
        raise ValueError(f'{SessionStash.VALUE_ERROR.value}')
    return (name, session)


StashSession = namedtuple(
    SessionStash.TYPE_NAME.value,
    [SessionStash.DB_NAME.value,
    SessionStash.SESSION.value]
)
StashSession.__doc__ = SessionStash.DOC.value

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
    """Prefix generator for five throught nine database"""
    for l in (LowerTables.F.value,
              LowerTables.G.value,
              LowerTables.H.value,
              LowerTables.I.value
    ):
        yield l

def jml_db() -> Generator[bytes,None,None]:
    """Prefix generator for five throught nine database"""
    for l in (LowerTables.J.value,
              LowerTables.K.value,
              LowerTables.L.value,
              LowerTables.M.value
    ):
        yield l

def nrl_db() -> Generator[bytes,None,None]:
    """Prefix generator for five throught nine database"""
    for l in (LowerTables.N.value,
              LowerTables.O.value,
              LowerTables.P.value,
              LowerTables.Q.value,
              LowerTables.R.value
    ):
        yield l

def svl_db() -> Generator[bytes,None,None]:
    """Prefix generator for five throught nine database"""
    for l in (LowerTables.S.value,
              LowerTables.T.value,
              LowerTables.U.value,
              LowerTables.V.value
    ):
        yield l

def wzl_db() -> Generator[bytes,None,None]:
"""Prefix generator for five throught nine database"""
    for l in (LowerTables.W.value,
              LowerTables.X.value,
              LowerTables.Y.value,
              LowerTables.Z.value
    ):
        yield l

def aeu_db() -> Generator[bytes,None,None]:
"""Prefix generator for five throught nine database"""
    for l in (UpperTables.A.value,
              UpperTables.B.value,
              UpperTables.C.value,
              UpperTables.D.value,
              UpperTables.E.value
    ):
        yield l

def fiu_db() -> Generator[bytes,None,None]:
"""Prefix generator for five throught nine database"""
    for l in (UpperTables.F.value,
              UpperTables.G.value,
              UpperTables.H.value,
              UpperTables.I.value
    ):
        yield l

def jmu_db() -> Generator[bytes,None,None]:
"""Prefix generator for five throught nine database"""
    for l in (UpperTables.J.value,
              UpperTables.K.value,
              UpperTables.L.value,
              UpperTables.M.value
    ):
        yield l

def nru_db() -> Generator[bytes,None,None]:
"""Prefix generator for five throught nine database"""
    for l in (UpperTables.N.value,
              UpperTables.O.value,
              UpperTables.P.value,
              UpperTables.Q.value,
              UpperTables.R.value
    ):
        yield l

def svu_db() -> Generator[bytes,None,None]:
"""Prefix generator for five throught nine database"""
    for l in (UpperTables.S.value,
              UpperTables.T.value,
              UpperTables.U.value,
              UpperTables.V.value
    ):
        yield l

def wzu_db() -> Generator[bytes,None,None]:
"""Prefix generator for five throught nine database"""
    for l in (UpperTables.W.value,
              UpperTables.X.value,
              UpperTables.Y.value,
              UpperTables.Z.value
    ):
        yield l

def get_db_name(prefix: bytes) -> bytes:
    """Find database for given prefix"""
    match prefix:
        case char if char in zf_db():
            return Names.ZFD.value
        case char if char in :
            return Names.FND.value
        case char if char in :
            return Names.AEL.value
        case char if char in :
            return Names.FIL.value
        case char if char in :
            return Names.JML.value
        case char if char in :
            return Names.NRL.value
        case char if char in :
            return Names.SVL.value
        case char if char in :
            return Names.WZL.value
        case char if char in :
            return Names.AEU.value
        case char if char in :
            return Names.FIU.value
        case char if char in :
            return Names.JMU.value
        case char if char in :
            return Names.NRU.value
        case char if char in :
            return Names.SVU.value
        case char if char in :
            return Names.WZU.value
        case _:
            raise ValueError(Utils.DB_NAME_ERROR.value)

def mk_table_names() -> Generator[str, None, None]:
    """Make all valid Table names

    Generate names for all tables in cache
    Return a generator.
    """
    for chars in (Digitables,LowerTables,UpperTables):
        for suffix in chars:
            yield f'{TableName.ROOT.value}{suffix.value}'


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
