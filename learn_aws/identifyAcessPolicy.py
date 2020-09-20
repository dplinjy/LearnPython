# -*- encoding: utf-8 -*-
"""
@File    : identifyAcessPolicy.py
@Time    : 2020/1/5 17:27
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import boto3
import json


def get_bucket_policy(bucket_name):
    # Retrieve the policy of the specigied bucket
    s3 = boto3.client('s3')
    result = s3.get_bucket_policy(Bucket=bucket_name)
    return result['Policy']


# print(get_bucket_policy('1s3dplinjy'))


def create_bucket_policy(bucket_name):
    # Create a bucket policy
    # bucket_name = '1s3dplinjy'
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
    }

    # convert the policy from JSON dict to string
    bucket_policy = json.dumps(bucket_policy)
    s3 = boto3.client('s3')
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)


if __name__ == '__main__':
    create_bucket_policy('1s3dplinjy')
    print(get_bucket_policy('1s3dplinjy'))