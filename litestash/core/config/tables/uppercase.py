"""The Uppercase character Table Module

TODO: docs
"""
from litestash.core.config.root import Valid
from litestash.core.config.schema_conf import Names

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
        return(
            f'{UpperTables.A.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def b_upper() -> str:
        """Get the full table name for hash[B:]"""
        return(
            f'{UpperTables.B.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def c_upper() -> str:
        """Get the full table name for hash[C:]"""
        return(
            f'{UpperTables.C.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def d_upper() -> str:
        """Get the full table name for hash[D:]"""
        return(
            f'{UpperTables.D.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def e_upper() -> str:
        """Get the full table name for hash[E:]"""
        return(
            f'{UpperTables.E.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def f_upper() -> str:
        """Get the full table name for hash[F:]"""
        return(
            f'{UpperTables.F.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def g_upper() -> str:
        """Get the full table name for hash[G:]"""
        return(
            f'{UpperTables.G.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def h_upper() -> str:
        """Get the full table name for hash[H:]"""
        return(
            f'{UpperTables.H.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def i_upper() -> str:
        """Get the full table name for hash[I:]"""
        return(
            f'{UpperTables.I.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def j_upper() -> str:
        """Get the full table name for hash[J:]"""
        return(
            f'{UpperTables.J.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def k_upper() -> str:
        """Get the full table name for hash[K:]"""
        return(
            f'{UpperTables.K.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def l_upper() -> str:
        """Get the full table name for hash[L:]"""
        return(
            f'{UpperTables.L.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def m_upper() -> str:
        """Get the full table name for hash[M:]"""
        return(
            f'{UpperTables.M.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def n_upper() -> str:
        """Get the full table name for hash[N:]"""
        return(
            f'{UpperTables.N.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def o_upper() -> str:
        """Get the full table name for hash[O:]"""
        return(
            f'{UpperTables.O.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def p_upper() -> str:
        """Get the full table name for hash[P:]"""
        return(
            f'{UpperTables.P.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def q_upper() -> str:
        """Get the full table name for hash[Q:]"""
        return(
            f'{UpperTables.Q.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def r_upper() -> str:
        """Get the full table name for hash[R:]"""
        return(
            f'{UpperTables.R.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def s_upper() -> str:
        """Get the full table name for hash[S:]"""
        return(
            f'{UpperTables.S.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def t_upper() -> str:
        """Get the full table name for hash[T:]"""
        return(
            f'{UpperTables.T.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def u_upper() -> str:
        """Get the full table name for hash[U:]"""
        return(
            f'{UpperTables.U.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def v_upper() -> str:
        """Get the full table name for hash[V:]"""
        return(
            f'{UpperTables.V.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def w_upper() -> str:
        """Get the full table name for hash[W:]"""
        return(
            f'{UpperTables.W.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def x_upper() -> str:
        """Get the full table name for hash[X:]"""
        return(
            f'{UpperTables.X.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def y_upper() -> str:
        """Get the full table name for hash[Y:]"""
        return(
            f'{UpperTables.Y.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )

    @staticmethod
    def z_upper() -> str:
        """Get the full table name for hash[Z:]"""
        return(
            f'{UpperTables.Z.value.decode()}{Names.UP.value}{Names.HASH.value}'
        )
