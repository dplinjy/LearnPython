# encoding: UTF8

import re

print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())

res = re.search('www', 'www.runoob.com')

line = 'Cats are smarter than dogs'

searchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print("searchObj.group(): ", searchObj.group())
    print("searchObj.group(1): ", searchObj.group(1))
    print("searchObj.group(2): ", searchObj.group(2))
else:
    print("Nothing found!")






