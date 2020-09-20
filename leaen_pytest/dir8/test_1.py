# -*- encoding: utf-8 -*-
"""
@File    : test_1.py
@Time    : 2020/2/26 11:25
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import bb
import pytest


list = ['1', '2', '5', '9', '10']
str = ['a', 'b', 'c', 'd']

@pytest.mark.parametrize('num, str', [(list[0], str[0]), (list[1], str[1]), (list[2], str[2])])
def test_bb(num, str):
    bb.bb(num, str)


parametrize=[(list, str)]
@pytest.mark.parametrize('num, str', parametrize)
def test_bb_new(num, str):
    bb.bb(num, str)


@pytest.mark.parametrize('num', list)
def test_cc(num):
    bb.cc(num)


if __name__ == '__main__':
    pytest.main(["-v"])