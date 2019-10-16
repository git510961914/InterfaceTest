#!user/bin/python3
#coding=utf-8
import json
import logging
import unittest
from common.service import excel_case_data

class LoginTest(unittest.TestCase):
    def setUp(self):
        print("\n\n初始化数据")
        self.sheet_index = 0
        self.excel_data = excel_case_data.ExcelData()
        #excel文件位置
        self.file_name = "D:\\Pycharm\\PycharmProject\\InterfaceTest\\data\\driver.xlsx"
        logging.info("======This is setUp function======")

    def tearDown(self):
        print("\n清理数据")
        logging.info("======This is tearDown function======")

    def test_case_01(self):
            #excel_data_input = json.loads(input_data)  #将json格式字符串自动转换成字典
            #excel_data_input = json.dumps(excel_data_input)  #dict转为json
        response_data = self.excel_data.get_case_data(self.file_name,self.sheet_index,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_02(self):
        response_data = self.excel_data.get_case_data(self.file_name,1,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)



if __name__ == '__main__':
    # runner = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(runner)
    unittest.main()