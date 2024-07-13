"""The Lowercase character Table Module

TODO: docs
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

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
        return f'{LowerTables.A.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def b_low() -> str:
        """Get the full table name for hash[b:]"""
        return f'{LowerTables.B.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def c_low() -> str:
        """Get the full table name for hash[c:]"""
        return f'{LowerTables.C.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def d_low() -> str:
        """Get the full table name for hash[d:]"""
        return f'{LowerTables.D.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def e_low() -> str:
        """Get the full table name for hash[e:]"""
        return f'{LowerTables.E.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def f_low() -> str:
        """Get the full table name for hash[f:]"""
        return f'{LowerTables.F.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def g_low() -> str:
        """Get the full table name for hash[g:]"""
        return f'{LowerTables.G.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def h_low() -> str:
        """Get the full table name for hash[h:]"""
        return f'{LowerTables.H.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def i_low() -> str:
        """Get the full table name for hash[i:]"""
        return f'{LowerTables.I.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def j_low() -> str:
        """Get the full table name for hash[j:]"""
        return f'{LowerTables.J.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def k_low() -> str:
        """Get the full table name for hash[k:]"""
        return f'{LowerTables.K.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def l_low() -> str:
        """Get the full table name for hash[l:]"""
        return f'{LowerTables.L.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def m_low() -> str:
        """Get the full table name for hash[m:]"""
        return f'{LowerTables.M.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def n_low() -> str:
        """Get the full table name for hash[n:]"""
        return f'{LowerTables.N.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def o_low() -> str:
        """Get the full table name for hash[o:]"""
        return f'{LowerTables.O.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def p_low() -> str:
        """Get the full table name for hash[p:]"""
        return f'{LowerTables.P.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def q_low() -> str:
        """Get the full table name for hash[q:]"""
        return f'{LowerTables.Q.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def r_low() -> str:
        """Get the full table name for hash[r:]"""
        return f'{LowerTables.R.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def s_low() -> str:
        """Get the full table name for hash[s:]"""
        return f'{LowerTables.S.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def t_low() -> str:
        """Get the full table name for hash[t:]"""
        return f'{LowerTables.T.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def u_low() -> str:
        """Get the full table name for hash[u:]"""
        return f'{LowerTables.U.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def v_low() -> str:
        """Get the full table name for hash[v:]"""
        return f'{LowerTables.V.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def w_low() -> str:
        """Get the full table name for hash[w:]"""
        return f'{LowerTables.W.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def x_low() -> str:
        """Get the full table name for hash[x:]"""
        return f'{LowerTables.X.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def y_low() -> str:
        """Get the full table name for hash[y:]"""
        return f'{LowerTables.Y.value.decode()}{Names.LOW.value}{Names.HASH.value}'

    @staticmethod
    def z_low() -> str:
        """Get the full table name for hash[z:]"""
        return f'{LowerTables.Z.value.decode()}{Names.LOW.value}{Names.HASH.value}'
