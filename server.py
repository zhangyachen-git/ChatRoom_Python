#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : server.py
@Time : 2019/03/07 12:39:13
@Author : ZhangYachen 
@Version : 1.0
@Contact : aachen_z@163.com
'''

# here put the import lib
from socket import *
import os,sys

# 接收客户端请求
def do_parent():
    print('do_parent')
# 管理员喊话
def do_child():
    print('do_child')


# 创建网络，创建进程，调用功能函数
def main():
    # server address
    ADDR = ('0.0.0.0',8888)
    # 创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    # 创建一个单独的进程处理管理员喊话功能
    pid = os.fork()
    if pid < 0 :
        sys.exit('创建进程失败！')
    elif pid == 0 :
        do_child()
    else:
        do_parent()

if __name__ == "__main__":
    main()