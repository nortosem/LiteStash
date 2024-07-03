"""Package Configuration

The config module enumerates the common required strings.
"""
from enum import Enum
from enum import unique

class Valid(Enum):
    """Valid Root"""
    pass


class TableName(Valid):
    """The Root of a Table Name

    Arg:
        ROOT (str): LiteCache
    """
    ROOT = f'LiteCache_'

class Num(Valid):
    """The numeric characters

    For hashes that begin with a digit.
    """
    ZERO = f'0'
    ONE = f'1'
    TWO = f'2'
    THREE = f'3'
    FOUR = f'4'
    FIVE = f'5'
    SIX = f'6'
    SEVEN = f'7'
    EIGHT = f'8'
    NINE = f'9'


class LowerCase(Valid):
    """The Lowercase charaters

    For hashes that begin with lowercase letters.
    """
    A = f'a'
    B = f'b'
    C = f'c'
    D = f'd'
    E = f'e'
    F = f'f'
    G = f'g'
    H = f'h'
    I = f'i'
    J = f'j'
    K = f'k'
    L = f'l'
    M = f'm'
    N = f'n'
    O = f'o'
    P = f'p'
    Q = f'q'
    R = f'r'
    S = f's'
    T = f't'
    U = f'u'
    V = f'v'
    W = f'w'
    X = f'x'
    Y = f'y'
    Z = f'z'


class UpperCase(Valid):
    """The Uppercase Characters

    For hashes that begin with an uppercase char.
    """
    A = f'A'
    B = f'B'
    C = f'C'
    D = f'D'
    E = f'E'
    F = f'F'
    G = f'G'
    H = f'H'
    I = f'I'
    J = f'J'
    K = f'K'
    L = f'L'
    M = f'M'
    N = f'N'
    O = f'O'
    P = f'P'
    Q = f'Q'
    R = f'R'
    S = f'S'
    T = f'T'
    U = f'U'
    V = f'V'
    W = f'W'
    X = f'X'
    Y = f'Y'
    Z = f'Z'
