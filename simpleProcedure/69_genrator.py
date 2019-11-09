l = [i for i in range(5)]
print(l, type(l))

g = (i for i in range(5))
print(g, type(g))
print(next(g))