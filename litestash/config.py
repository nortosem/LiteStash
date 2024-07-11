"""Package Configuration

The config module enumerates the common required strings.
#from pydantic import ValidationError, validator
"""
from enum import Enum

class Valid(Enum):
    """Valid Root"""
    pass


class Utils(Valid):
    """Defaults for util functions

    SIZE (int): digest_size for hash_key
    """
    SIZE = 17
    DB_NAME_ERROR = 'Invalid character'


class DataScheme(Valid):
    """LiteStashData Scheme

    Define the config and schema for the data transfer object.
    """
    TITLE = 'Data'
    DESCRIPTION = 'The key name and JSON data for the given key.'
    MIN_LENGTH = 4
    MAX_LENGTH = 41
    FORBID_EXTRA = 'forbid'


class EngineStash(Valid):
    """The namedtuple config for all engine attributes of a LiteStash"""
    TYPE_NAME = 'StashEngine'
    DB_NAME = 'db_name'
    ENGINE = 'engine'
    DOC = '''Defines a named tuple for tuple returned by utils.setup_engine.
    Attributes:
        db_name (str): name of the database for this engine
        engine (Engine): the sqlalchemy engine itself
    '''
    VALUE_ERROR = 'No such engine found'


class MetaStash(Valid):
    """The namedtuple config for all metadata attributes of a LiteStash"""
    TYPE_NAME = 'StashMeta'
    DB_NAME = f'{EngineStash.DB_NAME.value}'
    METADATA = 'metadata'
    DOC = '''todo'''

class SessionStash(Valid):
    """The namedtuple config for all session attribues of a LiteStash """
    TYPE_NAME = 'StashSession'
    DB_NAME = f'{EngineStash.DB_NAME.value}'
    SESSION = 'session'
    VALUE_ERROR = 'Invalid database: no tables found'
    DOC = '''todo'''


class MetaSlots(Valid):
    """Slots for the LiteStashMetadata"""
    ZFD = 'zfd'
    FND = 'fnd'
    AEL = 'ael'
    FIL = 'fil'
    JML = 'jml'
    NRL = 'nrl'
    SVL = 'svl'
    WZL = 'wzl'
    AEU = 'aeu'
    FIU = 'fiu'
    JMU = 'jmu'
    NRU = 'nru'
    SVU = 'svu'
    WZU = 'wzu'

class StashSlots(Valid):
    """all slots for the LiteStash"""
    ENGINE = 'engine'
    METADATA = 'metadata'
    DB_SESSION = 'db_session'


class SetupDB(Valid):
    """SetupDB

    Provide the configuation to setup a database engine.
    """
    SQLITE = 'sqlite://'
    DIR_NAME = 'litestash'
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


class FTS5(Valid):
    """SQL Text for FTS5 setup"""
    TABLE_PREFIX = 'fts_'
    MK_TABLE = 'CREATE VIRTUAL TABLE IF NOT EXISTS'
    USING = 'USING'
    OPEN = 'fts5('
    CONTENT = 'content='
    ROW_ID = 'content_rowid='
    CLOSE = ');'
    MK_TRIGGER = 'CREATE TRIGGER IF NOT EXISTS'
    NEW = 'new.'
    AFTER_INSERT = 'AFTER INSERT ON'
    AFTER_UPDATE = 'AFTER UPDATE ON'
    AFTER_DELETE = 'AFTER DELETE ON'
    BEGIN_INSERT = 'BEGIN INSERT INTO'
    VALUES = 'VALUES'
    END = 'END;'


class GetKey(Valid):
    """The SQL for a Get

    """

class Pragma(Valid):
    """Sqlite Pragma

    The default pragma configuration.
    """
    PRAGMA = 'PRAGMA'
    JOURNAL_MODE = 'journal_mode=WAL'
    SYNCHRONOUS = 'synchronous=NORMAL'
    FOREIGN_KEYS = 'foreign_keys=ON'

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
    HASH = 'key_hash'
    KEY = 'key'
    VALUE = 'value'
    TIME = 'timedate'


class Names(Valid):
    """Database filenames

    Default filenames for each database.
    Also the Table name suffix as HASH
    """
    HASH = '_hash'
    ZFD = b'zfd.db'
    FND = b'fnd.db'
    AEL = b'ael.db'
    FIL = b'fil.db'
    JML = b'jml.db'
    NRL = b'nrl.db'
    SVL = b'svl.db'
    WZL = b'wzl.db'
    AEU = b'ael.db'
    FIU = b'fiu.db'
    JMU = b'jmu.db'
    NRU = b'nru.db'
    SVU = b'svu.db'
    WZU = b'wzu.db'

    @staticmethod
    def db_zft():
        """Filename for database with hashes that start with 0-4"""
        return f'{Names.ZFD.value.decode()}'

    @staticmethod
    def db_fnt():
        """Filename for database with hashes that start with 5-9"""
        return f'{Names.FND.value.decode()}'

    @staticmethod
    def db_ael():
        """Filename for database with hashes that start with a-e"""
        return f'{Names.AEL.value.decode()}'

    @staticmethod
    def db_fil():
        """Filename for database with hashes that start with f-i"""
        return f'{Names.FIL.value.decode()}'

    @staticmethod
    def db_jml():
        """Filename for database with hashes that start with j-m"""
        return f'{Names.JML.value.decode()}'

    @staticmethod
    def db_nrl():
        """Filename for database with hashes that start with n-r"""
        return f'{Names.NRL.value.decode()}'

    @staticmethod
    def db_svl():
        """Filename for database with hashes that start with s-v"""
        return f'{Names.SVL.value.decode()}'

    @staticmethod
    def db_wzl():
        """Filename for database with hashes that start with w-z"""
        return f'{Names.WZL.value.decode()}'


class Digitables(Valid):
    """Digitables

    The table prefix for hashes that start with a digit.
    """
    ZERO = b'0'
    ONE = b'1'
    TWO = b'2'
    THREE = b'3'
    FOUR = b'4'
    FIVE = b'5'
    SIX = b'6'
    SEVEN = b'7'
    EIGHT = b'8'
    NINE = b'9'

    @staticmethod
    def get_table_name(char: bytes) -> str:
        """Match on char and return table name"""
        match char:
            case Digitables.ZERO.value:
                return Digitables.zero()
            case Digitables.ONE.value:
                return Digitables.one()
            case Digitables.TWO.value:
                return Digitables.two()
            case Digitables.THREE.value:
                return Digitables.three()
            case Digitables.FOUR.value:
                return Digitables.four()
            case Digitables.FIVE.value:
                return Digitables.five()
            case Digitables.SIX.value:
                return Digitables.six()
            case Digitables.SEVEN.value:
                return Digitables.seven()
            case Digitables.EIGHT.value:
                return Digitables.eight()
            case Digitables.NINE.value:
                return Digitables.nine()
            case _:
                raise ValueError('NO!')

    @staticmethod
    def zero() -> str:
        """Get the full table name for hash[0:]"""
        return f'{Digitables.ZERO.value.decode()}{Names.HASH.value}'

    @staticmethod
    def one() -> str:
        """Get the full table name for hash[1:]"""
        return f'{Digitables.ONE.value.decode()}{Names.HASH.value}'

    @staticmethod
    def two() -> str:
        """Get the full table name for hash[2:]"""
        return f'{Digitables.TWO.value.decode()}{Names.HASH.value}'

    @staticmethod
    def three() -> str:
        """Get the full table name for hash[3:]"""
        return f'{Digitables.THREE.value.decode()}{Names.HASH.value}'

    @staticmethod
    def four() -> str:
        """Get the full table name for hash[4:]"""
        return f'{Digitables.FOUR.value.decode()}{Names.HASH.value}'

    @staticmethod
    def five() -> str:
        """Get the full table name for hash[5:]"""
        return f'{Digitables.FIVE.value.decode()}{Names.HASH.value}'

    @staticmethod
    def six() -> str:
        """Get the full table name for hash[6:]"""
        return f'{Digitables.SIX.value.decode()}{Names.HASH.value}'

    @staticmethod
    def seven() -> str:
        """Get the full table name for hash[7:]"""
        return f'{Digitables.SEVEN.value.decode()}{Names.HASH.value}'

    @staticmethod
    def eight() -> str:
        """Get the full table name for hash[8:]"""
        return f'{Digitables.EIGHT.value.decode()}{Names.HASH.value}'

    @staticmethod
    def nine() -> str:
        """Get the full table name for hash[9:]"""
        return f'{Digitables.NINE.value.decode()}{Names.HASH.value}'


class LowerTables(Valid):
    """Lowertables

    The table prefix for hashes that start with a lowercase letter.
    """
    A = b'a'
    B = b'b'
    C = b'c'
    D = b'd'
    E = b'e'
    F = b'f'
    G = b'g'
    H = b'h'
    I = b'i'
    J = b'j'
    K = b'k'
    L = b'l'
    M = b'm'
    N = b'n'
    O = b'o'
    P = b'p'
    Q = b'q'
    R = b'r'
    S = b's'
    T = b't'
    U = b'u'
    V = b'v'
    W = b'w'
    X = b'x'
    Y = b'y'
    Z = b'z'

    @staticmethod
    def get_table_name(char: bytes) -> str:
        """Get the table name by match on given char"""
        match char:
            case LowerTables.A.value:
                return LowerTables.a_low()
            case LowerTables.B.value:
                return LowerTables.b_low()
            case LowerTables.C.value:
                return LowerTables.c_low()
            case LowerTables.D.value:
                return LowerTables.d_low()
            case LowerTables.E.value:
                return LowerTables.e_low()
            case LowerTables.F.value:
                return LowerTables.f_low()
            case LowerTables.G.value:
                return LowerTables.g_low()
            case LowerTables.H.value:
                return LowerTables.h_low()
            case LowerTables.I.value:
                return LowerTables.i_low()
            case LowerTables.J.value:
                return LowerTables.j_low()
            case LowerTables.K.value:
                return LowerTables.k_low()
            case LowerTables.L.value:
                return LowerTables.l_low()
            case LowerTables.M.value:
                return LowerTables.m_low()
            case LowerTables.N.value:
                return LowerTables.n_low()
            case LowerTables.O.value:
                return LowerTables.o_low()
            case LowerTables.P.value:
                return LowerTables.p_low()
            case LowerTables.Q.value:
                return LowerTables.q_low()
            case LowerTables.R.value:
                return LowerTables.r_low()
            case LowerTables.S.value:
                return LowerTables.s_low()
            case LowerTables.T.value:
                return LowerTables.t_low()
            case LowerTables.U.value:
                return LowerTables.u_low()
            case LowerTables.V.value:
                return LowerTables.v_low()
            case LowerTables.W.value:
                return LowerTables.w_low()
            case LowerTables.X.value:
                return LowerTables.x_low()
            case LowerTables.Y.value:
                return LowerTables.y_low()
            case LowerTables.Z.value:
                return LowerTables.z_low()
            case _:
                raise ValueError('NO!')

    @staticmethod
    def a_low() -> str:
        """Get the full table name for hash[a:]"""
        return f'{LowerTables.A.value.decode()}{Names.HASH.value}'

    @staticmethod
    def b_low() -> str:
        """Get the full table name for hash[b:]"""
        return f'{LowerTables.B.value.decode()}{Names.HASH.value}'

    @staticmethod
    def c_low() -> str:
        """Get the full table name for hash[c:]"""
        return f'{LowerTables.C.value.decode()}{Names.HASH.value}'

    @staticmethod
    def d_low() -> str:
        """Get the full table name for hash[d:]"""
        return f'{LowerTables.D.value.decode()}{Names.HASH.value}'

    @staticmethod
    def e_low() -> str:
        """Get the full table name for hash[e:]"""
        return f'{LowerTables.E.value.decode()}{Names.HASH.value}'

    @staticmethod
    def f_low() -> str:
        """Get the full table name for hash[f:]"""
        return f'{LowerTables.F.value.decode()}{Names.HASH.value}'

    @staticmethod
    def g_low() -> str:
        """Get the full table name for hash[g:]"""
        return f'{LowerTables.G.value.decode()}{Names.HASH.value}'

    @staticmethod
    def h_low() -> str:
        """Get the full table name for hash[h:]"""
        return f'{LowerTables.H.value.decode()}{Names.HASH.value}'

    @staticmethod
    def i_low() -> str:
        """Get the full table name for hash[i:]"""
        return f'{LowerTables.I.value.decode()}{Names.HASH.value}'

    @staticmethod
    def j_low() -> str:
        """Get the full table name for hash[j:]"""
        return f'{LowerTables.J.value.decode()}{Names.HASH.value}'

    @staticmethod
    def k_low() -> str:
        """Get the full table name for hash[k:]"""
        return f'{LowerTables.K.value.decode()}{Names.HASH.value}'

    @staticmethod
    def l_low() -> str:
        """Get the full table name for hash[l:]"""
        return f'{LowerTables.L.value.decode()}{Names.HASH.value}'

    @staticmethod
    def m_low() -> str:
        """Get the full table name for hash[m:]"""
        return f'{LowerTables.M.value.decode()}{Names.HASH.value}'

    @staticmethod
    def n_low() -> str:
        """Get the full table name for hash[n:]"""
        return f'{LowerTables.N.value.decode()}{Names.HASH.value}'

    @staticmethod
    def o_low() -> str:
        """Get the full table name for hash[o:]"""
        return f'{LowerTables.O.value.decode()}{Names.HASH.value}'

    @staticmethod
    def p_low() -> str:
        """Get the full table name for hash[p:]"""
        return f'{LowerTables.P.value.decode()}{Names.HASH.value}'

    @staticmethod
    def q_low() -> str:
        """Get the full table name for hash[q:]"""
        return f'{LowerTables.Q.value.decode()}{Names.HASH.value}'

    @staticmethod
    def r_low() -> str:
        """Get the full table name for hash[r:]"""
        return f'{LowerTables.R.value.decode()}{Names.HASH.value}'

    @staticmethod
    def s_low() -> str:
        """Get the full table name for hash[s:]"""
        return f'{LowerTables.S.value.decode()}{Names.HASH.value}'

    @staticmethod
    def t_low() -> str:
        """Get the full table name for hash[t:]"""
        return f'{LowerTables.T.value.decode()}{Names.HASH.value}'

    @staticmethod
    def u_low() -> str:
        """Get the full table name for hash[u:]"""
        return f'{LowerTables.U.value.decode()}{Names.HASH.value}'

    @staticmethod
    def v_low() -> str:
        """Get the full table name for hash[v:]"""
        return f'{LowerTables.V.value.decode()}{Names.HASH.value}'

    @staticmethod
    def w_low() -> str:
        """Get the full table name for hash[w:]"""
        return f'{LowerTables.W.value.decode()}{Names.HASH.value}'

    @staticmethod
    def x_low() -> str:
        """Get the full table name for hash[x:]"""
        return f'{LowerTables.X.value.decode()}{Names.HASH.value}'

    @staticmethod
    def y_low() -> str:
        """Get the full table name for hash[y:]"""
        return f'{LowerTables.Y.value.decode()}{Names.HASH.value}'

    @staticmethod
    def z_low() -> str:
        """Get the full table name for hash[z:]"""
        return f'{LowerTables.Z.value.decode()}{Names.HASH.value}'


class UpperTables(Valid):
    """Uppertables

    The table prefix for hashes that start with an uppercase letter.
    """
    A = b'A'
    B = b'B'
    C = b'C'
    D = b'D'
    E = b'E'
    F = b'F'
    G = b'G'
    H = b'H'
    I = b'I'
    J = b'J'
    K = b'K'
    L = b'L'
    M = b'M'
    N = b'N'
    O = b'O'
    P = b'P'
    Q = b'Q'
    R = b'R'
    S = b'S'
    T = b'T'
    U = b'U'
    V = b'V'
    W = b'W'
    X = b'X'
    Y = b'Y'
    Z = b'Z'

    @staticmethod
    def get_table_name(char: bytes) -> str:
        """Get the table name by match on given char"""
        match char:
            case UpperTables.A.value:
                return UpperTables.a_upper()
            case UpperTables.B.value:
                return UpperTables.b_upper()
            case UpperTables.C.value:
                return UpperTables.c_upper()
            case UpperTables.D.value:
                return UpperTables.d_upper()
            case UpperTables.E.value:
                return UpperTables.e_upper()
            case UpperTables.F.value:
                return UpperTables.f_upper()
            case UpperTables.G.value:
                return UpperTables.g_upper()
            case UpperTables.H.value:
                return UpperTables.h_upper()
            case UpperTables.I.value:
                return UpperTables.i_upper()
            case UpperTables.J.value:
                return UpperTables.j_upper()
            case UpperTables.K.value:
                return UpperTables.k_upper()
            case UpperTables.L.value:
                return UpperTables.l_upper()
            case UpperTables.M.value:
                return UpperTables.m_upper()
            case UpperTables.N.value:
                return UpperTables.n_upper()
            case UpperTables.O.value:
                return UpperTables.o_upper()
            case UpperTables.P.value:
                return UpperTables.p_upper()
            case UpperTables.Q.value:
                return UpperTables.q_upper()
            case UpperTables.R.value:
                return UpperTables.r_upper()
            case UpperTables.S.value:
                return UpperTables.s_upper()
            case UpperTables.T.value:
                return UpperTables.t_upper()
            case UpperTables.U.value:
                return UpperTables.u_upper()
            case UpperTables.V.value:
                return UpperTables.v_upper()
            case UpperTables.W.value:
                return UpperTables.w_upper()
            case UpperTables.X.value:
                return UpperTables.x_upper()
            case UpperTables.Y.value:
                return UpperTables.y_upper()
            case UpperTables.Z.value:
                return UpperTables.z_upper()
            case _:
                raise ValueError('NO!')

    @staticmethod
    def a_upper() -> str:
        """Get the full table name for hash[A:]"""
        return f'{UpperTables.A.value.decode()}{Names.HASH.value}'

    @staticmethod
    def b_upper() -> str:
        """Get the full table name for hash[B:]"""
        return f'{UpperTables.B.value.decode()}{Names.HASH.value}'

    @staticmethod
    def c_upper() -> str:
        """Get the full table name for hash[C:]"""
        return f'{UpperTables.C.value.decode()}{Names.HASH.value}'

    @staticmethod
    def d_upper() -> str:
        """Get the full table name for hash[D:]"""
        return f'{UpperTables.D.value.decode()}{Names.HASH.value}'

    @staticmethod
    def e_upper() -> str:
        """Get the full table name for hash[E:]"""
        return f'{UpperTables.E.value.decode()}{Names.HASH.value}'

    @staticmethod
    def f_upper() -> str:
        """Get the full table name for hash[F:]"""
        return f'{UpperTables.F.value.decode()}{Names.HASH.value}'

    @staticmethod
    def g_upper() -> str:
        """Get the full table name for hash[G:]"""
        return f'{UpperTables.G.value.decode()}{Names.HASH.value}'

    @staticmethod
    def h_upper() -> str:
        """Get the full table name for hash[H:]"""
        return f'{UpperTables.H.value.decode()}{Names.HASH.value}'

    @staticmethod
    def i_upper() -> str:
        """Get the full table name for hash[I:]"""
        return f'{UpperTables.I.value.decode()}{Names.HASH.value}'

    @staticmethod
    def j_upper() -> str:
        """Get the full table name for hash[J:]"""
        return f'{UpperTables.J.value.decode()}{Names.HASH.value}'

    @staticmethod
    def k_upper() -> str:
        """Get the full table name for hash[K:]"""
        return f'{UpperTables.K.value.decode()}{Names.HASH.value}'

    @staticmethod
    def l_upper() -> str:
        """Get the full table name for hash[L:]"""
        return f'{UpperTables.L.value.decode()}{Names.HASH.value}'

    @staticmethod
    def m_upper() -> str:
        """Get the full table name for hash[M:]"""
        return f'{UpperTables.M.value.decode()}{Names.HASH.value}'

    @staticmethod
    def n_upper() -> str:
        """Get the full table name for hash[N:]"""
        return f'{UpperTables.N.value.decode()}{Names.HASH.value}'

    @staticmethod
    def o_upper() -> str:
        """Get the full table name for hash[O:]"""
        return f'{UpperTables.O.value.decode()}{Names.HASH.value}'

    @staticmethod
    def p_upper() -> str:
        """Get the full table name for hash[P:]"""
        return f'{UpperTables.P.value.decode()}{Names.HASH.value}'

    @staticmethod
    def q_upper() -> str:
        """Get the full table name for hash[Q:]"""
        return f'{UpperTables.Q.value.decode()}{Names.HASH.value}'

    @staticmethod
    def r_upper() -> str:
        """Get the full table name for hash[R:]"""
        return f'{UpperTables.R.value.decode()}{Names.HASH.value}'

    @staticmethod
    def s_upper() -> str:
        """Get the full table name for hash[S:]"""
        return f'{UpperTables.S.value.decode()}{Names.HASH.value}'

    @staticmethod
    def t_upper() -> str:
        """Get the full table name for hash[T:]"""
        return f'{UpperTables.T.value.decode()}{Names.HASH.value}'

    @staticmethod
    def u_upper() -> str:
        """Get the full table name for hash[U:]"""
        return f'{UpperTables.U.value.decode()}{Names.HASH.value}'

    @staticmethod
    def v_upper() -> str:
        """Get the full table name for hash[V:]"""
        return f'{UpperTables.V.value.decode()}{Names.HASH.value}'

    @staticmethod
    def w_upper() -> str:
        """Get the full table name for hash[W:]"""
        return f'{UpperTables.W.value.decode()}{Names.HASH.value}'

    @staticmethod
    def x_upper() -> str:
        """Get the full table name for hash[X:]"""
        return f'{UpperTables.X.value.decode()}{Names.HASH.value}'

    @staticmethod
    def y_upper() -> str:
        """Get the full table name for hash[Y:]"""
        return f'{UpperTables.Y.value.decode()}{Names.HASH.value}'

    @staticmethod
    def z_upper() -> str:
        """Get the full table name for hash[Z:]"""
        return f'{UpperTables.Z.value.decode()}{Names.HASH.value}'
