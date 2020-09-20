# encoding:UTF8

dic = {"name": "Nick", "age": 33}

del dic["name"]
print(dic)

dic2 = {"name": "Tony"}

dic.update(dic2)

print(dic)


dd = {'name': 'Mike', 'age': 20, 'job': 'student'}

del dd['job']
print(dd)

ddd = {'job': ['student', 'kids']}

dd.update(ddd)
print(dd)