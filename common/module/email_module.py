#!user/bin/python3
#coding=utf-8

import setting
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMail(file):
    f = open(file, 'rb')
    #读取测试报告正文
    mail_body = f.read()
    f.close()

    #创建一个带附件的实例
    msg = MIMEMultipart()
    msg['From'] = setting.EMAIL_CONFIG['sender']
    receiver = ','.join(setting.EMAIL_CONFIG['receiver'])
    msg['To'] = receiver
    msg['Subject'] = 'Python test'


    # 邮件正文
    msg.attach(MIMEText('sending email test', 'plain', 'utf-8'))

    # 构造附件1
    att1 = MIMEText(mail_body, 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename= %s' % file
    msg.attach(att1)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(setting.EMAIL_CONFIG['smtpserver'],25)
        smtpObj.login(setting.EMAIL_CONFIG['username'],setting.EMAIL_CONFIG['password'])
        smtpObj.sendmail(setting.EMAIL_CONFIG['sender'],receiver,msg.as_string())
        print('Success')
    except smtplib.SMTPException:
        print('Error')