# -*- encoding: utf-8 -*-
"""
@File    : test_fixture.py
@Time    : 2020/2/16 22:20
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest


@pytest.fixture()
def test1():
    a = 'leo'
    # b = '123456'
    # c = (a, b)
    print('\n传出a')
    return a


@pytest.fixture(scope='function')
def test2():
    b = '男'
    print('\n传出b')
    return b


def test3(test1):
    name = 'leo'
    print('找到name')
    assert test1 == name


def test4(test2):
    sex = '男'
    print('找到sex')
    assert test2 == sex

# def test_2(fixture_func):
#     u = fixture_func[0]
#     p = fixture_func[1]
#     assert u == 'leo'
#     assert p == '123456'
#     print('tuple format is correct')


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture.py'])



