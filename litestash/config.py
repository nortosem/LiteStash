"""Package Configuration

The config module enumerates the common required strings.
"""
from enum import Enum
from enum import unique
from typing import Self

class Valid(Enum):
    """Valid Root"""
    pass


class StashSlots(Valid):
    """all slots for the LiteStash"""
    DB_NAME = f'db_name'
    ENGINE = f'engine'
    METADATA = f'metadata'
    DB_SESSION = f'db_session'


class SetupDB(Valid):
    """SetupDB

    Provide the configuation to setup a database engine.
    """
    SQLITE = f'sqlite://'
    DIR_NAME = f'litestash'
    ECHO = True
    FUTURE = True
    NO_ECHO = False
    NO_FUTURE = False

    @staticmethod
    def sqlite() -> str:
        return f'{SetupDB.SQLITE.value}'

    @staticmethod
    def dirname() -> str:
        return f'{SetupDB.DIR_NAME.value}'

    @staticmethod
    def echo() -> str:
        return f'{SetupDB.ECHO.value}'

    @staticmethod
    def future() -> str:
        return f'{SetupDB.FUTURE.value}'

    @staticmethod
    def no_echo() -> str:
        return f'{SetupDB.NO_ECHO.value}'

    @staticmethod
    def no_future() -> str:
        return f'{SetupDB.NO_FUTURE.value}'


class Pragma(Valid):
    """Sqlite Pragma

    The default pragma configuration.
    """
    PRAGMA = f'PRAGMA'
    JOURNAL_MODE = f'journal_mode=WAL'
    SYNCHRONOUS = f'synchronous=NORMAL'
    FOREIGN_KEYS = f'foreign_keys=ON'

    @staticmethod
    def journal_mode() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.JOURNAL_MODE.value}'

    @staticmethod
    def synchronous() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.SYNCHRONOUS.value}'

    @staticmethod
    def foreign_keys() -> str:
        return f'{Pragma.PRAGMA.value} {Pragma.FOREIGN_KEYS.value}'


class ColumnSetup(Valid):
    """The Column Setup

    Define the column attributes for each table
    """
    ROW_ID = f'rowid'
    HASH = f'key_hash'
    KEY = f'key'
    VALUE = f'value'
    TIME = f'timedate'


class Names(Valid):
    """Table & File Names

    Default filenames for each database.
    And suffix for each table in database file.
    """
    HASH = f'_hash'
    ZFT = f'zft.db'
    FNT = f'fnt.db'
    AEL = f'ael.db'
    FIL = f'fil.db'
    JML = f'jml.db'
    NRL = f'nrl.db'
    SVL = f'svl.db'
    WZL = f'wzl.db'
    AEU = f'nzl.db'
    FIU = f'amu.db'
    JMU = f'nzu.db'
    NRU = f'nru.db'
    SVU = f'svu.db'
    WZU = f'wzu.db'


    @staticmethod
    def db_zft():
        """Filename for database with hashes that start with 0-4"""
        return f'{Names.ZFT.value}'

    @staticmethod
    def db_fnt():
        """Filename for database with hashes that start with 5-9"""
        return f'{Names.FNT.value}'

    @staticmethod
    def db_ael():
        """Filename for database with hashes that start with a-e"""
        return f'{Names.AEL.value}'

    @staticmethod
    def db_fil():
        """Filename for database with hashes that start with f-i"""
        return f'{Names.FIL.value}'

    @staticmethod
    def db_jml():
        """Filename for database with hashes that start with j-m"""
        return f'{Names.JML.value}'

    @staticmethod
    def db_nrl():
        """Filename for database with hashes that start with n-r"""
        return f'{Names.NRL.value}'




class Digitables(Valid)
    """Digitables

    The table prefix for hashes that start with a digit.
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

    @staticmethod
    def zero() -> str:
        """Get the full table name for hash[0:]"""
        return f'{Digitables.ZERO.value}{Names.HASH.value}'

    @staticmethod
    def one() -> str:
        """Get the full table name for hash[1:]"""
        return f'{Digitables.ONE.value}{Names.HASH.value}'

    @staticmethod
    def two() -> str:
        """Get the full table name for hash[2:]"""
        return f'{Digitables.TWO.value}{Names.HASH.value}'

    @staticmethod
    def three() -> str:
        """Get the full table name for hash[3:]"""
        return f'{Digitables.THREE.value}{Names.HASH.value}'

    @staticmethod
    def four() -> str:
        """Get the full table name for hash[4:]"""
        return f'{Digitables.FOUR.value}{Names.HASH.value}'

    @staticmethod
    def five() -> str:
        """Get the full table name for hash[5:]"""
        return f'{Digitables.FIVE.value}{Names.HASH.value}'

    @staticmethod
    def six() -> str:
        """Get the full table name for hash[6:]"""
        return f'{Digitables.SIX.value}{Names.HASH.value}'

    @staticmethod
    def seven() -> str:
        """Get the full table name for hash[7:]"""
        return f'{Digitables.SEVEN.value}{Names.HASH.value}'

    @staticmethod
    def eight() -> str:
        """Get the full table name for hash[8:]"""
        return f'{Digitables.EIGHT.value}{Names.HASH.value}'

    @staticmethod
    def nine() -> str:
        """Get the full table name for hash[9:]"""
        return f'{Digitables.NINE.value}{Names.HASH.value}'


class LowerTables(Valid):
    """Lowertables

    The table prefix for hashes that start with a lowercase letter.
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

    @staticmethod
    def a_low() -> str:
        """Get the full table name for hash[a:]"""
        return f'{LowerTables.A.value}{Names.HASH.value}'

    @staticmethod
    def b_low() -> str:
        """Get the full table name for hash[b:]"""
        return f'{LowerTables.B.value}{Names.HASH.value}'

    @staticmethod
    def c_low() -> str:
        """Get the full table name for hash[c:]"""
        return f'{LowerTables.C.value}{Names.HASH.value}'

    @staticmethod
    def d_low() -> str:
        """Get the full table name for hash[d:]"""
        return f'{LowerTables.D.value}{Names.HASH.value}'

    @staticmethod
    def e_low() -> str:
        """Get the full table name for hash[e:]"""
        return f'{LowerTables.E.value}{Names.HASH.value}'

    @staticmethod
    def f_low() -> str:
        """Get the full table name for hash[f:]"""
        return f'{LowerTables.F.value}{Names.HASH.value}'

    @staticmethod
    def g_low() -> str:
        """Get the full table name for hash[g:]"""
        return f'{LowerTables.G.value}{Names.HASH.value}'

    @staticmethod
    def h_low() -> str:
        """Get the full table name for hash[h:]"""
        return f'{LowerTables.H.value}{Names.HASH.value}'

    @staticmethod
    def i_low() -> str:
        """Get the full table name for hash[i:]"""
        return f'{LowerTables.I.value}{Names.HASH.value}'

    @staticmethod
    def j_low() -> str:
        """Get the full table name for hash[j:]"""
        return f'{LowerTables.J.value}{Names.HASH.value}'

    @staticmethod
    def k_low() -> str:
        """Get the full table name for hash[k:]"""
        return f'{LowerTables.K.value}{Names.HASH.value}'

    @staticmethod
    def l_low() -> str:
        """Get the full table name for hash[l:]"""
        return f'{LowerTables.L.value}{Names.HASH.value}'

    @staticmethod
    def m_low() -> str:
        """Get the full table name for hash[m:]"""
        return f'{LowerTables.M.value}{Names.HASH.value}'

    @staticmethod
    def n_low() -> str:
        """Get the full table name for hash[n:]"""
        return f'{LowerTables.N.value}{Names.HASH.value}'

    @staticmethod
    def o_low() -> str:
        """Get the full table name for hash[o:]"""
        return f'{LowerTables.O.value}{Names.HASH.value}'

    @staticmethod
    def p_low() -> str:
        """Get the full table name for hash[p:]"""
        return f'{LowerTables.P.value}{Names.HASH.value}'

    @staticmethod
    def q_low() -> str:
        """Get the full table name for hash[q:]"""
        return f'{LowerTables.Q.value}{Names.HASH.value}'

    @staticmethod
    def r_low() -> str:
        """Get the full table name for hash[r:]"""
        return f'{LowerTables.R.value}{Names.HASH.value}'

    @staticmethod
    def s_low()v -> str:
        """Get the full table name for hash[s:]"""
        return f'{LowerTables.S.value}{Names.HASH.value}'

    @staticmethod
    def t_low() -> str:
        """Get the full table name for hash[t:]"""
        return f'{LowerTables.T.value}{Names.HASH.value}'

    @staticmethod
    def u_low() -> str:
        """Get the full table name for hash[u:]"""
        return f'{LowerTables.U.value}{Names.HASH.value}'

    @staticmethod
    def v_low() -> str:
        """Get the full table name for hash[v:]"""
        return f'{LowerTables.V.value}{Names.HASH.value}'

    @staticmethod
    def w_low() -> str:
        """Get the full table name for hash[w:]"""
        return f'{LowerTables.W.value}{Names.HASH.value}'

    @staticmethod
    def x_low() -> str:
        """Get the full table name for hash[x:]"""
        return f'{LowerTables.X.value}{Names.HASH.value}'

    @staticmethod
    def y_low() -> str:
        """Get the full table name for hash[y:]"""
        return f'{LowerTables.Y.value}{Names.HASH.value}'

    @staticmethod
    def z_low() -> str:
        """Get the full table name for hash[z:]"""
        return f'{LowerTables.Z.value}{Names.HASH.value}'


class Uppertables(Valid):
    """Uppertables

    The table prefix for hashes that start with an uppercase letter.
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


    @staticmethod
    def A_upper() -> str:
        """Get the full table name for hash[A:]"""
        return f'{LowerTables.A.value}{Names.HASH.value}'

    @staticmethod
    def B_upper() -> str:
        """Get the full table name for hash[B:]"""
        return f'{LowerTables.B.value}{Names.HASH.value}'

    @staticmethod
    def c_upper() -> str:
        """Get the full table name for hash[C:]"""
        return f'{LowerTables.C.value}{Names.HASH.value}'

    @staticmethod
    def d_upper() -> str:
        """Get the full table name for hash[D:]"""
        return f'{LowerTables.D.value}{Names.HASH.value}'

    @staticmethod
    def e_upper() -> str:
        """Get the full table name for hash[E:]"""
        return f'{LowerTables.E.value}{Names.HASH.value}'

    @staticmethod
    def f_upper() -> str:
        """Get the full table name for hash[F:]"""
        return f'{LowerTables.F.value}{Names.HASH.value}'

    @staticmethod
    def g_upper() -> str:
        """Get the full table name for hash[G:]"""
        return f'{LowerTables.G.value}{Names.HASH.value}'

    @staticmethod
    def h_upper() -> str:
        """Get the full table name for hash[H:]"""
        return f'{LowerTables.H.value}{Names.HASH.value}'

    @staticmethod
    def i_upper() -> str:
        """Get the full table name for hash[I:]"""
        return f'{LowerTables.I.value}{Names.HASH.value}'

    @staticmethod
    def j_upper() -> str:
        """Get the full table name for hash[J:]"""
        return f'{LowerTables.J.value}{Names.HASH.value}'

    @staticmethod
    def k_upper() -> str:
        """Get the full table name for hash[K:]"""
        return f'{LowerTables.K.value}{Names.HASH.value}'

    @staticmethod
    def l_upper() -> str:
        """Get the full table name for hash[L:]"""
        return f'{LowerTables.L.value}{Names.HASH.value}'

    @staticmethod
    def m_upper() -> str:
        """Get the full table name for hash[M:]"""
        return f'{LowerTables.M.value}{Names.HASH.value}'

    @staticmethod
    def n_upper() -> str:
        """Get the full table name for hash[N:]"""
        return f'{LowerTables.N.value}{Names.HASH.value}'

    @staticmethod
    def o_upper() -> str:
        """Get the full table name for hash[O:]"""
        return f'{LowerTables.O.value}{Names.HASH.value}'

    @staticmethod
    def p_upper() -> str:
        """Get the full table name for hash[P:]"""
        return f'{LowerTables.P.value}{Names.HASH.value}'

    @staticmethod
    def q_upper() -> str:
        """Get the full table name for hash[Q:]"""
        return f'{LowerTables.Q.value}{Names.HASH.value}'

    @staticmethod
    def r_upper() -> str:
        """Get the full table name for hash[R:]"""
        return f'{LowerTables.R.value}{Names.HASH.value}'

    @staticmethod
    def s_upper()v -> str:
        """Get the full table name for hash[S:]"""
        return f'{LowerTables.S.value}{Names.HASH.value}'

    @staticmethod
    def t_upper() -> str:
        """Get the full table name for hash[T:]"""
        return f'{LowerTables.T.value}{Names.HASH.value}'

    @staticmethod
    def u_upper() -> str:
        """Get the full table name for hash[U:]"""
        return f'{LowerTables.U.value}{Names.HASH.value}'

    @staticmethod
    def v_upper() -> str:
        """Get the full table name for hash[V:]"""
        return f'{LowerTables.V.value}{Names.HASH.value}'

    @staticmethod
    def w_upper() -> str:
        """Get the full table name for hash[W:]"""
        return f'{LowerTables.W.value}{Names.HASH.value}'

    @staticmethod
    def x_upper() -> str:
        """Get the full table name for hash[X:]"""
        return f'{LowerTables.X.value}{Names.HASH.value}'

    @staticmethod
    def y_upper() -> str:
        """Get the full table name for hash[Y:]"""
        return f'{LowerTables.Y.value}{Names.HASH.value}'

    @staticmethod
    def z_upper() -> str:
        """Get the full table name for hash[Z:]"""
        return f'{LowerTables.Z.value}{Names.HASH.value}'
