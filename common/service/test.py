#!user/bin/python3
#coding='utf-8'

import time
import datetime
import os
import pymysql

# print(time.time())
# print(datetime.datetime.now())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# hour_stamp = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
# print(hour_stamp)
# hour_stamp = hour_stamp + datetime.timedelta(hours=24)
# print(hour_stamp)
# file = './../testcase/LoginTest.py'
# dir = os.path.abspath(file)
# print(dir)
# rdir = os.path.dirname(dir)
# print(rdir)
# print(__file__)
# cwd = os.getcwd()
# print(cwd)
# file1 = "./../data/customer.xlsx"
# wholedir = os.path.abspath(file1)
# print(wholedir)
root = __file__.split('common')[0]
rootpath = root + 'data\\customer.xlsx'
print(rootpath)