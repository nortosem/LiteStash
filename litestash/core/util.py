"""The Core Utility Module

This module organizes and defines a set of utility functions and classes
for the core LiteStash moduels.
#TODO docs
"""
from litestash.core.engine import Engine
from litestash.config import ColumnSetup as Col
from litestash.config import SetupDB
from litestash.config import EngineStash
from litestash.config import MetaStash
from litestash.config import SessionStash
from litestash.config import FTS5
from litestash.utils import mk_tables
from collections import namedtuple
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import inspect

from sqlalchemy import MetaData

from sqlalchemy.orm.session import sessionmaker
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


def setup_fts(*data):
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


