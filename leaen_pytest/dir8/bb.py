# -*- encoding: utf-8 -*-
"""
@File    : bb.py
@Time    : 2020/2/26 11:27
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""

def bb(list, str):
    try:
        for i in range(len(list)):
            if i == 0:
                print('\n')
            if i == 2:
                assert False
            if i < len(str):
                print(list[i], str[i])
            else:
                print(list[i])
    except Exception as err:
        print("若为2结果置为false")
        print(err)


def cc(list):
    try:
        for i in range(len(list)):
            if i == 0:
                print('\n')
            if i == 2:
                assert False

            print(list[i])
            assert True
    except Exception as err:
        print("若为2结果置为false")
        print(err)
