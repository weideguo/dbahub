#coding:utf8
#python >= 3.3
#yield from


# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count


# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()


# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激生成器
    print(calc_average.send(10))  
    print(calc_average.send(20))  
    print(calc_average.send(30))  
    

if __name__ == '__main__':
    main()