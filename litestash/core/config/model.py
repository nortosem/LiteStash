"""LiteStash Model Configuration

Provides Pydantic model configuration constants for serialization and behavior.
"""
from litestash.core.config.root import Valid
from litestash.core.config.litestash_conf import DataScheme

class Parameter(Valid):
    """LiteStash Model Parameters

    Enumeration parameters used in LiteStash models.
    """
    SLOTS = True
    FROM_ATTRIBUTES = 'from_attributes'
    EXTRA = 'extra'


class StashDataclass(Valid):
    """LiteStash Dataclass Config Parameters

    Enumeration of ConfigDict parameters used for pydantic dataclass.
    """
    CONFIG = ((Parameter.FROM_ATTRIBUTES.value,
               DataScheme.FROM_ATTRIBUTES.value),
              (Parameter.EXTRA.value,
               DataScheme.FORBID_EXTRA.value)
              )


class StashField(Valid):
    """LiteStashData Key Config


    """
    VALID_KEY_ASCII = 'Value error, ASCII keys only'
    VALID_KEY_TEXT = 'Key text missing'
    VALID_VALUE_JSON = 'JSON input should be string, bytes, or bytearray'
    VALID_VALUE_TYPE = 'Input should be a valid string'
    VALID_KEY_LENGTH = '1 validation error for'
    AT_MOST = 'String should have at most 999 characters'
    AT_LEAST = 'String should have at least 3 characters'
