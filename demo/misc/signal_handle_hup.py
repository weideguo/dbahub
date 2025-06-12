#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 捕捉信号
# kill -HUP $curent_pid
# 触发应用的动作

import signal
import time


def handle_hup(signum, frame):
    print(f"收到 SIGHUP 信号 {signum}")
    app_action()


def app_action():
    print("应用进行自定义操作")   
    # 如重新加载配置文件


# 监听信号，进行自定义处理，如果不进行监听，则会杀死应用
signal.signal(signal.SIGHUP, handle_hup)


print("可以运行 `kill -HUP $curent_pid` 触发定义操作")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("程序退出")

