#!user/bin/python3
#coding=utf-8
import unittest
from InterfaceTest.common.module import email_module

def all_case():
    # 你的文件路径
    case_dir = r"D:\PyCharm\PycharmProject\InterfaceTest\testcase"
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="*Test.py", top_level_dir=None)
    return discover

if __name__ == '__main__':
    # 导入HTMLTestRunner模块
    from InterfaceTest.common.integretion import HTMLTestRunner
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_path = r"D:\PyCharm\PycharmProject\InterfaceTest\report.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况")
    runner.run(all_case())
    fp.close()
    # 调用封装好的sendMail方法，参数为上面的文件
    mail = email_module.sendMail(report_path)
    print("Email sending Success")
