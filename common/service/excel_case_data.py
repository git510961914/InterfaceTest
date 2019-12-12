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
        self.data = ''
        self.expect_res = ''
        #self.data = {}
        self.case_url = ''
        self.case_input = ''
        self.header = {"User-Agent":"callmec/3.6.0 (iPhone; iOS 13.1.2; Scale/2.00)","c-br":"iPhone 7","c-lng":"106.491219",\
                       "c-sv":"13.1.2","c-cv":"3.6.0","c-lat":"29.621786","c-ct":"2","c-ch":"667.000000","c-sr":"0","Accept-Language":"zh-Hans-CN;q=1",\
                       "c-iv":"3.6.0","c-cw":"375.000000","Accept":"*/*","Accept-Encoding":"gzip, deflate","c-nw":"4G",\
                       "c-im":"4A0E5A73-665E-495B-9E93-6BA72FFC7154","c-st":"1","Content-Type":"","token":""}

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
        case_data_list = excel_handle.row_values(sheet,row_id)
        # 获取第row_id行第2列的数据(路径)
        path = case_data_list[1]
        # 获取完整url
        self.url = self.get_url(path)
        print("完整URL：" + self.url)
        # ID、Path、Request、Input、Expect
        # 获取发送方式（Request）
        self.method = case_data_list[2]
        # 获取请求参数
        self.data = case_data_list[3]
        # 获取期望返回数据
        self.expect_res = case_data_list[4]
        print("期望数据：" + self.expect_res)
        # 字符串转字典
        if self.data != '':
            self.data = json.loads(self.data,encoding="utf-8")
        logging.info(self.data)
        if kwargs is not None:
            for i in kwargs:
                for j in self.data:
                    # 如果传参key和发送内容key相同，则替换Excel表中的对应key的value
                    if i == j:
                        self.data[j] = kwargs[i]
            if "content_type" in kwargs:
                self.header['Content-Type'] = kwargs['content_type']
        if self.data == '':
            token = self.get_token()
            self.header['token'] = token
            res1 = self.get_actual_data()
            actual_res = res1.content
            actual_res = json.loads(actual_res)
            if actual_res['success']:
                print("响应正确")
            else:
                print("响应不正确")
        elif self.get_token() == '':  #strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
            res2 = self.get_actual_data()
            actual_res = res2.content
            actual_res = json.loads(actual_res)
            if actual_res['success']:
                print("响应正确")
            else:
                print("响应不正确")
        else:
            token = self.get_token()
            self.header['token'] = token
            print("当前token为：" + self.header['token'])
            res3 = self.get_actual_data(token)
            actual_res = res3.content
            actual_res = json.loads(actual_res)
            if 'success' in actual_res.keys():
                if actual_res['success']:
                    print("响应正确")
                else:
                    print("响应不正确")
        return actual_res

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
        return environment_module.EnvironmentModule().get_env_url('Pre') + path

    def get_token(self):
        token = environment_module.EnvironmentModule().get_token()
        return token

    def set_token(self,token):
        environment_module.EnvironmentModule().set_token(token)
        print("token设置成功")

    def get_expect_data(self):
        logging.debug("=============Expect============" + self.expect_res)
        return self.expect_res.encode('utf-8')

    #发送请求并分析返回数据
    def get_actual_data(self,token=None):
        if token:
            self.data['token'] = token
        actual_res_handle = requests_module.GetResponse(self.url,self.method)
        if self.data != {}:
            #api.py中，get方法的params参数传字典，post方法的data参数传json字符串(以字典提交需要编码data=urllib.urlencode(data))
            if self.method == "get":
                actual_res = actual_res_handle.get_response(self.data,self.header)
            else:
                self.data = json.dumps(self.data)
                actual_res = actual_res_handle.get_response(self.data,self.header)
        else:
            actual_res = actual_res_handle.get_response(self.data,self.header)
        logging.debug((u"===========实际返回的数据为：%s============") % actual_res)
        return actual_res