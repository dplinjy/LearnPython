# encoding:UTF8

class A(object):
    def __init__(self):
        print("this is init func", self)

    def __new__(cls):
        print("this is cls's ID", id(cls))
        print("this is new func", object.__new__(cls))
        return object.__new__(cls)

A()
print("this is A's ID", id(A))

