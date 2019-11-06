import re

a = "not 404 found 张三 99 深圳"

lis = a.split(" ")

print(lis)

res = re.findall(r'\d+\.?\d*|[a-zA-Z]+', a)

print(res)

for i in res:
    if i in lis:
        lis.remove(i)

new_str = " ".join(lis)
print(new_str)
