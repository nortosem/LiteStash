"""LiteStash FTS

The Full-Text Search module provides the fts search capability for each
database. Each value and time column is usable for fts in a functional way.
def search_all_tables(search_term):
"""
import orjson
from typing import Generator
from typing import List
from sqlalchemy import Column
from sqlalchemy import DDL
from sqlalchemy import event
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy import union_all
from sqlalchemy.orm import Session
from litestash.models import LiteStashData
from litestash.core.config.root import Tables as DB_Names
from litestash.core.fts_model import ValueSearchColumn
from litestash.core.config.schema_conf import Sql
from litestash.core.config.fts_conf import ViewSetup as View
from litestash.core.config.fts_conf import SearchSetup as Search
from litestash.core.config.fts_conf import Trigger
from litestash.core.config.schema_conf import ColumnFields as C
from litestash.core.config.schema_conf import ColumnConfig as Conf
from litestash.core.util.litestash_util import EngineAttributes
from litestash.core.util.litestash_util import MetaAttributes
from litestash.core.util.litestash_util import SessionAttributes
from litestash.core.util.schema_util import mk_table_names

def db_key_search(
        session: Session,
        search_term: str
) -> List[LiteStashData]:
    """Full-text search for a database

    The data being search is json.  The key is a key for some data in the json
    Other values will likely fail.

    Args:
        session (Session): the session reference for a database
        search_term (str): the search string for a key within the json stash.
    """
    search_statement = select(
        func.key_hash.label(f'{C.HASH.value}'),
        text(
            f"json_extract({C.VALUE.value}, '$.{search_term}')"
        ).label(f'{C.VALUE.value}')
    ).where(
        text(f'{Search.table_name()} {Search.match()} :search_term')
    ).params(search_term=search_term)

    with session() as search_session:
        json_results = search_session.execute(search_statement).fetchall()

        if json_results is []:
            return []

        matches = []
        for row in json_results:
            match = LiteStashData(key=row.key, value=orjson.loads(row.value))
            matches.append(match)
        search_session.commit()
        return matches


def create_all_search_tables(
    engine_stash: EngineAttributes,
    meta_stash: MetaAttributes,
    session_stash: SessionAttributes,
) -> None:
    """Iterate through each database and create the FTS table"""
    for database in DB_Names:

        engine_detail = engine_stash.get(database)
        metadata_detail = meta_stash.get(database)
        session_detail = session_stash.get(database)

        create_view_all_table(
            engine_detail,
            metadata_detail,
            session_detail
        )

        create_search_table(
            engine_detail,
            metadata_detail,
            session_detail
        )


def create_search_table(
    engine_detail: EngineAttributes = None,
    metadata_detail: MetaAttributes = None,
    session_detail: SessionAttributes = None
) -> None:
    """
    Create a virtual FTS table on the view table for all tables in a database.
    """
    if engine_detail or metadata_detail or session_detail is None:
        raise ValueError('details missing error: TODO')

    if (engine_detail.db_name != metadata_detail.db_name or
            engine_detail.db_name != session_detail.db_name or
            metadata_detail.db_name != session_detail.db_name):
        raise ValueError('database must be the same error: TODO')

    create_view_all_table(engine_detail, metadata_detail, session_detail)
    metadata = metadata_detail.metadata
    session = session_detail.session

    with session() as mk_fts_session:
        create_fts_table_statement = text(
            f"""
            {Search.CREATE.value} {Search.ALL_VALUES.value}
            {Search.USING.value} fts5(
                {C.HASH.value} {Search.UNINDEXED.value},
                {C.TABLE_NAME.value} {Search.UNINDEXED.value},
                {C.DATA_VALUE.value},
                {Search.DETAIL.value}
            );
            """
        )
        mk_fts_session.execute(create_fts_table_statement)
        mk_fts_session.commit()

    def _insert_ddl(table_name) -> DDL:
        insert_statement = DDL(
            f"""
            {Trigger.create()} {table_name}{Trigger.name_insert()}
            {Trigger.after_insert()} {table_name}
            {Sql.begin()}
                {Sql.insert()} fts_all_values(
                    {C.HASH.value}, {C.TABLE_NAME.value}, {C.VALUE.value}
                )
                Sql.VALUES.value(
                    {Sql.new()}.{C.HASH.value},
                    '{table_name}',
                    {Sql.new()}.{C.VALUE.value}
                );
            {Sql.end()}
            """
        )
        return insert_statement

    def _update_ddl(table_name) -> DDL:
        update_statement = DDL(
            f"""
            {Trigger.create()} {table_name}{Trigger.name_update()}
            {Trigger.after_update()} {table_name}
            {Sql.begin()}
                {Sql.delete()} {Search.table_name()}
                {Sql.where()}
                    {C.HASH.value} = {Sql.old()}.{C.HASH.value} {Sql.AND.value}
                    table_name = '{table_name}';
                {Sql.insert()} fts_all_values(
                    {C.HASH.value}, {C.TABLE_NAME.value}, {C.VALUE.value}
                )
                {Sql.values()} (
                    {Sql.new()}.{C.HASH.value},
                    '{table_name}',
                    {Sql.new()}{C.VALUE.value}
                );
            {Sql.end()}
            """
        )
        return update_statement


    def _delete_ddl(table_name) -> DDL:
        delete_statement = DDL(
            f"""
            {Trigger.create()} {table_name}{Trigger.name_update()}
            {Trigger.after_delete()} {table_name}
            {Sql.begin()}
                {Sql.delete()} {Search.table_name()} {Sql.where()}
                    {C.HASH.value} = {Sql.old()}.{C.HASH.value} {Sql.AND.value}
                    {C.table_name()} = '{table_name}';
            {Sql.end()}
            """
        )
        return delete_statement

    for table_name, table in metadata.tables.items():
        insert_statement = _insert_ddl(table_name)
        update_statement = _update_ddl(table_name)
        delete_statement = _delete_ddl(table_name)
        for trigger, statement in zip(
            [Search.INSERT.value, Search.UPDATE.value, Search.DELETE.value],
            [insert_statement, update_statement, delete_statement]
        ):
            event.listen(
                table,
                trigger,
                statement.execute_if(dialect=Search.DIALECT.value)
            )


def create_view_all_table(
    engine_detail: EngineAttributes = None,
    metadata_detail: MetaAttributes = None,
    session_detail: SessionAttributes = None
) -> None:
    """Prepare the database tables as view for a full-text search"""
    if engine_detail or metadata_detail or session_detail is None:
        raise ValueError('details missing error: TODO')

    if (engine_detail.db_name != metadata_detail.db_name or
            engine_detail.db_name != session_detail.db_name or
            metadata_detail.db_name != session_detail.db_name):
        raise ValueError('database must be the same error: TODO')

    db_name = engine_detail.db_name
    metadata = metadata_detail.metadata
    session = session_detail.session
    table_names = [table_name for table_name in mk_table_names(db_name)]

    with session() as mk_view_session:
        select_table1 = select(
            metadata.tables[table_names[0]].key_hash,
            text(f"'{table_names[0]}'").label(f"{C.TABLE_NAME.value}"),
            metadata.tables[table_names[0]].value
        )
        select_table2 = select(
            metadata.tables[table_names[1]].key_hash,
            text(f"'{table_names[1]}'").label(f"{C.TABLE_NAME.value}"),
            metadata.tables[table_names[1]].value
        )
        select_table3 = select(
            metadata.tables[table_names[2]].key_hash,
            text(f"'{table_names[2]}'").label(f"{C.TABLE_NAME.value}"),
            metadata.tables[table_names[2]].value
        )
        select_table4 = select(
            metadata.tables[table_names[3]].key_hash,
            text(f"'{table_names[3]}'").label(f"{C.TABLE_NAME.value}"),
            metadata.tables[table_names[3]].value
        )
        unite_tables = union_all(
            select_table1,
            select_table2,
            select_table3,
            select_table4
        )
        create_view_statement = text(
            f"""
            {View.CREATE.value} {View.ALL_VALUES.value} {View.AS.value}'
            """
            ).columns(
                *[column for column in mk_value_view_columns()]
        )
        mk_view_session.execute(create_view_statement, unite_tables)
        mk_view_session.commit()


def mk_value_view_columns() -> Generator[Column, None, None]:
    """Make and yield each column for a Value View table"""
    for column in (
        mk_value_view_hash_column(),
        mk_value_view_tablename_column(),
        mk_value_view_value_column(),
    ):
        yield column


def mk_value_view_hash_column() -> Column:
    """Create and return a key_hash column for the view table"""
    hash_key_column = ValueSearchColumn(
        name = C.HASH.value,
        type_ = Conf.STR.value
    )
    return build_value_column(hash_key_column)


def mk_value_view_tablename_column() -> Column:
    """Create and return a tablename column for the view table"""
    table_name_column = ValueSearchColumn(
        name = C.TABLE_NAME.value,
        type_ = Conf.STR.value
    )
    return build_value_column(table_name_column)


def mk_value_view_value_column() -> Column:
    """Create and return a value column for the view table"""
    value_column = ValueSearchColumn(
        name = C.DATA_VALUE.value,
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
