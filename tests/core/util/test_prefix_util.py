import pytest
from unittest.mock import patch
from litestash.core.util.prefix_util import *

@pytest.fixture(params=[
    ["0", "1", "2", "3"]
])
def valid_03(request):
    yield request.param


@pytest.fixture(params=[
    ["4", "5", "6", "7"]
])
def valid_47(request):
    yield request.param


@pytest.fixture(params=[
["8", "9", "-", "_"]
])
def valid_89hu(request):
    yield request.param


@pytest.fixture(params=[
    ["a", "b", "A", "B"]
])
def valid_ab(request):
    yield request.param


@pytest.fixture(params=[
    ["c", "d", "C", "D"]
])
def valid_cd(request):
    yield request.param


@pytest.fixture(params=[
    ["e", "f", "E", "F"]
])
def valid_ef(request):
    yield request.param


@pytest.fixture(params=[
    ["g", "h", "G", "H"]
])
def valid_gh(request):
    yield request.param


@pytest.fixture(params=[
    ["i", "j", "I", "J"]
])
def valid_ij(request):
    yield request.param


@pytest.fixture(params=[
    ["k", "l", "K", "L"]
])
def valid_kl(request):
    yield request.param


@pytest.fixture(params=[
    ["m", "n", "M", "N"]
])
def valid_mn(request):
    yield request.param


@pytest.fixture(params=[
    ["o", "p", "O", "P"]
])
def valid_op(request):
    yield request.param


@pytest.fixture(params=[
    ["q", "r", "Q", "R"]
])
def valid_qr(request):
    yield request.param


@pytest.fixture(params=[
    ["s", "t", "S", "T"]
])
def valid_st(request):
    yield request.param


@pytest.fixture(params=[
    ["u", "v", "U", "V"]
])
def valid_uv(request):
    yield request.param


@pytest.fixture(params=[
    ["w", "x", "W", "X"]
])
def valid_wx(request):
    yield request.param


@pytest.fixture(params=[
    ["y", "z", "Y", "Z"]
])
def valid_yz(request):
    yield request.param


@pytest.fixture(params=[
    "&", "$", "*", ":", ";", "@", "'", '"', "|", "\\", ","
])
def invalid_char(request):
    """Yields invalid characters for testing ValueError."""
    yield request.param


def test_tables_03(valid_03, invalid_char):
    table03 = [n for n in tables_03()]
    assert table03 == valid_03
    assert invalid_char not in table03


def test_tables_47(valid_47, invalid_char):
    table47 = [n for n in tables_47()]
    assert table47 == valid_47
    assert invalid_char not in table47


def test_tables_89hu(valid_89hu, invalid_char):
    table_89hu = [n for n in tables_89hu()]
    assert table_89hu == valid_89hu
    assert invalid_char not in table_89hu


def test_tables_ab(valid_ab, invalid_char):
    table_ab = [n for n in tables_ab()]
    assert table_ab == valid_ab
    assert invalid_char not in table_ab


def test_tables_cd(valid_cd, invalid_char):
    table_cd = [n for n in tables_cd()]
    assert table_cd == valid_cd
    assert invalid_char not in table_cd


def test_tables_ef(valid_ef, invalid_char):
    table_ef = [n for n in tables_ef()]
    assert table_ef == valid_ef
    assert invalid_char not in table_ef


def test_tables_gh(valid_gh, invalid_char):
    table_gh = [n for n in tables_gh()]
    assert table_gh == valid_gh
    assert invalid_char not in table_gh


def test_tables_ij(valid_ij, invalid_char):
    table_ij = [n for n in tables_ij()]
    assert table_ij == valid_ij
    assert invalid_char not in table_ij


def test_tables_kl(valid_kl, invalid_char):
    table_kl = [n for n in tables_kl()]
    assert table_kl == valid_kl
    assert invalid_char not in table_kl


def test_tables_mn(valid_mn, invalid_char):
    table_mn = [n for n in tables_mn()]
    assert table_mn == valid_mn
    assert invalid_char not in table_mn


def test_tables_op(valid_op, invalid_char):
    table_op = [n for n in tables_op()]
    assert table_op == valid_op
    assert invalid_char not in table_op


def test_tables_qr(valid_qr, invalid_char):
    table_qr = [n for n in tables_qr()]
    assert table_qr == valid_qr
    assert invalid_char not in table_qr


def test_tables_st(valid_st, invalid_char):
    table_st = [n for n in tables_st()]
    assert table_st == valid_st
    assert invalid_char not in table_st


def test_tables_uv(valid_uv, invalid_char):
    table_uv = [n for n in tables_uv()]
    assert table_uv == valid_uv
    assert invalid_char not in table_uv


def test_tables_wx(valid_wx, invalid_char):
    table_wx = [n for n in tables_wx()]
    assert table_wx == valid_wx
    assert invalid_char not in table_wx


def test_tables_yz(valid_yz, invalid_char):
    table_yz = [n for n in tables_yz()]
    assert table_yz == valid_yz
    assert invalid_char not in table_yz
