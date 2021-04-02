# -*- coding: utf-8 -*-
import inspect
import ctypes
 
 
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        """if it returns a number greater than one, you're in trouble,
        and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)





if __name__ == "__main__":
    import time
    import threading
    import logging

    logging.basicConfig(
        level = logging.DEBUG,
        format = "(%(threadName)-10s) %(message)s",
    )
    
    def f1():
        while 1:
            logging.debug("Starging")
            time.sleep(1)
            logging.debug("Exiting")

    t = threading.Thread(name='daemon',target=f1)
    t.start()
    print(t.ident, ctypes.c_long(t.ident))
    
    time.sleep(10)
    stop_thread(t)        #结束正在运行的子线程

    print("now sub thread was killed")
    time.sleep(10000)

