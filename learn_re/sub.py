# encoding: UTF8

import re

phone = "2004-959-559"

num = re.sub(r'#.*$', "", phone)

print("电话号码：", num)

num2 = re.sub(r'\D', "", phone)

print("电话号码：", num)