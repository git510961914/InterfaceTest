#!user/bin/python3
#coding=utf-8
import json
import logging
import unittest
from InterfaceTest.common.service import excel_case_data

class LoginTest(unittest.TestCase):
    def setUp(self):
        print("初始化数据")
        self.sheet_index = 0
        self.excel_data = excel_case_data.ExcelData()
        #excel文件位置
        self.file_name = "D:\\Pycharm\\Project\\InterfaceTest\\data\\testcase.xlsx"
        logging.info("======This is setUp function======")

    def tearDown(self):
        print("清理数据")
        logging.info("======This is tearDown function======")

    def test_case_01(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=self.sheet_index, row_id=1)
        print(input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)  #将json格式字符串自动转换成字典
            print(excel_data_input)
            #excel_data_input = json.dumps(excel_data_input)  #dict转为json
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=1 ,data=excel_data_input)
        print(response_data)

    def test_case_02(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=self.sheet_index, row_id=2)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=2 ,data=excel_data_input)
        print(response_data)
if __name__ == '__main__':
    # runner = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(runner)
    unittest.main()