
"""
有五只猴子，分一堆桃子，可是怎么也平分不了，于是大家同意先去睡觉，明天再说。
一只猴子偷偷起来，把一个桃子扔到山下后正好可以分成五份，它把自己的一份收藏起来就睡觉去了。
第二只猴子起来也扔了一个刚好分成五份，也把自己那一份收藏起来。
第三、第四、第五只猴子都是这样，扔了一个也刚好可以分成五份，问一共有多少桃子？
"""
import time

n = 1
next_flag = True
m = 5
while next_flag:
    nx = n
    while m>0:
        if (nx - 1)>0 and  nx % 5 !=0 and (nx-1) % 5 ==0:
            nx = (nx-1)*4/5
            m = m-1
            print(n,m)
            #time.sleep(0.01)
        else:
            m = -1
    
    if m == 0:
        next_flag = False
    else:
        m = 5
        n = n+1   
        # n = n+5    # n 只可能个位数为1或6，因此加5更快
    

m = 5    
nx = n
while m>0:
    _nx = (nx-1)*1/5
    print(nx,_nx) 
    nx = (nx-1)*4/5
    m = m-1
      

