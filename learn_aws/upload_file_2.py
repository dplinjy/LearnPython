# -*- encoding: utf-8 -*-
"""
@File    : upload_file_2.py
@Time    : 2020/1/4 22:10
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import boto3
from boto3.s3.transfer import TransferConfig

# Set the desired multipart threshold value (5GB)
GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5*GB)

# Perform the transfer
s3 = boto3.client('s3')
s3.upload_file('FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME', Config=config)
