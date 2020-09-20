# -*- encoding: utf-8 -*-
"""
@File    : test_tmpdir2.py
@Time    : 2020/1/2 22:45
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import os


def test_create_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1
    assert 0

