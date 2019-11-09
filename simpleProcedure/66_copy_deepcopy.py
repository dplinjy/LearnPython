# encoding:UTF8
import copy

a = ['a', ['b', 'c']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append('e')

print('a: ', a, id(a))
print('b: ', b, id(b))
print('c: ', c, id(c))
print('d: ', d, id(d))

