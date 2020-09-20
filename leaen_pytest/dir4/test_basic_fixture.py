# -*- encoding: utf-8 -*-
"""
@File    : test_basic_fixture.py
@Time    : 2020/1/3 23:04
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest


@pytest.fixture
def supply_AA_BB_CC():
    aa = 25
    bb = 35
    cc = 45
    return [aa, bb, cc]


def test_comparewithAA(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[0] == zz, "aa and zz comparison failed"


def test_comparewithBB(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[1] == zz, "cc and zz comparison failed"


def test_comparewithCC(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[2] == zz, "cc and zz comparison failed"
