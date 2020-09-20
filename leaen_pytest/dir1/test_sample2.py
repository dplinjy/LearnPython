# -*- encoding: utf-8 -*-
"""
@File    : test_sample2.py
@Time    : 2020/1/2 22:59
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest


def func(x):
    return x + 1

@pytest.mark.case1
def test_file2_answer1():
    assert func(4) == 5


@pytest.mark.case1
def test_file2_answer2():
    assert func(6) == 5

