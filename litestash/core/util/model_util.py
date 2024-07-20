"""LiteStash Model Utilities

This module provides helper types and functions for working with
LiteStash's data models and SQLAlchemy column definitions.

Key Components:

* `ColumnType`: A namedtuple representing a column type definition.
* `StrType`, `IntType`, `JsonType`: Predefined ColumnType objects for common
SQLite data types.
"""
from litestash.core.config.schema_conf import ColumnConfig
from collections import namedtuple
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String

# General Column KVS
ColumnType = namedtuple(
    ColumnConfig.TYPE_NAME.value,
    [
        ColumnConfig.TYPE_STR.value,
        ColumnConfig.TYPE_DB.value
    ]
)
ColumnType.__doc__ = ColumnConfig.DOC.value

# sqlalchemy sqlite data types
StrType = ColumnType(ColumnConfig.STR.value, String)
IntType = ColumnType(ColumnConfig.INT.value, Integer)
JsonType = ColumnType(ColumnConfig.JSON.value, JSON)
