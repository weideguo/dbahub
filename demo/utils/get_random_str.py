#!/bin/env python
# -*- coding: utf-8 -*-
import random

number_str="1234567890"
special_identifier="~!@#$%^&*-=[];',./<>?:{}|_+"
lower_alphabet_str="qwertyuiopasdfghjklzxcvbnm"
upper_alphabet_str="QWERTYUIOPASDFGHJKLZXCVBNM"

basic_str=number_str+special_identifier+lower_alphabet_str+upper_alphabet_str

bs_len=len(basic_str)

def get_next_unique_char(origin_str):
    next_unique_char=basic_str[random.randint(0,bs_len-1)]
    if len(origin_str)==0:
        return next_unique_char
    elif origin_str[-1]==next_unique_char:
        next_unique_char=get_next_unique_char(origin_str)
    return next_unique_char

def get_simple_random_str(n):
    generated_str=""
    for i in range(n):
        generated_str=str(generated_str)+str(get_next_unique_char(generated_str))
    return generated_str	

def get_universal_random_str(n):
    universal_generated_str=""
    for i in range(n):
        universal_generated_str=universal_generated_str+unichr(random.randint(0x0001,0x9FA5)) 
    return universal_generated_str

if __name__=="__main__":
    print(get_simple_random_str(9))
