#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 9/19/2020 9:36 PM


def foo(num):
    return num + 1


def bar(fun):
    return fun(3)


value = bar(foo)
print(value)