# -*- encoding: utf-8 -*-
"""
@File    : demo.py
@Time    : 2020/1/9 22:52
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import hashlib
import os


def getMd5(str):
    md5_value = hashlib.md5()
    md5_value.update(str.encode('útf-8'))
    md5_value_hexDigest = md5_value.hexdigest()
    print(md5_value_hexDigest)



def getFileMd5(filename):
    fileObj = open(filename)
    fileContent = fileObj.read()
    getfilemd5 = getMd5(fileContent)
    print(getfilemd5)
    return getfilemd5


