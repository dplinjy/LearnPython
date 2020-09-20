# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/1/12 17:31
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
from multiprocessing import Process
import os


def run_proc(name):
    print('Run child process %s. ' % os.getpid())


if __name__ == '__main__':
    print('Parent process %s. ' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


