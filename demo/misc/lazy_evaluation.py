# lazy evaluation 
# 惰性求值 

# builds a big list and immediately discards it
sum([x*x for x in range(2000000)])
2666664666667000000L
 
# only keeps one value at a time in memory
sum(x*x for x in range(2000000))



from itertools import islice

["no sleep", time.sleep(1), time.sleep(2)][0]
#'no sleep'  # takes 3 seconds to print

list(islice((time.sleep(x) for x in range(3)), 1))
#[None] # takes 0 seconds
list(islice((time.sleep(x) for x in range(3)), 2))
#[None, None] # takes 1 second
list(islice((time.sleep(x) for x in range(3)), 3))
#[None, None, None] # takes 3 seconds


[lambda: "no sleep", lambda: time.sleep(1), lambda: time.sleep(2)][0]()
#'no sleep' # takes 0 seconds




def f():
    i = 0
    while i<10:
        i += 1
        print("-----------"+str(i))
        yield i


import time
for x in f():
    time.sleep(2)
    print(x)
    
#使用多少才生成多少    
    

