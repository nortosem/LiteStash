"""The LiteStash Core

The Core module contains the configuration, utility, and build modules used by
LiteStash.

Modules:
    config: Package-wide configuration enumerations
    util: Various package utilities
    engine: Initiate and manage the engines for the LiteStash
    schema: Initiate and manage the metadata for the LiteStash
    session: Mange the session factories for all LiteStash databases
"""
from litestash.core.config.root import Core
from litestash.core import config
from litestash.core import util
from litestash.core.engine import Engine
from litestash.core.schema import Metadata
from litestash.core.session import Session

__all__ = [
    Core.CONFIG.value,
    Core.UTIL.value,
    Core.ENGINE.value,
    Core.SCHEMA.value,
    Core.SESSION.value
]
