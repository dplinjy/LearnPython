# -*- encoding: utf-8 -*-
"""
@File    : test_time.py
@Time    : 2020/2/16 21:53
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import pytest
from datetime import datetime, timedelta


testData = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1))
]


@pytest.mark.parametrize("a, b, expected", testData)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a, b, expected", testData, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected


def idfn(val):
    if isinstance(val, (datetime, )):
        return val.strftime('%Y%m%d')


@pytest.mark.parametrize("a, b, expected", testData, ids=idfn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected

