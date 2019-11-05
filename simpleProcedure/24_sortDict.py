dic = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

lis = sorted(dic.items(), key=lambda i:i[0], reverse=False)

print(lis)

print(dict(lis))
