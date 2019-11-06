# encoding: UTF8

import re

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('Hello World Wide Web')
print("m: ", m)
print('m.group(): ', m.group())
print('m.span(): ', m.span(0))
print('m.group(1): ', m.group(1))
print('m.span(1): ', m.span(1))
print('m.group(2): ', m.group(2))
print('m.span(2): ', m.span(2))

