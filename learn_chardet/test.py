# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/1/22 21:03
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import chardet


b = b'Hello, World'
print(type(b))
print(chardet.detect(b))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))