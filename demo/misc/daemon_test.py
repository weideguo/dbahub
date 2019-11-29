#coding=utf8
import os
import sys
import atexit
import datetime
import time

def daemonize(forever_run,pid_file=None,chdir='/tmp',err_file='/dev/null',**kwargs):
	pid=os.fork()
	if pid:
		sys.exit()
    
	os.chdir(chdir)
	os.umask(0)
	os.setsid()
	
	_pid=os.fork()
	if _pid:
		sys.exit()
    
	sys.stdout.flush()
	sys.stderr.flush()
    
	with open(err_file,'w+') as write_null:
		os.dup2(write_null.fileno(),sys.stdin.fileno())
		os.dup2(write_null.fileno(),sys.stdout.fileno())
		os.dup2(write_null.fileno(),sys.stdout.fileno())
    
	if pid_file:
		with open(pid_file,'w+') as f:
			f.write(str(os.getpid())+'\n')
		atexit.register(os.remove,pid_file)
    
    forever_run(**kwargs)
	
	
	
if __name__=='__main__':

    def f(out_file):
        with open(out_file,'w') as out:
            while True:
                out.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'daemon work!\n')
                out.flush()
                time.sleep(1)
                
    
	daemonize(f,out_file='mydaemon.out',pid_file='mydaemon.pid',chdir='/tmp')
	
