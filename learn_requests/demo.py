# -*- encoding: utf-8 -*-
"""
@File    : demo.py
@Time    : 2020/2/19 21:19
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import requests
import json


url = 'http://localhost:9999/dataTransform/companyInfo'
headers = {
    # 'Host': 'localhost:9999',
    'Content-Type': 'application/json'
    # 'Referer': 'http://localhost:9999/swagger-ui.html'
    # 'Cookie': 'Pycharm-91913199=7482e5e2-bf73-412b-bb02-37b4dcdf8888'
}
# data = {
#     'companyName': 'Alibaba Inc.',
#     'exchange': 'Nyse',
#     'securityType': 'Ordinary Shares'
# }
data = {
    "companyName": "Alibaba Inc.",
    "exchange": "Nyse",
    "securityType": "Ordinary Shares"
}
res = requests.post(url=url, json=data, headers=headers)
print(res.text)
print(res.json())
