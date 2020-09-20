# -*- encoding: utf-8 -*-
"""
@File    : test_sample1.py
@Time    : 2020/1/3 22:40
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest


@pytest.mark.set1
def test_file1_method1():
    x=5
    y=6
    assert x+1 == y, "test failed"
    assert x == y, "test failed"


@pytest.mark.set2
def test_file1_method2():
    x=5
    y=6
    assert x+1 == y, "test failed"

