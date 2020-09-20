# -*- encoding: utf-8 -*-
"""
@File    : list_bucket.py
@Time    : 2020/1/4 18:17
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import boto3


s3 = boto3.client('s3')
response = s3.list_buckets()
print('Existing buckets: ')
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')