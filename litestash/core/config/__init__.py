"""The Config subpackage

Modules:
    litestash_conf: The constants for litestash config
    schema_conf: The constants for schema config
    tables: The tables subpackage
"""
from litestash.core.config.root import Config
from litestash.core.config import litestash_conf
from litestash.core.config import schema_conf
from litestash.core.config import tables

__all__ = [
    Config.LITESTASH.value,
    Config.SCHEMA.value,
    Config.TABLES.value
]
