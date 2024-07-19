"""The LiteStash Package

A unSQL key-value database for JSON data with string keys.

Modules:
    Core: The core components of the LiteStash
    Models: The data models for a LiteStash
    Store: The LiteStash class module
"""
from litestash.core.config.root import Main
from litestash import core
from litestash.models import LiteStashData
from litestash.models import LiteStashStore
from litestash.store import LiteStash

__version__ = "0.1.0b2"
__all__ = [
    Main.CORE.value,
    Main.DATA.value,
    Main.STORE.value,
    Main.STASH.value
]
