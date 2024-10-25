
"""
pip install bcrypt
将密码进行hash，相对于md5更加安全
"""

import bcrypt
 
# 密码原文
password = b"this_is_my_password"

# len(password) <= 72 的度影响计算结果，之后的长度不影响计算结果？

#salt = bcrypt.gensalt()
# rounds=10     迭代多少轮 2**10=1024
# prefix=b"2a"
# prefix=b"2b"
salt = bcrypt.gensalt(rounds=10,prefix=b"2a")

hashed = bcrypt.hashpw(password, salt)
 
print(hashed)


# 校验
bcrypt.checkpw(password, hashed)

