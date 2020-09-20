#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date: 9/19/2020 9:43 PM


# def foo():
#     print("记录日志开始")
#     print("foo")
#     print("记录日志结束")


def outer(func):
    def inner():
        print("记录日志开始")
        func()  # 业务函数
        print("激励日志结束")
    return inner


def foo():
    print("foo")


foo = outer(foo)
foo()

