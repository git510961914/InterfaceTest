#!user/bin/python3
#coding=utf-8
import json
import logging
import requests
from InterfaceTest.common.module import excel_module
from InterfaceTest.common.module import requests_module
from InterfaceTest.common.module import environment_module

class ExcelData:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.data_send = ''
        self.expect_res = ''
        self.data = {}
        self.case_url = ''
        self.case_input = ''
        self.content_type = ''

    def get_case_data(self, file_name, sheet_index=0, row_id=0, data=None, **kwargs):
        """
        # 形参*param表示创建一个名为param的空元组，并将所有收到的值都封装到这个元组中
        # 形参**param表示创建一个名为param的空字典，并将收到的所有键-值对都封装到这个字典中
        1、获取对应id的行的内容
        2、获取url
        3、获取请求方式
        4、获取请求参数，并进行转码
        5、获取预期结果
        6、获取string类型的response
        :param file_name: xlsx文件名
        :param sheet_index: sheet索引
        :param row_id: 行索引
        :param data: 不用Excel表里的数据，自己传
        :param kwargs: 替换excel表里的某个key的value
        :return: expect_res, actual_res
        """
        # 读取Excel
        excel_handle = excel_module.ReadExcel(file_name)
        # 获取指定sheet
        sheet = excel_handle.sheet_by_index(sheet_index)
        # 读取指定行
        case_data_list = excel_handle.row_values(sheet, row_id)
        # 获取第row_id行第2列的数据(路径)
        path = case_data_list[1]
        print("path: ", path)
        # 获取完整url
        self.get_url(path)
        print(self.get_url(path))
        # ID、Path、Request、Input、Expect
        # 获取发送方式（Request）
        self.method = case_data_list[2]
        # 获取请求参数
        self.data_send = case_data_list[3]
        # 获取期望返回数据
        self.expect_res = case_data_list[4]
        print(self.expect_res)
        # 字符串转字典
        if self.data_send != '':
            self.data = json.loads(self.data_send, encoding='utf-8')
        logging.info(self.data_send)
        if data is not None:
            self.data = data
        if kwargs is not None:
            for i in kwargs:
                for j in self.data:
                    # 如果传参key和发送内容key相同，则替换Excel表中的对应key的value
                    if i == j:
                        self.data[j] = kwargs[i]
        expect_res = self.get_expect_data()
        # 遍历传参，如果有cookie字段则将该cookie赋值给access_token
        access_token = ''
        for i in kwargs.keys():
            if i == 'cookie':
                access_token = kwargs[i]
        if access_token.strip() == '':  #strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
            actual_res = self.get_actual_data()
        else:
            actual_res = self.get_actual_data(access_token)

        return expect_res,actual_res

    def get_case_input(self, file_name, sheet_index=0, row_id=0):
        """
        获取输入数据
        :param file_name: 文件路径
        :param sheet_index: sheet索引
        :param row_id: 行索引
        :return: Excel表中的传入数据
        """
        excel_handle = excel_module.ReadExcel(file_name)
        sheet = excel_handle.sheet_by_index(sheet_index)
        case_data = excel_handle.row_values(sheet, row_id)
        self.data = case_data[3]
        return self.data

    def get_url(self, path):
        self.url = environment_module.EnvironmentModule().get_env_url('login') + path
        return self.url

    def get_expect_data(self):
        logging.debug("=============Expect============" + self.expect_res)
        return self.expect_res.encode('utf-8')

    #发送请求并分析返回数据
    def get_actual_data(self,access_token=None):
        # headers = setting.REQUEST_HEADER
        # headers['Content-Type'] = self.content_type['Content-Type']
        # for i in kwargs:
        #     if i == "access_token":
        #         headers['Cookies'] = kwargs[i]
        self.data['access_token'] = access_token
        actual_res_handle = requests_module.GetResponse(self.url,method=self.method)
        actual_url = actual_res_handle.get_response(data=self.data)
        res_analysis = requests_module.AnalysisResponse(actual_url)
        actual_res = res_analysis.str_content
        cookies = requests.utils.dict_from_cookiejar(res_analysis.cookies)
        # logging.debug(u"===============data==============") + json.dumps(self.data)
        logging.debug((u"===========实际返回的数据为：%s============") % actual_res)
        #print(actual_res)
        return actual_res, cookies