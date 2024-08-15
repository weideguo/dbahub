#!/bin/env python
# 下注后，去除一张不中的牌，更换下注命中率

import time
import random
import copy

rand_max = 100000000            # 随机数范围，更大的数随机数更均匀

imitate_round = 10000           # 迭代次数，更多次更能模拟真实情况

win_count = 0

is_switch = 1                  # 是否换下注

init_faces = [False,False,False]   # 初始牌面
faces_len = len(init_faces)

def pop_one(bet_index,faces):
    # 获取一张不中牌的偏移量
    r = random.randint(1,rand_max)
    # 去除的偏移量
    for i in range(0,faces_len-1):
        if r <= rand_max*(i+1)/(faces_len-1):
            bet_index_gap = i+1
            break
    
    pop_temp_index = (bet_index+bet_index_gap) % faces_len
    if faces[pop_temp_index]:
        #print(bet_index_gap)
        return pop_one(bet_index,faces)
    else:
        return bet_index_gap
 

for i in range(0,imitate_round):
    
    # 牌面设置一张命中
    faces = copy.deepcopy(init_faces)
    r = random.randint(1,rand_max)
    for i in range(0,faces_len):
        if r <= rand_max*(i+1)/faces_len:
            faces[i] = True
            break   
            
    #print(faces)
    
    # 第一次下注
    r = random.randint(1,rand_max)
    for i in range(0,faces_len):
        if r <= rand_max*(i+1)/faces_len:
            bet_index = i
            break
    
    #print(bet_index)
    
    pop_index_gap = pop_one(bet_index,faces) 
    pop_index = (bet_index+pop_index_gap) % faces_len
    
    bet_index_list = [i for i in range(0,faces_len)]
    if is_switch:
        # 更换下注
        bet_index_list.remove(bet_index)  # remove为根据值移除
        bet_index_list.remove(pop_index)
        bet_index_list_len = len(bet_index_list)
        # 从剩余牌中随机选
        r = random.randint(1,rand_max)
        for i in range(0,bet_index_list_len):
            if r <= rand_max*(i+1)/bet_index_list_len:
                new_bet_index = bet_index_list[i]
        
        
        real_bet_index = new_bet_index
    else:
        real_bet_index = bet_index
        
    is_win = faces[real_bet_index]
    
    if is_win:
        win_count = win_count +1
    
    #print(bet_index,pop_index,real_bet_index,faces,is_win)

print(win_count,imitate_round,win_count/imitate_round)    

    