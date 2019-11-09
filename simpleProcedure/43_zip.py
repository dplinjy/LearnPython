a = [1, 2]
b = [3, 4]
res = [i for i in zip(a, b)]
print(res)

print(dict(res))

m = (1, 2, 3)
n = (3, 4, 5)
res2 = [i for i in zip(m, n)]
print(res2)

print(dict(res2))

s1 = {1, 2, 3}
s2 = {4, 5, 6}
res3 = [i for i in zip(s1,s2)]
print(res3)