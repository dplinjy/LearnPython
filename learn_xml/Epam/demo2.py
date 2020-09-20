# -*- encoding: utf-8 -*-
"""
@File    : demo1.py
@Time    : 2020/1/1 19:28
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import os
import xml.dom.minidom
from xml.dom.minidom import parse


def printLibrary(library):
    pass


# open a xml file and parse it into a dom
myDoc = parse(r'demo2.xml')
myLibrary = myDoc.getElementsByTagName("library")[0]

# get all the book elements in the library
books = myLibrary.getElementsByTagName("book")
