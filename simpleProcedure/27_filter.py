# encoding: UTF8

a = [1, 2, 3, 5, 6, 7, 8, 9, 10]

def fn(a):
    return a%2 == 1

newlist = filter(fn, a)

print(type(newlist))

newlist = [i for i in newlist]
print(newlist)


# 方法二
newlist2 = [i for i in a if i%2 == 1]
print(newlist2)

newlist3 = [i**2 for i in a]
print(newlist3)

newlist4 = map(lambda x: x**2, a)
print(list(newlist4))