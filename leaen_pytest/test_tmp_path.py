# -*- encoding: utf-8 -*-
"""
@File    : test_tmp_path.py
@Time    : 2020/1/2 22:40
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import os

content = "content"


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(content)
    assert p.read_text() == content
    assert len(list(tmp_path.iterdir())) == 1
    assert 0