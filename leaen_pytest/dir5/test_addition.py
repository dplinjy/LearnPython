# -*- encoding: utf-8 -*-
"""
@File    : test_addition.py
@Time    : 2020/1/3 23:39
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest


@pytest.mark.parametrize("input1, input2, output", [(5, 5, 10), (3, 5, 12)])
def test_add(input1, input2, output):
    assert input1 + input2 == output, "-_-failed-_-"

