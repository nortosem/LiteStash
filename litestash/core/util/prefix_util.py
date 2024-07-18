"""The Database Prefix Build Functions

TODO: docs
"""
from typing import Generator
from litestash.core.config.tables.tables_03 import Tables03
from litestash.core.config.tables.tables_47 import Tables47
from litestash.core.config.tables.tables_89hu import Tables89hu
from litestash.core.config.tables.tables_ab import TablesAB
from litestash.core.config.tables.tables_cd import TablesCD
from litestash.core.config.tables.tables_ef import TablesEF
from litestash.core.config.tables.tables_gh import TablesGH
from litestash.core.config.tables.tables_ij import TablesIJ
from litestash.core.config.tables.tables_kl import TablesKL
from litestash.core.config.tables.tables_mn import TablesMN
from litestash.core.config.tables.tables_op import TablesOP
from litestash.core.config.tables.tables_qr import TablesQR
from litestash.core.config.tables.tables_st import TablesST
from litestash.core.config.tables.tables_uv import TablesUV
from litestash.core.config.tables.tables_wx import TablesWX
from litestash.core.config.tables.tables_yz import TablesYZ


def tables_03() -> Generator[str,None,None]:
    """Prefix generator for zero through three database"""
    for n in (Tables03.ZERO.value,
              Tables03.ONE.value,
              Tables03.TWO.value,
              Tables03.THREE.value
    ):
        yield n

def tables_47() -> Generator[str,None,None]:
    """Prefix generator for four through seven database"""
    for n in (Tables47.FOUR.value,
              Tables47.FIVE.value,
              Tables47.SIX.value,
              Tables47.SEVEN.value
    ):
        yield n

def tables_89hu() -> Generator[str,None,None]:
    """Prefix generator for eight,nine,-,_ database"""
    for n in(Tables89hu.EIGHT.value,
             Tables89hu.NINE.value,
             Tables89hu.HYPHEN.value,
             Tables89hu.UNDERSCORE.value
    ):
        yield n


def tables_ab() -> Generator[str,None,None]:
    """Prefix generator for a,b,A,B database"""
    for l in (TablesAB.A_LOW.value,
              TablesAB.B_LOW.value,
              TablesAB.A_UP.value,
              TablesAB.B_UP.value
    ):
        yield l

def tables_cd() -> Generator[str,None,None]:
    """Prefix generator for c,d,C,D database"""
    for l in (TablesCD.C_LOW.value,
              TablesCD.D_LOW.value,
              TablesCD.C_UP.value,
              TablesCD.D_UP.value
    ):
        yield l

def tables_ef() -> Generator[str,None,None]:
    """Prefix generator for e,f,E,F database"""
    for l in (TablesEF.E_LOW.value,
              TablesEF.F_LOW.value,
              TablesEF.E_UP.value,
              TablesEF.F_UP.value
    ):
        yield l

def tables_gh() -> Generator[str,None,None]:
    """Prefix generator for g,h,G,H database"""
    for l in (TablesGH.G_LOW.value,
              TablesGH.H_LOW.value,
              TablesGH.G_UP.value,
              TablesGH.H_UP.value
    ):
        yield l

def tables_ij() -> Generator[str,None,None]:
    """Prefix generator for i,j,I,J database"""
    for l in (TablesIJ.I_LOW.value,
              TablesIJ.J_LOW.value,
              TablesIJ.I_UP.value,
              TablesIJ.J_UP.value
    ):
        yield l

def tables_kl() -> Generator[str,None,None]:
    """Prefix generator for k,l,K,L database"""
    for l in (TablesKL.K_LOW.value,
              TablesKL.L_LOW.value,
              TablesKL.K_UP.value,
              TablesKL.L_UP.value
    ):
        yield l

def tables_mn() -> Generator[str,None,None]:
    """Prefix generator for m,n,M,N database"""
    for l in (TablesMN.M_LOW.value,
              TablesMN.N_LOW.value,
              TablesMN.M_UP.value,
              TablesMN.N_UP.value
    ):
        yield l

def tables_op() -> Generator[str,None,None]:
    """Prefix generator for o,p,O,P database"""
    for l in (TablesOP.O_LOW.value,
              TablesOP.P_LOW.value,
              TablesOP.O_UP.value,
              TablesOP.P_UP.value
    ):
        yield l

def tables_qr() -> Generator[str,None,None]:
    """Prefix generator for q,r,Q,R database"""
    for l in (TablesQR.Q_LOW.value,
              TablesQR.R_LOW.value,
              TablesQR.Q_UP.value,
              TablesQR.R_UP.value
    ):
        yield l

def tables_st() -> Generator[str,None,None]:
    """Prefix generator for s,t,S,T database"""
    for l in (TablesST.S_LOW.value,
              TablesST.T_LOW.value,
              TablesST.S_UP.value,
              TablesST.T_UP.value
    ):
        yield l

def tables_uv() -> Generator[str,None,None]:
    """Prefix generator for u,v,U,V database"""
    for l in (TablesUV.U_LOW.value,
              TablesUV.V_LOW.value,
              TablesUV.U_UP.value,
              TablesUV.V_UP.value
    ):
        yield l

def tables_wx() -> Generator[str,None,None]:
    """Prefix generator for w,x,W,X database"""
    for l in (TablesWX.W_LOW.value,
              TablesWX.X_LOW.value,
              TablesWX.W_UP.value,
              TablesWX.X_UP.value
    ):
        yield l


def tables_yz() -> Generator[str,None,None]:
    """Prefix generator for y,z,Y,Z database"""
    for l in (TablesYZ.Y_LOW.value,
              TablesYZ.Z_LOW.value,
              TablesYZ.Y_UP.value,
              TablesYZ.Z_UP.value
    ):
        yield l
