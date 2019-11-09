import random
import string
import uuid

dd = {x:'item'+str(x**2) for x in (2,3,4)}
print(dd)

num = 9
def fn1():
    num = 7

def fn2():
    print(num)

fn2()
fn1()
fn2()