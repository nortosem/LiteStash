"""misc_util module

Miscellaneous LiteStash Utility Functions

- `allot`: Creates a random string for key distribution.
- **spaces_match:** Check for space characters in a value.
- **name_match:** Check if all name characters are valid ASCII.
"""
import re
from secrets import base64
from pydantic import StrictStr
from secrets import SystemRandom
from pydantic import ValidationError
from litestash.core.config.misc_conf import Matches
from litestash.logging import root_logger as logger


def allot(size: int = 6) -> StrictStr:
    """Generates a unique random string for key distribution.

    Args:
        size: The number of random bytes to use (must be divisible by 3).

    Returns:
        A URL-safe Base64-encoded string of the specified size.
    """
    if size is None:
        logger.error('No size provided for the random bytes')
        raise ValueError('A value of six or more is required')

    if not isinstance(size, int):
        logger.error('Integer size not provided: %s', size)
        raise TypeError(f'Invalid size type: {type(size)}')

    if size < 6:
        raise ValueError('min size')

    if size % 3 != 0:
        raise ValueError('must be divisible by three')

    lot = SystemRandom().randbytes(size)
    return base64.urlsafe_b64encode(lot).decode()


def spaces_match(value: StrictStr) -> bool:
    """Spaces Match Function

    Match value to compiled spaces pattern to check if value contains any
    space characters.

    Args:
        value: (StrictStr) -
            A Pydantic type that ensures the value is strictly a string.

    Returns:
        result: (Boolean) -
            True if the string contains any space character, False otherwise.

    Raises:
        ValidationError:
            If the input is not a string.
    """
    try:
        spaces = re.compile(r'.*?\s+')
        return bool(spaces.match(value))
    except ValidationError as value_error:
        logger.error('%s%s', Matches.log_error(), value_error)
        raise TypeError(f'{Matches.type_error()}') from value_error
