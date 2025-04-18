###########################################################
def generator():
    i = 1
    while True:
        yield i
        i += 1

from itertools import islice
 
def take(n, iterable):
    '''Return first n items of the iterable as a list'''
    return list(islice(iterable, n))

print(take(5, generator()))
#即为实现range(0,5)


def primes():
    for n in generator():
        if not any(i > 1 and i != n and n%i == 0 for i in islice(generator(), n)):
            yield n

print(take(10, primes()))
#求素数


############################################################
#islice跟slice类似，但返回的是迭代器
for i in islice(range(0,10),5):
    print(i)


# 设置截取5个元素的切片
myslice = slice(5)    
myslice
#slice(None, 5, None)
arr = range(10)
arr
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr[myslice]         # 截取 5 个元素
#[0, 1, 2, 3, 4



list(range(0,5))   #将迭代器转换成list


############################################################
# 创建迭代器
my_iterator = iter([1, 2, 3])

# 迭代器转成列表
list(my_iterator)

