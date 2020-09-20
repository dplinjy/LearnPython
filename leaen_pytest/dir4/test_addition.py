# -*- encoding: utf-8 -*-
"""
@File    : test_addition.py
@Time    : 2020/1/3 23:46
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest


@pytest.mark.skip
def test_add_1():
    assert 100 + 200 == 400, "failed"


@pytest.mark.skip
def test_add_2():
    assert 100 + 200 == 300, "failed"


@pytest.mark.xfail
def test_add_3():
    assert 15 + 13 == 28, "failed"


@pytest.mark.xfail
def test_add_4():
    assert 15 + 13 == 100, "failed"


def test_add_5():
    assert 3 + 2 == 5, "failed"


def test_add_6():
    assert 3 + 2 == 6, "failed"

