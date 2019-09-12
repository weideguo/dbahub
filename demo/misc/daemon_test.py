#coding=utf8
import os
import sys
import atexit
import datetime
import time

def daemonize(pid_file=None):
	pid=os.fork()
	if pid:
		sys.exit()
	os.chdir('/home/weideguo')
	os.umask(0)
	os.setsid()
	
	_pid=os.fork()
	if _pid:
		sys.exit()
	sys.stdout.flush()
	sys.stderr.flush()
	with open('/dev/null','w+') as write_null:
		os.dup2(write_null.fileno(),sys.stdin.fileno())
		os.dup2(write_null.fileno(),sys.stdout.fileno())
		os.dup2(write_null.fileno(),sys.stdout.fileno())
	if pid_file:
		with open(pid_file,'w+') as f:
			f.write(str(os.getpid())+'\n')
		atexit.register(os.remove,pid_file)
	with open('/home/weideguo/mydaemon.log','w') as out:
		while True:
			out.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'daemon work!\n')
			out.flush()
			time.sleep(1)
	
	
if __name__=='__main__':
	daemonize('mydaemon.pid')
	
