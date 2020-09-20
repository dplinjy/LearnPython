# -*- encoding: utf-8 -*-
"""
@File    : upload_file.py
@Time    : 2020/1/4 18:20
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import logging
import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    """
    upload a file to an s3 bucket
    :param file_name: file to upload
    :param bucket: Bucket to upload to
    :param object_name: s3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = file_name

    # upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


