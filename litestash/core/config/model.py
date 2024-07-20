"""LiteStash Model Configuration

Provides Pydantic model configuration constants for serialization and behavior.
"""
from litestash.core.config.root import Valid

class StashConf(Valid):
    """LiteStash Model Config

    Enumeration for the model_config dictionary slots/keys.
    """
    ORM_MODE = 'orm_mode'
    EXTRA = 'extra'
    JSON_LOADS = 'json_loads'
    JSON_DUMPS = 'json_dumps'
