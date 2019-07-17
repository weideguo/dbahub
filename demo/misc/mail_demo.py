#coding:utf8
#发送邮件
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
import os

#如163 smtp.163.com 465
#qq    smtp.qq.com 25
smtp_server="smtp_server"
smtp_port=465

from_addr="your_email"
# 这里的密码是开启smtp服务时输入的客户端登录授权码，并不是登录网页邮箱使用的密码
password='smtp_password'
to_addr=["fake_name@fake.com"]
    

def get_smtp(from_addr, password):
    smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    #smtp.set_debuglevel(1)
    #smtp.ehlo(smtp_server)
    smtp.login(from_addr, password)
    return smtp
    
    
def msg_text(title,content):    
    """
    发送文字
    """
    msg = MIMEText(content,'html','utf-8')
    msg['From'] = '%s' % from_addr              #可以为<%s>
    msg['To'] = '%s' % ','.join(to_addr)        #多个可以用","分隔   msg['Cc'] 抄送
    msg['Subject'] = title
    
    return msg
    
    
def msg_attach(title,content,file):    
    """
    带有附件
    """
    msg = MIMEMultipart()
    msg['From'] = '%s' % from_addr
    msg['To'] = '%s' % ','.join(to_addr)
    msg['Subject'] = title
    
    part_attach = MIMEApplication(open(file,'rb').read())                      #打开附件
    part_attach.add_header('Content-Disposition','attachment',filename=os.path.basename(file))   #为附件命名
    
    msg.attach(part_attach)
    msg.attach(MIMEText(content,_charset='utf-8'))   
    
    return msg
    
    
def msg_png(title,content,file):  
    """
    直接在邮件内显示
    """
    msg = MIMEMultipart()
    msg['From'] = '%s' % from_addr
    msg['To'] = '%s' % ','.join(to_addr)
    msg['Subject'] = title
    
    with open(file, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename=os.path.basename(file))
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
        mime.add_header('Content-ID', 'a')
        mime.add_header('X-Attachment-Id', '1')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    
    #使用的cid 为 Content-ID设置的值        
    msg.attach(MIMEText('<html><body><h1>' +content+
        '</h1><p><img src="cid:a"></p>' +
        '</body></html>', 'html', 'utf-8'))    
    
    return msg
        
    
    
if __name__ == "__main__":   
    
    smtp=get_smtp(from_addr,password,)
    
    #msg=msg_text('标题','正文内容')
    #msg=msg_attach('标题','正文内容','/root/test2/superman.png')
    msg=msg_png('标题','正文内容','/root/test2/superman.png')
    
    smtp.sendmail(from_addr, to_addr, msg.as_string())


