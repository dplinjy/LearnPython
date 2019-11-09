t = (6, 3, 2, 1, 90)
print(sorted(t, reverse=True))

s = {3, 0, 35}
print(sorted(s, reverse=True))

lis = [0, -1, 3, -10, 5, 9]
lis.sort(reverse=False)
print(lis)

lis = [0, -1, 3, -10, 5, 9]
res = sorted(lis, reverse=False)
print("sorted有返回值是新的list", lis)
print("返回值", res)


