import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M|re.I)

if matchObj:
    print("match --> matchObj.group(): ", matchObj.group())
else:
    print("No match!")

searchObj = re.search(r'dogs', line, re.M|re.I)

if searchObj:
    print("search --> searchObj.group(): ", searchObj.group())
else:
    print("No match!")


pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print(m)

m = pattern.match('one12twothree34four', 2, 10)
print(m)

m = pattern.match('one12twothree34four', 3, 10)
print(m.group())
# print(m.group(1))
print(m.start(0))
print(m.end(0))
print(m.span())

