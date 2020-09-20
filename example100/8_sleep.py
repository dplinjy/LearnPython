# -*- encoding: utf-8 -*-
"""
@File    : 8_sleep.py
@Time    : 2019/11/17 19:43
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""

import time

myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
for key, value in myD.items():
    print(key, value)
    time.sleep(1)