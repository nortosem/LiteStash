"""LiteStash FTS

The Full-Text Search module provides the fts search capability for each
database. Each value and time column is usable for fts in a functional way.
"""
from litestash.core.config.root import Tables as DB_Names
from litestash.core.fts_model import ValueSearchColumn
from litestash.core.config.schema_conf import ColumnSetup as Col
from litestash.core.config.schema_conf import ColumnConfig as Conf
from litestash.core.util.litestash_util import EngineAttributes
from litestash.core.util.litestash_util import MetaAttributes
from litestash.core.util.litestash_util import SessionAttributes

def search(text: str = None) ->:
    """"""
    pass


def db_search(db_name: str, text: str) ->:
    """Full-text search of the values stored in the given database"""
    pass


def create_all_search_tables(
    engine_stash: EngineAttributes,
    meta_stash: MetaAttributes,
    session_stash: SessionAttributes,
) -> None:
    """Create FTS Tables in each database"""
    for database in DB_NAMES:
        pass



def create_search_table(
    db_name: str,
    db_engine: Engine,
    db_metadata: MetaData,
    db_session: Session
) -> None:
    """Create a FTS table on the view table for all tables in a database."""
    pass


def create_view_all_table(
    engine_detail: EngineAttributes = None,
    metadata_detail: MetaAttributes = None,
) -> None:
    """Prepare the database tables as view for a full-text search"""
    if engine_detail or metadata_detail is None:
        raise ValueError('details missing error: TODO')

    if engine_detail.db_name != metadata_detail.db_name:
        raise ValueError('database must be the same error: TODO')
    pass



def mk_value_view_tables(db_name: str, metadata: MetaData) -> MetaData:
    """"""
    for table_name in :
        Table(
            table_name,
            metadata,
            *[column for column in mk_value_view_columns()]
        )
    return metadata


def mk_value_view_columns() -> Generator[Column, None, None]:
    """"""
    for column in (
        mk_value_view_hash_column(),
        mk_value_view_tablename_column(),
        mk_value_view_value_column(),
    ):
        yield column


def mk_value_view_hash_column() -> Column:
    """"""
    hash_key_column = ValueSearchColumn(
        name = Col.HASH.value,
        type_ = Conf.STR.value
    )
    return build_value_column(hash_key_column)


def mk_value_view_tablename_column() -> Column:
    """"""
    table_name_column = ValueSearchColumn(
        name = Col.TABLE_NAME.value,
        type_ = Conf.STR.value
    )
    return build_value_column(table_name_column)


def mk_value_view_value_column() -> Column:
    """"""
    value_column = ValueSearchColumn(
        name = Col.TABLE_NAME.value,
        type_ = Conf.STR.value
    )
    return build_value_column(value_column)

def build_value_column(value_column: ValueSearchColumn) -> Column:
    """Create a value search column for the view table."""
    column = Column(
        value_column.name,
        value_column.type_
    )
    return column
