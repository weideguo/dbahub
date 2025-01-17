"""
Diffie-Hellman算法
实现共享密钥生成

A=g^a mod p
B=g^b mod p  
 
s1=B^a mod p
s2=A^b mod p 

s1==s2
"""

import random

def generate_keys(p, g):
    # 选择随机整数a，为私钥
    a = random.randint(2, p-2)
    # 计算A=g^a mod p ，为公钥
    A = pow(g, a, p)
    return a, A

def get_shared_secret(a, B, p):
    # 计算共享密钥s=B^a mod p
    s = pow(B, a, p)
    return s
    

# 选择一个大素数p，以及与p互质的整数原根g
p = 37
g = 3

# Alice生成公钥A和私钥a
a, A = generate_keys(p, g)
print("Alice's public key: ", A)

# Bob生成公钥B和私钥b
b, B = generate_keys(p, g)
print("Bob's public key: ", B)

# A传公钥给B，B传公钥给A

# Alice计算共享密钥
s1 = get_shared_secret(a, B, p)

# Bob计算共享密钥
s2 = get_shared_secret(b, A, p)

# 验证共享密钥是否相同
print("Shared secret: ", s1, s1 == s2)

"""
第三方用户即使获取到 p g A B，也不能计算出共享密钥
后续用户A和B可以s1（跟s2一样）为密钥使用对称加密算法（如AES）来加密和解密数据
"""

