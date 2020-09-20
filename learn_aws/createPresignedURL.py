# -*- encoding: utf-8 -*-
"""
@File    : createPresignedURL.py
@Time    : 2020/1/5 16:26
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import logging
import boto3
import requests
from botocore.exceptions import ClientError


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """
    Generate a presigned URL to share an s3 object
    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None
    """

    # Generate a presigned URL for the s3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name,
                                                                          'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    # the response contains the presigned URL
    return response


if __name__ == '__main__':
    url = create_presigned_url('1s3dplinjy', 'test_fox.jpg')
    if url is not None:
        with open('download.jpg', 'wb') as fs:
            response = requests.get(url, timeout=6000, verify=False)
            fs.write(response.content)