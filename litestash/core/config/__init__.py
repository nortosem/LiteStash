"""LiteStash Configuration Subpackage

This subpackage provides centralized configuration constants and enums for
various aspects of the LiteStash key-value store. It includes:

- **`litestash_conf`:**  General configuration constants for LiteStash
behavior.
- **`schema_conf`:**  Configuration options related to database schema and
column definitions.
- **`tables`:** A subpackage defining enums for accessing table names within
the distributed database structure.
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
