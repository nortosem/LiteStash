"""The Utilities


"""
from litestash.config import TableName
from litestash.config import Num
from litestash.config import LowerCase
from litestash.config import UpperCase

def make_tables():
    """Make Tables

    Generate names for all tables in cache
    """
    for i in [Num,LowerCase,UpperCase]
    for table_name in (
        f'{TableName.ROOT.value}{suffix.value}' for suffix in i
    ):
        yield table_name
