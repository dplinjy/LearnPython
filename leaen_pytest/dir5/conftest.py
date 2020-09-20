# -*- encoding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2020/1/3 23:17
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
