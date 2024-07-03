"""The Utilities


"""
from litestash.config import TableName
from litestash.config import Num
from litestash.config import LowerCase
from litestash.config import UpperCase

def mk_table_names():
    """Make Table Names

    Generate names for all tables in cache
    Return a generator.
    """
    for i in [Num,LowerCase,UpperCase]:
        for table_name in (
            f'{TableName.ROOT.value}{suffix.value}' for suffix in i
        ):
            yield table_name
