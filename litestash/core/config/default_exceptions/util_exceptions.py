"""Utility Exceptions Module

Define Default messages for the litestash.core.util modules.

- **`TableUtilError`** Default error messages for table_util module
"""
from litestash.core.config.root import Valid


class TableUtilErrorMessages(Valid):
    """Default messages for TableUtil Exceptions"""
    TABLE_NOT_FOUND = 'No such table found'
    INVALID_TABLE_CLASS = 'A valid Table class is required'
    PARENT_TABLE_CLASS = 'A specific table is required'
    NONE_TABLE_CLASS = 'Tables cannot be None'
    INVALID_STASH_COLUMN = 'Table column cannot be None'
    STASH_COLUMN_TYPE = 'Column must be of the StashColumn type'

    @staticmethod
    def table_not_found():
        return TableUtilError.TABLE_NOT_FOUND.value

    @staticmethod
    def invalid_table_class():
        return TableUtilError.INVALID_TABLE_CLASS.value

    @staticmethod
    def parent_table_class():
        return TableUtilError.PARENT_TABLE_CLASS.value

    @staticmethod
    def none_table_class():
        return TableUtilError.NONE_TABLE_CLASS.value

    @staticmethod
    def invalid_stash_column():
        return TableUtilError.INVALID_STASH_COLUMN.value

    @staticmethod
    def stash_column_type():
        return TableUtilError.STASH_COLUMN_TYPE.value
