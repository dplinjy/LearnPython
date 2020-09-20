# -*- encoding: utf-8 -*-
"""
@File    : create_bucket.py
@Time    : 2020/1/4 18:14
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

