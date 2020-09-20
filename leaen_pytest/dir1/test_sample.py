# -*- encoding: utf-8 -*-
"""
@File    : test_sample.py
@Time    : 2020/1/2 22:58
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
# -*- encoding: utf-8 -*-
"""
@File    : test_sample2.py
@Time    : 2020/1/2 22:56
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest


def func(x):
    return x + 1


@pytest.mark.case1
def test_file1_answer1():
    assert func(3) == 5

@pytest.mark.case2
def test_file1_answer2():
    assert func(5) == 5

