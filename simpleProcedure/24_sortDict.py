# encoding:UTF8

# 根据字典的key排序

dic = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

lis = sorted(dic.items(), key=lambda i: i[0], reverse=False)

print(lis)
print(dic)
print(dict(lis))

# 根据字典的value排序

dd = {"name":"zs","age":'18',"city":"深圳","tel":"1362626627"}

lis2 = sorted(dd.items(), key=lambda i: i[1], reverse=False)

print(lis2)

