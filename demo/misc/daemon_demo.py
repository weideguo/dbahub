#pip install python-daemon

import os
import time
from daemon.runner import DaemonRunner
 
_base_path="/tmp/"
class MyApp(object):
 
    stdin_path = "/dev/null"
    stdout_path = os.path.join(_base_path, "myapp.stdout")
    stderr_path =  os.path.join(_base_path, "myapp.stderr")
    pidfile_path =  os.path.join(_base_path, "myapp.pid")
    pidfile_timeout = 5
 
    def run(self):
        for i in range(10):
            print i
            time.sleep(5)
 
if __name__ == '__main__':
    run = DaemonRunner(MyApp())
    run.do_action()
    
