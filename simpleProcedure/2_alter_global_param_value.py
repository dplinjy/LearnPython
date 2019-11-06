# encoding:UTF8

a = 5

def fn():
    global a
    a = 7

fn()
print(a)

