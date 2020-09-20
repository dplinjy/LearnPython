# -*- encoding: utf-8 -*-
"""
@File    : extract_data.py
@Time    : 2020/1/1 17:44
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import xml.etree.ElementTree as ET
import xml.dom.minidom
import base64


# tree = ET.parse('data_sourcing_demo.xml')
tree = xml.dom.minidom.parse('data_sourcing_demo.xml')
root = tree.documentElement
# root = ET.fromstring()
# print(root.attrib)

# for child in root:
    # print(child.tag, child.attrib)

# target = root['itemSet']['newsItem']['contentSet']['inlineData']
# target = root[1][0][-1][0]
target = root.getElementsByTagName('inlineData')

print("target", type(target))
print(target[0].nodeName)
ele_content = target[0].childNodes[0].data
# print(ele_content)
print("ele_content: ", type(ele_content))

pre = ele_content.encode('utf-8')
print("pre: ", type(pre))
# print(pre)
readable = base64.b64decode(pre)

print("readable: ", type(readable))
middle_content = base64.b64decode(ele_content.encode('utf-8'))
print("middle_content", type(middle_content))


# content = target.
with open(file='output6.pdf', mode='wb') as f:
    f.write(base64.b64decode(ele_content.encode('utf-8')))


# content_demo = '你好耗时的返回的水电费很快就东方红'
# content_demo_encode = base64.b64encode(content_demo.encode('utf-8'))
# print(content_demo_encode)
# with open('fff.pdf', 'w', encoding='utf-8') as f:
#     f.write(content_demo)

