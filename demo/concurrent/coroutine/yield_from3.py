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
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total/count
    
    # 每一次return，都意味着当前协程结束。
    return total,count,average


# 委托生成器
def proxy_gen():
    while True:                                           #如果不设置循环，结束协程后不能再开协程
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        total, count, average = yield from average_gen()
        print("%d %d %d" % (count, total, average))


# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)             # 预激协程
    print(calc_average.send(10))  
    print(calc_average.send(20))  
    print(calc_average.send(30))  
    calc_average.send(None)        # 结束协程，由子生成器确定结束的方式
    
    # 如果再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程


if __name__ == '__main__':
    main()    
    