#coding:utf8
import atexit


#程序退出时执行
def exit_handler():
    print('Stopping all modules before exit!')

atexit.register(exit_handler)



if __name__ == "__main__":
    #使用装饰器
    @atexit.register
    def xxx():
        print("yes you will exit")   

    import time
    while True:
        print("xxxx")
        time.sleep(1)
