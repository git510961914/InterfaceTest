#!user/bin/python3
#coding=utf-8
#setting.py文件放的是我们用到的一些常量
import logging
import os
import time
import inspect

"""
Log日志设置
"""
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
'''
ENVIRONMENT CONFIG
'''
ENVIRONMENT_CONFIG = {
    "interfaceUrl": {
        "login": "https://tcc.taobao.com"
    }
}

'''
电子邮件配置
'''
EMAIL_CONFIG = {
    'sender':'wcyhwcx@163.com',
    'receiver':['510961914@qq.com','wangchengyin@huwochuxing.com'],
    'subject':'接口测试报告',
    'smtpserver':'smtp.163.com',
    'username': 'wcyhwcx@163.com',
    'password': 'qaz3320197'
}
