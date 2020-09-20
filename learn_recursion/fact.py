# -*- encoding: utf-8 -*-
"""
@File    : fact.py
@Time    : 2019/11/17 17:23
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(1))
print(fact(2))
print(fact(3))
print(list(range(1, 100, 10)))