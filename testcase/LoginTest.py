#!user/bin/python3
#coding=utf-8
import json
import logging
import unittest
from common.service import excel_case_data

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n\n初始化数据")
        cls.sheet_index = 0
        cls.excel_data = excel_case_data.ExcelData()
        #excel文件位置
        cls.file_name = "D:\\Pycharm\\PycharmProject\\InterfaceTest\\data\\driver.xlsx"
        logging.info("======This is setUp function======")

    @classmethod
    def tearDownClass(cls):
        print("\n清理数据")
        logging.info("======This is tearDown function======")

    def test_case_01(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=self.sheet_index, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)  #将json格式字符串自动转换成字典
            #excel_data_input = json.dumps(excel_data_input)  #dict转为json
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=self.sheet_index, row_id=1 ,data=excel_data_input)
        print("\n返回数据：" + str(response_data))

    def test_case_02(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=1, row_id=1)
        print("\nExcel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=1, row_id=1 ,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_03(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=2, row_id=1)
        print("\nExcel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=2, row_id=1,data=excel_data_input)
        print("\n返回数据：" + str(response_data))

    def test_case_04(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=3, row_id=1)
        print("\nExcel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=3, row_id=1,data=excel_data_input)
        print("\n返回数据：" + str(response_data))

    def test_case_05(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=4, row_id=1)
        print("\nExcel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=4, row_id=1,data=excel_data_input)
        print("\n返回数据：" + str(response_data))

    def test_case_06(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=5, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=5, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_07(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=6, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=6, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_08(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=7, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=7, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_09(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=8, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=8, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_10(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=9, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=9, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_11(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=10, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=10, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_12(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=11, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=11, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_13(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=12, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=12, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_14(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=12, row_id=2)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=12, row_id=2,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_15(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=13, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=13, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_16(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=14, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=14, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_17(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=15, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=15, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_18(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=16, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=16, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_19(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=17, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=17, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_20(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=18, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=18, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

    def test_case_21(self):
        input_data = self.excel_data.get_case_input(self.file_name, sheet_index=19, row_id=1)
        print("Excel参数：" + input_data)
        if input_data != '':
            excel_data_input = json.loads(input_data)
        else:
            excel_data_input = None
        response_data = self.excel_data.get_case_data(self.file_name, sheet_index=19, row_id=1,data=excel_data_input)
        print("返回数据：" + str(response_data))

if __name__ == '__main__':
    # runner = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(runner)
    unittest.main()