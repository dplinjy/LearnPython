#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 9/19/2020 9:39 PM
def outer():
    x = 1
    def inner():
        print(x)
    inner()


outer()