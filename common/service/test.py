#!user/bin/python3
#coding=utf-8

import time
import datetime
import pymysql

if __name__ == '__main__':
    # runner = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(runner)
    print(time.time())
    print(datetime.datetime.now())
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    hour_stamp = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
    print(hour_stamp)
    hour_stamp = hour_stamp + datetime.timedelta(hours=24)
    print(hour_stamp)