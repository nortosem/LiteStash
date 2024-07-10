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
    ZFD = 'zfd.db'
    FND = 'fnd.db'
    AEL = 'ael.db'
    FIL = 'fil.db'
    JML = 'jml.db'
    NRL = 'nrl.db'
    SVL = 'svl.db'
    WZL = 'wzl.db'
    AEU = 'ael.db'
    FIU = 'fiu.db'
    JMU = 'jmu.db'
    NRU = 'nru.db'
    SVU = 'svu.db'
    WZU = 'wzu.db'

    @staticmethod
    def db_zft():
        """Filename for database with hashes that start with 0-4"""
        return f'{Names.ZFD.value}'

    @staticmethod
    def db_fnt():
        """Filename for database with hashes that start with 5-9"""
        return f'{Names.FND.value}'

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

    @staticmethod
    def db_svl():
        """Filename for database with hashes that start with s-v"""
        return f'{Names.SVL.value}'

    @staticmethod
    def db_wzl():
        """Filename for database with hashes that start with w-z"""
        return f'{Names.WZL.value}'


class Digitables(Valid):
    """Digitables

    The table prefix for hashes that start with a digit.
    """
    ZERO = '0'
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'

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
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'
    G = 'g'
    H = 'h'
    I = 'i'
    J = 'j'
    K = 'k'
    L = 'l'
    M = 'm'
    N = 'n'
    O = 'o'
    P = 'p'
    Q = 'q'
    R = 'r'
    S = 's'
    T = 't'
    U = 'u'
    V = 'v'
    W = 'w'
    X = 'x'
    Y = 'y'
    Z = 'z'

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
    def s_low() -> str:
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


class UpperTables(Valid):
    """Uppertables

    The table prefix for hashes that start with an uppercase letter.
    """
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'

    @staticmethod
    def A_upper() -> str:
        """Get the full table name for hash[A:]"""
        return f'{UpperTables.A.value}{Names.HASH.value}'

    @staticmethod
    def B_upper() -> str:
        """Get the full table name for hash[B:]"""
        return f'{UpperTables.B.value}{Names.HASH.value}'

    @staticmethod
    def c_upper() -> str:
        """Get the full table name for hash[C:]"""
        return f'{UpperTables.C.value}{Names.HASH.value}'

    @staticmethod
    def d_upper() -> str:
        """Get the full table name for hash[D:]"""
        return f'{UpperTables.D.value}{Names.HASH.value}'

    @staticmethod
    def e_upper() -> str:
        """Get the full table name for hash[E:]"""
        return f'{UpperTables.E.value}{Names.HASH.value}'

    @staticmethod
    def f_upper() -> str:
        """Get the full table name for hash[F:]"""
        return f'{UpperTables.F.value}{Names.HASH.value}'

    @staticmethod
    def g_upper() -> str:
        """Get the full table name for hash[G:]"""
        return f'{UpperTables.G.value}{Names.HASH.value}'

    @staticmethod
    def h_upper() -> str:
        """Get the full table name for hash[H:]"""
        return f'{UpperTables.H.value}{Names.HASH.value}'

    @staticmethod
    def i_upper() -> str:
        """Get the full table name for hash[I:]"""
        return f'{UpperTables.I.value}{Names.HASH.value}'

    @staticmethod
    def j_upper() -> str:
        """Get the full table name for hash[J:]"""
        return f'{UpperTables.J.value}{Names.HASH.value}'

    @staticmethod
    def k_upper() -> str:
        """Get the full table name for hash[K:]"""
        return f'{UpperTables.K.value}{Names.HASH.value}'

    @staticmethod
    def l_upper() -> str:
        """Get the full table name for hash[L:]"""
        return f'{UpperTables.L.value}{Names.HASH.value}'

    @staticmethod
    def m_upper() -> str:
        """Get the full table name for hash[M:]"""
        return f'{UpperTables.M.value}{Names.HASH.value}'

    @staticmethod
    def n_upper() -> str:
        """Get the full table name for hash[N:]"""
        return f'{UpperTables.N.value}{Names.HASH.value}'

    @staticmethod
    def o_upper() -> str:
        """Get the full table name for hash[O:]"""
        return f'{UpperTables.O.value}{Names.HASH.value}'

    @staticmethod
    def p_upper() -> str:
        """Get the full table name for hash[P:]"""
        return f'{UpperTables.P.value}{Names.HASH.value}'

    @staticmethod
    def q_upper() -> str:
        """Get the full table name for hash[Q:]"""
        return f'{UpperTables.Q.value}{Names.HASH.value}'

    @staticmethod
    def r_upper() -> str:
        """Get the full table name for hash[R:]"""
        return f'{UpperTables.R.value}{Names.HASH.value}'

    @staticmethod
    def s_upper() -> str:
        """Get the full table name for hash[S:]"""
        return f'{UpperTables.S.value}{Names.HASH.value}'

    @staticmethod
    def t_upper() -> str:
        """Get the full table name for hash[T:]"""
        return f'{UpperTables.T.value}{Names.HASH.value}'

    @staticmethod
    def u_upper() -> str:
        """Get the full table name for hash[U:]"""
        return f'{UpperTables.U.value}{Names.HASH.value}'

    @staticmethod
    def v_upper() -> str:
        """Get the full table name for hash[V:]"""
        return f'{UpperTables.V.value}{Names.HASH.value}'

    @staticmethod
    def w_upper() -> str:
        """Get the full table name for hash[W:]"""
        return f'{UpperTables.W.value}{Names.HASH.value}'

    @staticmethod
    def x_upper() -> str:
        """Get the full table name for hash[X:]"""
        return f'{UpperTables.X.value}{Names.HASH.value}'

    @staticmethod
    def y_upper() -> str:
        """Get the full table name for hash[Y:]"""
        return f'{UpperTables.Y.value}{Names.HASH.value}'

    @staticmethod
    def z_upper() -> str:
        """Get the full table name for hash[Z:]"""
        return f'{UpperTables.Z.value}{Names.HASH.value}'
