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

    def test_case_03(self):
        response_data = self.excel_data.get_case_data(self.file_name,2,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_04(self):
        response_data = self.excel_data.get_case_data(self.file_name,3,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_05(self):
        response_data = self.excel_data.get_case_data(self.file_name,4,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_06(self):
        response_data = self.excel_data.get_case_data(self.file_name,5,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_07(self):
        response_data = self.excel_data.get_case_data(self.file_name,6,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_08(self):
        response_data = self.excel_data.get_case_data(self.file_name,7,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_09(self):
        response_data = self.excel_data.get_case_data(self.file_name,8,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_10(self):
        response_data = self.excel_data.get_case_data(self.file_name,9,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_11(self):
        response_data = self.excel_data.get_case_data(self.file_name,10,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_12(self):
        response_data = self.excel_data.get_case_data(self.file_name,11,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_13(self):
        response_data = self.excel_data.get_case_data(self.file_name,12,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_14(self):
        response_data = self.excel_data.get_case_data(self.file_name,12,2,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_15(self):
        response_data = self.excel_data.get_case_data(self.file_name,13,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_16(self):
        response_data = self.excel_data.get_case_data(self.file_name,14,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_17(self):
        response_data = self.excel_data.get_case_data(self.file_name,15,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_18(self):
        response_data = self.excel_data.get_case_data(self.file_name,16,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_19(self):
        response_data = self.excel_data.get_case_data(self.file_name,17,1,content_type="multipart/form-data; boundary=Boundary+76727AD6F3A1D284")
        print("\n返回数据：",response_data)

    def test_case_20(self):
        response_data = self.excel_data.get_case_data(self.file_name,18,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)

    def test_case_21(self):
        response_data = self.excel_data.get_case_data(self.file_name,19,1,content_type="application/json;charset=UTF-8")
        print("\n返回数据：",response_data)




if __name__ == '__main__':
    # runner = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(runner)
    unittest.main()