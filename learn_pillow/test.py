# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/1/22 20:30
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
from PIL import Image, ImageFilter


im = Image.open('fox.jpg')
w, h = im.size
print('Original iamge size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
