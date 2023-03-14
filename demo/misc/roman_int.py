#!/bin/env python
# coding: utf-8

def romanToInt(s):
    """
    罗马数字转成阿拉伯数字
    """
    base = {
    "I": 1   ,
    "V": 5   ,
    "X": 10  ,
    "L": 50  ,
    "C": 100 ,
    "D": 500 ,
    "M": 1000,
    }
    
    n=0
    tmp = 0                         #临时存放尚未累加的一个或多个数字转换值，因为其中可能需要改变数字符号
    _tmp = 0                        #存放每个字母的原始数字转换值
    l = len(s)
    if l ==1:
        return base[s]
    
    for i in range(l):
        #print(s[i])
        _tmp = base[s[i]]
        next_temp = base[s[i+1]]
        if _tmp == next_temp:
            tmp = tmp+_tmp
            _tmp=0
        elif _tmp < next_temp:
            tmp = tmp+_tmp
            tmp = -tmp
            _tmp=0
        elif _tmp > next_temp:
            n = tmp+_tmp+n
            tmp=0
        
        #print(tmp,n)
        if i+2 == l:
            #print(s[i+1])
            return tmp+next_temp+n

 


"""
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

"""
def intToRoman(n):
    """
    阿拉伯数字转成罗马数字
    int < 3999 MMMCMXCIX
    """
    base = {
    "I": 1   ,
    "V": 5   ,
    "X": 10  ,
    "L": 50  ,
    "C": 100 ,
    "D": 500 ,
    "M": 1000,
    }
    if n>3999:
        raise Exception("not legal int, should less than 3999")
    
    
    # 1000
    M_nums = int(n/1000)
    sub = n-M_nums*1000
    
    # 900 
    CM_nums = 0
    
    if sub>=900:
        sub = sub-900
        CM_nums = 1
    
    # 500
    D_nums = 0
    if sub>=500:
        D_nums = 1
        sub = sub-500
    
    # 400
    CD_nums = 0
    if sub>=400:
        sub = sub-400
        CD_nums = 1
    
    # 100
    C_nums = int(sub/100)
    sub = sub-C_nums*100
    
    # 90
    XC_nums = 0
    if sub>=90:
        sub = sub-90
        XC_nums = 1
    
    # 50
    L_nums = 0
    if sub>=50:
        sub = sub-50
        L = 1
    
    # 40
    XL_nums = 0
    if sub>=40:
        sub = sub-40
        XL_nums = 1
    
    # 10
    X_nums = int(sub/10)
    sub = sub-X_nums*10
    
    # 9
    IX_nums = 0
    if sub>=9:
        sub = sub-9
        IX_nums = 1
    
    # 5
    V_nums = 0
    if sub>=5:
        sub = sub-5
        V_nums = 1
    
    # 4
    IV_nums = 0
    if sub>=4:
        sub = sub-4
        IV_nums=1
        
    
    I_nums=sub
    
    
    s = 'M'*M_nums +'CM'*CM_nums +\
        'D'*D_nums +'CD'*CD_nums +\
        'C'*C_nums +'XC'*XC_nums + \
        'L'*L_nums +'XL'*XL_nums +\
        'X'*X_nums +'IX'*IX_nums + \
        'V'*V_nums +'IV'*IV_nums +\
        'I'*I_nums
    
    return s
    

print(romanToInt("III")) 
print(intToRoman(999))


