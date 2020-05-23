"""
孤儿进程和僵尸进程演示
"""
from multiprocessing import Process
from time import sleep
import os
from signal import *  # 函数模块 Linux

def fun():
    print("这是一个子进程",os.getppid(),'---',os.getpid())
    sleep(3)
    print("注定成为孤儿进程",os.getppid(),'---',os.getpid())

signal(SIGCHLD,SIG_IGN)  # 系统方法处理僵尸进程，所有子进程退出都由系统处理

p = Process(target=fun)
p.start()
# p.join()  # 防止僵尸进程产生

# 大量工作
while True:
    pass


