# -*- encoding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2020/1/3 23:57
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest


@pytest.fixture
def supply_url():
    return "http://reqres.in/api"


