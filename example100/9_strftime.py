# -*- encoding: utf-8 -*-
"""
@File    : 9_strftime.py
@Time    : 2019/11/17 19:49
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))