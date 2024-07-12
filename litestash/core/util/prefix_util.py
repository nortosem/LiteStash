"""The Database Prefix Build Functions

TODO: docs
"""
from typing import Generator
from litestash.core.config.tables.digits import Digitables
from litestash.core.config.tables.lowercase import LowerTables
from litestash.core.config.tables.uppercase import UpperTables

def zf_db() -> Generator[bytes,None,None]:
    """Prefix generator for zero through four database"""
    for n in (Digitables.ZERO.value,
              Digitables.ONE.value,
              Digitables.TWO.value,
              Digitables.THREE.value,
              Digitables.FOUR.value
    ):
        yield n

def fn_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for n in (Digitables.FIVE.value,
              Digitables.SIX.value,
              Digitables.SEVEN.value,
              Digitables.EIGHT.value,
              Digitables.NINE.value
    ):
        yield n

def ael_db() -> Generator[bytes,None,None]:
    """Prefix generator for a through e database"""
    for l in (LowerTables.A.value,
              LowerTables.B.value,
              LowerTables.C.value,
              LowerTables.D.value,
              LowerTables.E.value
    ):
        yield l

def fil_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.F.value,
              LowerTables.G.value,
              LowerTables.H.value,
              LowerTables.I.value
    ):
        yield l

def jml_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.J.value,
              LowerTables.K.value,
              LowerTables.L.value,
              LowerTables.M.value
    ):
        yield l

def nrl_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.N.value,
              LowerTables.O.value,
              LowerTables.P.value,
              LowerTables.Q.value,
              LowerTables.R.value
    ):
        yield l

def svl_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.S.value,
              LowerTables.T.value,
              LowerTables.U.value,
              LowerTables.V.value
    ):
        yield l

def wzl_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (LowerTables.W.value,
              LowerTables.X.value,
              LowerTables.Y.value,
              LowerTables.Z.value
    ):
        yield l

def aeu_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.A.value,
              UpperTables.B.value,
              UpperTables.C.value,
              UpperTables.D.value,
              UpperTables.E.value
    ):
        yield l

def fiu_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.F.value,
              UpperTables.G.value,
              UpperTables.H.value,
              UpperTables.I.value
    ):
        yield l

def jmu_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.J.value,
              UpperTables.K.value,
              UpperTables.L.value,
              UpperTables.M.value
    ):
        yield l

def nru_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.N.value,
              UpperTables.O.value,
              UpperTables.P.value,
              UpperTables.Q.value,
              UpperTables.R.value
    ):
        yield l

def svu_db() -> Generator[bytes,None,None]:
    """Prefix generator for five through nine database"""
    for l in (UpperTables.S.value,
              UpperTables.T.value,
              UpperTables.U.value,
              UpperTables.V.value
    ):
        yield l

def wzu_db() -> Generator[bytes,None,None]:
    """Prefix generator for W through Z database"""
    for l in (UpperTables.W.value,
              UpperTables.X.value,
              UpperTables.Y.value,
              UpperTables.Z.value
    ):
        yield l
