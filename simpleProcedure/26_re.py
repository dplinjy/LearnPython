import re

a = "not 404 found 张三 99 深圳"

lis = a.split(" ")

print("raw data: ", lis)

pattern_1 = re.compile(r'[0-9]+|[a-z]+|[A-Z]')
pattern_2 = re.compile(r'[0-9a-zA-Z]+ ')

res_1 = pattern_1.findall(a)

res_2 = pattern_2.findall(a)

res = re.findall('\d+|[a-zA-Z]+', a)

print(res_1)
print(res_2)

# for i in res:
#     if i in lis:
#         lis.remove(i)
#
# new_str = " ".join(lis)
#
# print(new_str)

