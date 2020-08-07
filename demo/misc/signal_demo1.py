import signal
 
def timeout(error_message="catch cancel ctrl+c"):
    def decorator(func):
        def signal_handler(signum, frame):
            raise Exception(error_message)
        
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGINT, signal_handler)     #可以直接捕获外部的ctrl+c信号
            result = func(*args, **kwargs)
            return result
        
        return wrapper
        
    return decorator


import time

@timeout()
def f(n):
    time.sleep(n)
    return 1



f(2)
f(200)

