# -*- encoding: utf-8 -*-
"""
@File    : test_seq.py
@Time    : 2019/12/25 23:08
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""


class TestClassOne(object):
    def test_one(self):
        x = 'this'
        assert 't' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')


class TestClassTwo(object):
    def test_one(self):
        x = 'iphone'
        assert 'p'in x

    def test_two(self):
        x = 'apple'
        assert hasattr(x, 'check')


