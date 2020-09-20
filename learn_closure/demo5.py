#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 9/19/2020 9:40 PM
def outer(x):
    def inner():
        print(x)
    return inner


closure = outer(1)
closure()