#!user/bin/python3
#coding=utf-8
import json
import logging
from common.module import excel_module
from common.module import requests_module
from common.module import environment_module

class ExcelData:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.data_send = ''
        self.expect_res = ''
        self.data = {}
        self.case_url = ''
        self.case_input = ''
        self.header = {"c-st":"2","content-type":""}

    def get_case_data(self,file_name,sheet_index=0,row_id=0,**kwargs):
        """
        形参*param表示创建一个名为param的空元组，并将所有收到的值都封装到这个元组中
        形参**param表示创建一个名为param的空字典，并将收到的所有键-值对都封装到这个字典中
        data:不用Excel表里的数据,自己传
        kwargs:替换excel表里的某个key的value
        """
        # 读取Excel
        excel_handle = excel_module.ReadExcel(file_name)
        # 获取指定sheet
        sheet = excel_handle.sheet_by_index(sheet_index)
        # 读取指定行
        case_data_list = excel_handle.row_values(sheet, row_id)
        # 获取第row_id行第2列的数据(路径)
        path = case_data_list[1]
        # 获取完整url
        self.get_url(path)
        print("完整URL：" + self.get_url(path))
        # ID、Path、Request、Input、Expect
        # 获取发送方式（Request）
        self.method = case_data_list[2]
        # 获取请求参数
        self.data_send = case_data_list[3]
        # 获取期望返回数据
        self.expect_res = case_data_list[4]
        print("期望数据：" + self.expect_res)
        # 字符串转字典
        if self.data_send != '':
            self.data = json.loads(self.data_send,encoding='utf-8')
        logging.info(self.data_send)
        if kwargs is not None:
            for i in kwargs:
                for j in self.data:
                    # 如果传参key和发送内容key相同，则替换Excel表中的对应key的value
                    if i == j:
                        self.data[j] = kwargs[i]
            if "content_type" in kwargs:
                self.header['content-type'] = kwargs['content_type']
        if self.data == {}:
            res = self.get_actual_data()
            actual_res = res.content
            jsondata = json.loads(actual_res)
            print(type(actual_res))
        elif self.get_token() == '':  #strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
            rest = self.get_actual_data()
            actual_res = rest.content
            print(type(actual_res))
            jsondata = json.loads(actual_res)
            token = jsondata['data']['token']
            print("最新token：" + token)
            self.set_token(token)
        else:
            token = self.get_token()
            print(token)
            rest = self.get_actual_data(token)
            actual_res = rest.content
            jsondata = json.loads(actual_res)
            print(type(actual_res))
            print("\n当前token为：" + self.get_token())
        return jsondata

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

    def get_token(self):
        token = environment_module.EnvironmentModule().get_token()
        return token

    def set_token(self,token):
        environment_module.EnvironmentModule().set_token(token)
        print("token设置成功\n")

    def get_expect_data(self):
        logging.debug("=============Expect============" + self.expect_res)
        return self.expect_res.encode('utf-8')

    #发送请求并分析返回数据
    def get_actual_data(self,token=None):
        if token != '':
            token = json.dumps(token)
            self.data['token'] = token
        actual_res_handle = requests_module.GetResponse(self.url,self.method)
        if self.data != {}:
            self.data = json.dumps(self.data)
            actual_res = actual_res_handle.get_response(self.data,self.header)
        else:
            actual_res = actual_res_handle.get_response()
        # logging.debug(u"===============data==============") + json.dumps(self.data)
        logging.debug((u"===========实际返回的数据为：%s============") % actual_res)
        return actual_res