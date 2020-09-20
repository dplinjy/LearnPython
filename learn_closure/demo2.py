#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 9/19/2020 9:32 PM


def foo():
    return 1


def bar():
   return foo


print(bar())
print(bar()())
print(foo())