# encoding: UTF8

import re

res1 = re.split('\W+', 'runoob, runoob, runoob.')
print(res1)

res2 = re.split('(\W+)', ' runoob, runoob, runoob.')
print(res2)