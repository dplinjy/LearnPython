# encoding: UTF8
import re

print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))

m = re.match('www', 'www.runoob.com').span()

print(type(m))

print(m)


m2 = re.match('com', 'www.runoob.com')

print(m2)


line = 'Cats are smarter than dogs. 6876'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

print(type(matchObj))

print(matchObj)

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
    # print("matchObj.group(2): ", matchObj.group(3))
else:
    print("No match!")




