#!user/bin/python3
#coding=utf-8
import logging
import unittest
import datetime
from common.service import excel_case_data
from common.module import database

class LoginTest(unittest.TestCase):
    def setUp(self):
        print("初始化数据")
        self.sheet_index = 0
        self.excel_data = excel_case_data.ExcelData()
        #excel文件位置
        self.file_name = "D:\\Pycharm\\PycharmProject\\InterfaceTest\\data\\customer.xlsx"
        logging.info("======This is setUp function======")

    def tearDown(self):
        print("清理数据\n")
        logging.info("======This is tearDown function======")

    def test_01_isMemberExist(self):
        #excel_data_input = json.loads(input_data)  #将json格式字符串自动转换成字典
        #excel_data_input = json.dumps(excel_data_input)  #dict转为json
        print("开始test_01_isMemberExist接口")
        response_data = self.excel_data.get_case_data(self.file_name,self.sheet_index,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_02_login(self):
        print("开始test_02_login接口")
        response_data = self.excel_data.get_case_data(self.file_name,1,1,content_type="application/json")
        data = response_data['data']
        token = data['token']
        print("最新token：" + token)
        self.excel_data.set_token(token)
        print("返回数据：",response_data)

    def test_03_getMemberInfo(self):
        print("开始test_03_getMemberInfo接口")
        response_data = self.excel_data.get_case_data(self.file_name,2,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_04_checkAppVersion(self):
        print("开始test_04_checkAppVersion接口")
        response_data = self.excel_data.get_case_data(self.file_name,3,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_05_getNotFinishedOrder(self):
        print("开始test_05_getNotFinishedOrder接口")
        response_data = self.excel_data.get_case_data(self.file_name,4,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_06_requirement(self):
        print("开始test_06_requirement接口")
        response_data = self.excel_data.get_case_data(self.file_name,5,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_07_adfind(self):
        print("开始test_07_adfind接口")
        response_data = self.excel_data.get_case_data(self.file_name,6,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_08_bizCityfind(self):
        print("开始test_08_bizCityfind接口")
        response_data = self.excel_data.get_case_data(self.file_name,7,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_09_isEnableService(self):
        print("开始test_09_isEnableService接口")
        response_data = self.excel_data.get_case_data(self.file_name,8,1,content_type="multipart/form-data; boundary=Boundary+9D54A8EEADF4A41C")
        print("返回数据：",response_data)

    def test_10_findRecommendLine(self):
        print("开始test_10_findRecommendLine接口")
        response_data = self.excel_data.get_case_data(self.file_name,9,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_11_listLineSameTime(self):
        print("开始test_11_listLineSameTime接口")
        response_data = self.excel_data.get_case_data(self.file_name,10,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_12_calcEstimatePrice(self):
        print("开始test_12_calcEstimatePrice接口")
        response_data = self.excel_data.get_case_data(self.file_name,11,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_13_contractslist(self):
        print("开始test_13_contractslist接口")
        response_data = self.excel_data.get_case_data(self.file_name,12,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_14_couponfind(self):
        print("开始test_14_couponfind接口")
        response_data = self.excel_data.get_case_data(self.file_name,13,1,content_type="application/json")
        print("返回数据：",response_data)

    # def test_15_createH5APPOrder(self):
    #     print("开始test_15_createH5APPOrder接口")
    #     hour_stamp = datetime.datetime.now().replace(minute=0, second=0, microsecond=0) #获取当前时间整点时间戳
    #     date_from = hour_stamp + datetime.timedelta(hours=24)
    #     date_to = hour_stamp + datetime.timedelta(hours=25)
    #     sql = 'select * from biz_coupondetail where detailId="711733"'
    #     db = database.Database('Pre')
    #     res = db.query(sql)
    #     response_data = self.excel_data.get_case_data(self.file_name,14,1,content_type="application/json",dateFrom=date_from,dateTo=date_to,detailId=res)
    #     print("返回数据：",response_data)

    #
    # def test_16_calculatePCCoupon(self):
    #     print("开始test_16_calculatePCCoupon接口")
    #     response_data = self.excel_data.get_case_data(self.file_name,15,1,content_type="application/json")
    #     print("返回数据：",response_data)
    #
    # def test_17_createPayment(self):
    #     print("开始test_17_createPayment接口")
    #     response_data = self.excel_data.get_case_data(self.file_name,16,1,content_type="application/json")
    #     print("返回数据：",response_data)

if __name__ == '__main__':
    # runner = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(runner)
    unittest.main()