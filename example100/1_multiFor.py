# -*- encoding: utf-8 -*-
"""
@File    : 1_multiFor.py
@Time    : 2019/11/17 18:25
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
-------------------------------------
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != k and i != j and j != k:
                print(i, j, k)