# -*- encoding: utf-8 -*-
"""
@File    : demo_aws.py
@Time    : 2019/12/26 22:44
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import boto3

# use Amazon s3
s3 = boto3.resource('s3')

# print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# upload a new file
# data = open('fox.jpg', 'rb')
# s3.Bucket('1s3dplinjy').put_object(Key='test_fox.jpg', Body=data)

s3_ = boto3.client('s3')
result = s3_.get_bucket_website('1s3dplinjy')
print(result)