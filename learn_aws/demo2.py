# -*- encoding: utf-8 -*-
"""
@File    : demo1.py
@Time    : 2020/1/4 22:27
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import boto3


s3 = boto3.client('s3')

# Define the website configuration
website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}

# Set the website configuration
# s3 = boto3.client('s3')
s3.put_bucket_website(Bucket='s3dplinjy', WebsiteConfiguration=website_configuration)


# Retrieve the website configuration
result = s3.get_bucket_website(Bucket='s3dplinjy')
print(result)


# Delete the website configuration
# s3 = boto3.client('s3')
# s3.delete_bucket_website(Bucket='s3dplinjy')

# Retrieve a bucket's ACL
res = s3.get_bucket_acl(Bucket='s3dplinjy')
print('_______________________________________________________')
print(res)
res2 = s3.get_bucket_policy(Bucket='s3dplinjy')
print(res2['Policy'])


