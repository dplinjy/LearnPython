# -*- encoding: utf-8 -*-
"""
@File    : udp_server.py
@Time    : 2020/1/25 20:49
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)

