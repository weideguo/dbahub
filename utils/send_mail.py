#!/usr/bin/env python2.7
#coding=utf-8  
#
# vim mail_config.conf
# [s1]
# mailto=abc1@abc.com,abc2@abc.com
# project=project_name
# filename=file_name
#
# [s2]
# mailto=abc11@abc.com,abc22@abc.com
# project=project_name1
# filename=file_name1 


import sys
import os  
import smtplib  
import mimetypes  
import ConfigParser
import codecs
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEBase import MIMEBase  
from email.MIMEText import MIMEText  
from email.MIMEAudio import MIMEAudio  
from email.MIMEImage import MIMEImage  
from email.Encoders import encode_base64  

mailFrom = 'mail_address'
mailPassword = 'mail_pwd'
smtp_host='smtp_host'
smtp_port=25
  
def sendMail(mailTo,subject,text, *attachmentFilePaths):  	
    msg = MIMEMultipart()  
    msg['From'] =mailFrom  
    msg['To'] = mailTo
    msg['Subject'] = subject  
    msg.attach(MIMEText(text))  
    
    for attachmentFilePath in attachmentFilePaths:  
        msg.attach(getAttachment(attachmentFilePath))  
    
    mailServer = smtplib.SMTP(smtp_host,smtp_port)  
    mailServer.ehlo()  
    mailServer.starttls()  
    mailServer.ehlo()  
    mailServer.login(mailFrom, mailPassword)  
    mailServer.sendmail(mailFrom,mailTo.split(','), msg.as_string())  
    #mailServer.sendmail(mailFrom, mailTo, msg.as_string())  
    mailServer.close()  
    
    print('Sent email to %s' % mailTo)  
  
def getAttachment(attachmentFilePath):  
    contentType, encoding = mimetypes.guess_type(attachmentFilePath)  
    if contentType is None or encoding is not None:  
        contentType = 'application/octet-stream'  
    mainType, subType = contentType.split('/',1) 
    
    file = open(attachmentFilePath,'rb')  
    
    attachment = MIMEBase(mainType, subType)  
    attachment.set_payload(file.read())  
    encode_base64(attachment)  
    
    file.close()  
    
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachmentFilePath))  
	return attachment  
    
if  __name__ == '__main__':
    config_file=sys.path[0]+'/mail_config.conf'
    cp=ConfigParser.SafeConfigParser()
    with codecs.open(config_file,'r',encoding='utf-8') as f:
        cp.readfp(f)
    secs=cp.sections()
    for sec in secs:
        mailTo=cp.get(sec,'mailto')
        project=cp.get(sec,'project').encode('utf-8')
        mail_subject='title is : %s'%project
        mail_content='''
        hi,
        %s
        '''%project
    
        attachmentFilePath=sys.path[0]+'/'+cp.get(sec,'filename')
    
        sendMail(mailTo,mail_subject,mail_content,attachmentFilePath)
