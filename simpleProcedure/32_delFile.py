# encoding: UTF8
import os
import sys


# with open('test.txt', 'w') as fb:
#     fb.write('2347jdhsfksd')


print("目录为：%s" % os.listdir(os.getcwd()))

print(type(os.listdir(os.getcwd())))

dirlist = os.listdir(os.getcwd())
for f in dirlist:
    if f == 'test.txt':
        print(f)
os.remove('test.txt')
dirlist = os.listdir(os.getcwd())
for f in dirlist:
    if f == 'test.txt':
        print(f)