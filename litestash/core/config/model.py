"""Model Configuration

Enumerate the config strings for the models module
"""
from litestash.core.config.root import Valid

class StashConf(Valid):
    """LiteStash Model Config

    The model_config dictionary slots/keys
    """
    ORM_MODE = 'orm_mode'
    EXTRA = 'extra'
    JSON_LOADS = 'json_loads'
    JSON_DUMPS = 'json_dumps'
