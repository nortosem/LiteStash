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


def test_tables_03(valid_03):
    table03 = [n for n in tables_03()]
    assert table03 == valid_03


def test_tables_47(valid_47):
    table47 = [n for n in tables_47()]
    assert table47 == valid_47


def test_tables_89hu(valid_89hu):
    table_89hu = [n for n in tables_89hu()]
    assert table_89hu == valid_89hu

def test_tables_ab(valid_ab):
    table_ab = [n for n in tables_ab()]
    assert table_ab == valid_ab


def test_tables_cd(valid_cd):
    table_cd = [n for n in tables_cd()]
    assert table_cd == valid_cd


def test_tables_ef(valid_ef):
    table_ef = [n for n in tables_ef()]
    assert table_ef == valid_ef


def test_tables_gh(valid_gh):
    tablegh = [n for n in tables_gh()]
    assert tablegh == valid_gh


def test_tables_ij(valid_ij):
    tableij = [n for n in tables_ij()]
    assert tableij == valid_ij


def test_tables_kl(valid_kl):
    tablekl = [n for n in tables_kl()]
    assert tablekl == valid_kl


def test_tables_mn(valid_mn):
    tablemn = [n for n in tables_mn()]
    assert tablemn == valid_mn

def test_tables_op(valid_op):
    tableop = [n for n in tables_op()]
    assert tableop == valid_op


def test_tables_qr(valid_qr):
    tableqr = [n for n in tables_qr()]
    assert tableqr == valid_qr

def test_tables_st(valid_st):
    tablest = [n for n in tables_st()]
    assert tablest == valid_st


def test_tables_uv(valid_uv):
    tableuv = [n for n in tables_uv()]
    assert tableuv == valid_uv


def test_tables_wx(valid_wx):
    tablewx = [n for n in tables_wx()]
    assert tablewx == valid_wx

def test_tables_yz(valid_yz):
    tableyz = [n for n in tables_yz()]
    assert tableyz == valid_yz
