import crypt
password = "19241112";
print(crypt.crypt(password))
# 生成的密码格式跟centos的一致，替换/etc/shadow文件对应记录即可实现密码修改


import crypt
import getpass
# 交互方式获取字符串
password = getpass.getpass()                
if (password == getpass.getpass("Confirm: ")):
    print(crypt.crypt(password) 


# 自定义salt
crypt_type = "$1$"   # MD5
crypt_type = "$5$"   # sha-256
crypt_type = "$6$"   # sha-512
            
salt = crypt_type + "some_random_string"
crypt.crypt(password, salt)  


# METHOD_MD5·
# METHOD_SHA256 
# METHOD_SHA512 
crypt.mksalt(crypt.METHOD_SHA512)


