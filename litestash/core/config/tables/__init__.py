"""The Tables subpackage

Modules:
    digits: Numbers 0-9 and methods
    lowercase: a-z and methods
    uppercase: A-Z and methods
"""
from litestash.core.config.tables import digits
from litestash.core.config.tables import lowercase
from litestash.core.config.tables import uppercase
from litestash.core.config.root import Tables

__all__ = [
    Tables.DIGITS.value,
    Tables.LOWER.value,
    Tables.UPPER.value
]
