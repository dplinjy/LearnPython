# encoding:UTF8

dic = {"name": "Nick", "age": 33}

del dic["name"]
print(dic)

dic2 = {"name": "Tony"}

dic.update(dic2)

print(dic)

