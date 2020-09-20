# -*- encoding: utf-8 -*-
"""
@File    : callback_demo.py
@Time    : 2020/1/1 15:27
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
from learn_xml.call_back.even import *


def getOddNumber(k, getEvenNumber):
    return 1 + getEvenNumber(k)


def main():
    k = 1
    i = getOddNumber(k, double)
    print(i)
    i = getOddNumber(k, quadruple)
    print(i)
    i = getOddNumber(k, lambda x: x*8)
    print(i)


main()
