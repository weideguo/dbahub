"""

'r', 'w' or 'a' 读 写 增加
'b'  二进制形式打开
'+'  允许同时读写 
rb+ r+ w+ wb+
"""

#需要进行显示关闭
f=open("/root/ansible-2.7.4.zip","rb")
f.read()
f.close()


#结束模块时自动关闭 不必显式关闭
with open("/root/ansible-2.7.4.zip","rb") as f:
    f.read()
    
