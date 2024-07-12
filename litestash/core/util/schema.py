"""The LiteStash Core Metadata Utilities

#TODO docs
"""


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
