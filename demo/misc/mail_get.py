#coding:utf8
import poplib  
import email,os,re
from email import Header

#M = poplib.POP3('pop.exmail.qq.com')  
M = poplib.POP3_SSL('pop.exmail.qq.com',port=995)   
M.user('my_email@email_domain')                   
M.pass_('my_email_passwd')                                 

#服务端保存的文件数量 需要在服务端自行设置保留机制，或者设置获取后直接删除，以防止获取太久之前的邮件
message_num = M.stat()[0]

for i in range(message_num): 
    m = M.retr(i+1)
    msg = email.message_from_string('\n'.join(m[1]))
    print(msg)
    print(msg['subject'])
    
    
    
"""
SMTP        用于客户端向服务端发送、服务端向服务端发送
POP3/IMAP   用于客户端向服务端获取
"""    
    
