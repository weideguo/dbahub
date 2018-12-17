#pip install pyotp


"""
TOTP  Time-based One-time Password Algorithm 
is an extension of the HMAC-based OneTime Password algorithm HOTP to support a time based moving factor
HMAC -Hash-based Message Authentication Code


HOTP(K,C) = Truncate(HMAC-SHA-1(K,C))

K 密钥种子
C 基于时间戳的变化周期

实现基于时间的动态密码验证

客户端 服务端只需要保证密钥相同
"""




import pyotp

#Generating a base32 Secret Key
pyotp.random_base32()



#客户端
totp = pyotp.TOTP('base32secret3232')
totp.now()                                # => '492039'



#服务端
totp = pyotp.TOTP('base32secret3232')
totp.verify('492039')                     # => True
time.sleep(30)
totp.verify('492039')                     # => False

