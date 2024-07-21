"""LiteStash: A High-Performance In-Memory Key-Value Store

LiteStash is a Python library providing a fast and efficient key-value (KV)
store for JSON data with string keys. It leverages SQLite for reliable data
storage and offers a simple NoSQL-like API.

Key Features:

- Blazing-Fast Performance:  Utilizes distributed hashing operations.
- Persistent Storage: Optionally syncs data to disk for durability.
- Scalability: Distributes data across tables & databases.
- Full-Text Search (FTS5):  Enables efficient searching within JSON values.
- Type Safety:  Uses Pydantic for robust data validation and type checking.

Main Modules:

- `core`: Core components for engine, metadata, and session management.
- `models`: Data models for representing key-value pairs and database entities.
- `store`: The main `LiteStash` class for interacting with the KV store.

Example:

```python
from litestash import LiteStash

cache = LiteStash()
cache.set("user_123", {"name": "Alice"})
data = cache.get("user_123")
"""
from litestash.core.config.root import Main
from litestash import core
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
from litestash.store import LiteStash

__version__ = "0.1.0b4"
__all__ = [
    Main.CORE.value,
    Main.DATA.value,
    Main.STORE.value,
    Main.STASH.value
]
