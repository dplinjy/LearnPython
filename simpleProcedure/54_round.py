a = "%.03f" % 1.3335
print(a, type(a))
b = round(float(a), 1)
print(b)
b = round(float(a), 2)
print(b)

A = zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))
A0 = dict(A)
print(A0)

S = zip('abcd', '1234')
print(dict(S))