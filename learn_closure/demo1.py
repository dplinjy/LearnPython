#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 9/19/2020 8:43 PM

# def print_msg():
#     msg = "zen of python"
#     def printer():
#         print(msg)
#     return printer
# another = print_msg()
# another()
#
def adder(x):
    def wrapper(y):
        return x + y
    return wrapper
adder5 = adder(5)
replica = adder5
print(adder5(5))
print(replica(5))
print(adder5(10))
print(adder5(6))
print(adder.__closure__)
print(adder5.__closure__)
print(adder5.__closure__[0].cell_contents)