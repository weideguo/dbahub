#!/bin/env python
# 押注模拟

import time
import random

win_rate = 45               # 胜率

amount_begin = 1024      # 初始额度
max_bet_round = 100       # 最大押注次数

rand_max = 10000            # 随机数范围

bet_begin = 1               # 初次押注额度
bet_round = 1               # 押注次数

bet_current = bet_begin     # 当前赌注

win_count=0

max_amount_round = 0         # 最大赢时的次数
max_amount = amount_begin    # 最大赢时的数额

while amount_begin >0 and bet_round<=max_bet_round:
    if  amount_begin < bet_current:
        bet_current = amount_begin
    
    is_win = random.randint(1,rand_max) <= (rand_max*win_rate/100)
    
    if is_win:
        amount_current = amount_begin+bet_current
        bet_next = bet_begin
    else:
        amount_current = amount_begin-bet_current
        bet_next = bet_current*2
    
    if is_win:
        bet_current = "+%d" % bet_current
        win_count = win_count+1
    else:
        bet_current = "-%d" % bet_current
    
    print(bet_round,amount_begin,bet_current,amount_current,bet_next)
    time.sleep(0.01)
    
    bet_round = bet_round+1
    bet_current = bet_next
    amount_begin = amount_current
    
    if max_amount<=amount_current:
        max_amount = amount_current
        max_amount_round = bet_round-1

print(win_count,bet_round-win_count-1,win_count/(bet_round-1))
print(max_amount_round,max_amount)
