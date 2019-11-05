# encoding:UTF8

s = 'ajldjlajfdljfddd'

unrepeat = set(list(s))

print(unrepeat)
#
mid = list(set(list(s)))

mid.sort(reverse=False)

print(mid)

res = "".join(mid)

print(res)
