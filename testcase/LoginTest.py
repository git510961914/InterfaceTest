#!user/bin/python3
#coding=utf-8
import logging
import unittest
import datetime
import os
from common.service import excel_case_data
from common.module import database
from common.temp import cashdata

class LoginTest(unittest.TestCase):
    def setUp(self):
        print("初始化数据")
        self.sheet_index = 0
        self.excel_data = excel_case_data.ExcelData()
        #excel文件位置
        self.file_name = "D:\\Pycharm\\PycharmProject\\InterfaceTest\\data\\customer.xlsx"
        self.dbEnv = 'Pre'
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

    def test_12_contractslist(self):
        print("开始test_12_contractslist接口")
        response_data = self.excel_data.get_case_data(self.file_name,11,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_13_couponfind(self):
        print("开始test_13_couponfind接口")
        response_data = self.excel_data.get_case_data(self.file_name,12,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_14_calcEstimatePrice(self):
        print("开始test_14_calcEstimatePrice接口")
        response_data = self.excel_data.get_case_data(self.file_name,13,1,content_type="application/json")
        data = response_data['data']
        cashdata.ORDER['coupondetailId'] = data['detailId']
        cashdata.ORDER['actualPayFee'] = data['actualPayFee']
        print("返回数据：",response_data)

    def test_15_createH5APPOrder(self):
        print("开始test_15_createH5APPOrder接口")
        hour_stamp = datetime.datetime.now().replace(minute=0, second=0, microsecond=0) #获取当前时间整点时间戳
        date_from = hour_stamp + datetime.timedelta(hours=24)
        date_from = str(date_from)
        date_to = hour_stamp + datetime.timedelta(hours=25)
        date_to = str(date_to)
        detailId = cashdata.ORDER['coupondetailId']
        response_data = self.excel_data.get_case_data(self.file_name,14,1,content_type="application/json",dateFrom=date_from,dateTo=date_to,detailId=detailId)
        data = response_data['data']
        cashdata.ORDER['orderId'] = data['id']
        print("当前订单Id为：orderId=",data['id'])
        cashdata.ORDER['preFee'] = data['preFee']
        print("返回数据：",response_data)

    def test_16_calculatePCCoupon(self):
        print("开始test_16_calculatePCCoupon接口")
        id = cashdata.ORDER['orderId']
        sql = "SELECT * FROM biz_coupondetail WHERE MemberId = 21421 AND CouponId = 132 AND isUser = 0 LIMIT 0,1000"
        db = database.Database(self.dbEnv)
        res = db.query(sql)
        if len(res) <= 1:
             print("优惠券不足了，请添加优惠券再测试")
        else:
            couponDetailId = res[1][0]
            response_data = self.excel_data.get_case_data(self.file_name,15,1,content_type="application/json",couponDetailId=couponDetailId,id=id)
            print("返回数据：",response_data)

    def test_17_createPayment(self):
        print("开始test_17_createPayment接口")
        orderId = cashdata.ORDER['orderId']
        response_data = self.excel_data.get_case_data(self.file_name,16,1,content_type="application/json",orderId=orderId)
        print("返回数据：",response_data)

    def test_18_listDriversByMembershipID(self):
        print("开始test_18_listDriversByMembershipID接口")
        response_data = self.excel_data.get_case_data(self.file_name,17,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_19_cancelCollectionDrivers(self):
        print("开始test_19_cancelCollectionDrivers接口")
        response_data = self.excel_data.get_case_data(self.file_name,18,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_20_collectionDrivers(self):
        print("开始test_20_collectionDrivers接口")
        response_data = self.excel_data.get_case_data(self.file_name,19,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_21_isCollection(self):
        print("开始test_21_isCollection接口")
        response_data = self.excel_data.get_case_data(self.file_name,20,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_22_getTripList(self):
        print("开始test_22_getTripList接口")
        response_data = self.excel_data.get_case_data(self.file_name,21,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_23_getPasOrderInfo(self):
        print("开始test_23_getPasOrderInfo接口")
        response_data = self.excel_data.get_case_data(self.file_name,22,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_24_getDriverInfo(self):
        print("开始test_24_getDriverInfo接口")
        response_data = self.excel_data.get_case_data(self.file_name,23,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_25_orderListInvoiceByMemberId(self):
        print("开始test_25_orderListInvoiceByMemberId接口")
        response_data = self.excel_data.get_case_data(self.file_name,24,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_26_listInvoiceByMemberId(self):
        print("开始test_26_listInvoiceByMemberId接口")
        response_data = self.excel_data.get_case_data(self.file_name,25,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_27_getInvoiceDetailInfo(self):
        print("开始test_27_getInvoiceDetailInfo接口")
        response_data = self.excel_data.get_case_data(self.file_name,26,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_28_getInvoiceOrderInfo(self):
        print("开始test_28_getInvoiceOrderInfo接口")
        response_data = self.excel_data.get_case_data(self.file_name,27,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_29_invoice(self):
        print("开始test_29_invoice接口")
        orderListInvoice = self.excel_data.get_case_data(self.file_name, 24, 1, content_type="application/json")
        data = orderListInvoice['data']
        orderId = data[0]['orderId']
        response_data = self.excel_data.get_case_data(self.file_name,28,1,content_type="application/json",orderIdList=[orderId])
        print("返回数据：",response_data)

    def test_30_unReadfind(self):
        print("开始test_30_unReadfind接口")
        response_data = self.excel_data.get_case_data(self.file_name,29,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_31_systemfind(self):
        print("开始test_31_systemfind接口")
        response_data = self.excel_data.get_case_data(self.file_name,30,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_32_activityfind(self):
        print("开始test_32_activityfind接口")
        response_data = self.excel_data.get_case_data(self.file_name,31,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_33_messageread(self):
        print("开始test_33_messageread接口")
        response_data = self.excel_data.get_case_data(self.file_name,32,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_34_messagedelete(self):
        print("开始test_34_messagedelete接口")
        response_data = self.excel_data.get_case_data(self.file_name,33,1,content_type="application/json")
        print("返回数据：",response_data)

    def test_35_ordersubmit(self):
        print("开始test_35_ordersubmit接口")
        sql = "select * from biz_order WHERE MemberShipID=21421 and state=7 ORDER BY CreateDate DESC LIMIT 0,10"
        db = database.Database(self.dbEnv)
        res = db.query(sql)
        if len(res) == '':
            print("没有待评论的订单")
        else:
            orderId = res[0][0]
            response_data = self.excel_data.get_case_data(self.file_name,34,1,content_type="application/json",id=orderId)
            print("返回数据：",response_data)

    def test_36_commentget(self):
        print("开始test_36_commentget接口")
        response_data = self.excel_data.get_case_data(self.file_name,35,1,content_type="application/json")
        print("返回数据：",response_data)


if __name__ == '__main__':
    # runner = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(runner)
    unittest.main()