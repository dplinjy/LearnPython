# -*- encoding: utf-8 -*-
"""
@File    : download_file.py
@Time    : 2020/1/4 18:37
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import boto3

s3 = boto3.client('s3')
# s3.download_file('1s3dplinjy', 'test_fox.jpg', 'xxx.jpg')

with open('xxx2.jpg', 'wb') as f:
    s3.download_fileobj('1s3dplinjy', 'test_fox.jpg', f)

