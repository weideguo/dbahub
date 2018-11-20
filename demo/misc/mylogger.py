#!/bin/env python
# coding: utf-8

import logging
from logging.handlers import TimedRotatingFileHandler
#from logging.handlers import WatchedFileHandler
import os
import sys

format = "[%(levelname)s] %(asctime)s %(message)s"
log_dir="log"
log_name="log.txt"
log_dir=os.path.dirname(os.path.realpath(__file__))+"/"+log_dir
if not os.path.exists(log_dir):
	os.makedirs(log_dir)

log_filename=log_dir+"/"+log_name
#多进程使用TimedRotatingFileHandler不安全，请使用其他方式实现日志分割
#如使用linux的crontab调度实现
handler=TimedRotatingFileHandler(filename=log_filename,when="D", interval=1, backupCount=30,utc=8)
#handler=WatchedFileHandler(filename=log_filename)

handler.setFormatter(logging.Formatter(format))

logger=logging.getLogger("alert_server_logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
