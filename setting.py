#!user/bin/python3
#coding=utf-8
#setting.py文件放的是我们用到的一些常量
import logging
import os
import time
import inspect

#Log日志设置

#获取当前文件路径
file_path = inspect.stack()[0][1]
cwd = os.path.split(file_path)[0]
#以下设置会在log文件夹下生成.log日志
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s'
                            '%(filename)s'
                            '%(funcName)s'
                            '[line:%(lineno)d]'
                            '%(levelname)s'
                            ':%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='%s/log/%s.log' % (cwd, time.strftime("%y-%m-%d")),
                    filemode='a')

#環境配置
ENVIRONMENT_CONFIG = {
    "interfaceUrl": {
        "Pre": "http://shuitupaycallbackpre.callme.work",
        "Test": "http://shuitupaycallbacktest.callme.work"
    }
}

#电子邮件配置
EMAIL_CONFIG = {
    'sender':'wcyhwcx@163.com',
    'receiver':['510961914@qq.com','wangchengyin@huwo.tech'],
    'subject':'接口测试报告',
    'smtpserver':'smtp.163.com',
    'username': 'wcyhwcx@163.com',
    'password': 'qaz3320197'
}

#token設置
TOKEN = {"token":""}

#數據庫設置
database = {
    'Pre':{
            'host':'172.29.0.204',
            'port':3306,
            'username':'root',
            'password':'root123'
          },
    'Test':{
            'host': '127.0.0.0',
            'port': 8080,
            'username': 'sdhjksdhfk',
            'password': 'sdfds56156'
          }
}
