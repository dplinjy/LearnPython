# -*- encoding: utf-8 -*-
"""
@File    : painter.py
@Time    : 2020/1/22 20:47
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# get random char
def rndChar():
    return chr(random.randint(65, 90))


# get random color 1
def rndColor():
    return (randint(64, 255), randint(64, 255), randint(64, 255))


# get random color 2
def rndColor2():
    return (randint(32, 127), randint(32, 127), randint(32, 127))


# 240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# create Font Object
font = ImageFont.truetype('arial.ttf', 36)
# create Draw Object
draw = ImageDraw.Draw(image)
# fill every pixel in the image
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# print text
for t in range(height):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# blur
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
