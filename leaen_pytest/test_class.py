# -*- encoding: utf-8 -*-
"""
@File    : test_class.py
@Time    : 2019/12/25 23:01
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""


class TestCase(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

