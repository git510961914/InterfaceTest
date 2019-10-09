#!user/bin/python3
#coding=utf-8
import requests
import logging
import json
from requests.exceptions import *

class GetResponse:
    def __init__(self,url,method='get'):
        self.__url = url
        self.__method = method.lower()
        self.__resp = ''

    def get_response(self,data):
        if self.__method == 'get':
            try:
                print("开始get请求")
                __resp = requests.get(self.__url,data)
                print("状态码为：" + str(__resp.status_code))
                if __resp.status_code == 200:
                    print("请求成功")
                else:
                    print("请求失败")
            except (MissingSchema, InvalidURL):
                logging.error(u'请检查url：%s 是否正确' % self.__url)
            except ConnectionError:
                logging.error(u'网络连接失败或接口响应时间过长')
            else:
                return __resp

        if self.__method == 'post':
            try:
                print("开始post请求")
                __resp = requests.post(self.__url,None,data)
                print("状态码为：" + str(__resp.status_code))
                if __resp.status_code == 200:
                    print("请求成功")
                else:
                    print("请求失败")
            except (MissingSchema, InvalidURL):
                logging.error(u'请检查url：%s 是否正确' % self.__url)
            except ConnectionError:
                logging.error(u'网络连接失败或接口响应时间过长')
            else:
                return __resp

class AnalysisResponse(object):
    """
    解析response：response为一大段字符串，该类将这个大串字符串中有用的内容提取出来
    """
    def __init__(self, resp):
        self.__resp = resp

    @property
    def url(self):
        __url = self.__resp.url
        return __url

    @property
    def status_code(self):
        __status_code = self.__resp.status_code
        return __status_code

    @property
    def str_content(self):
        """
        返回string类型的content
        """
        __str_content = str(self.__resp.content)
        return __str_content

    @property
    def dic_content(self):
        """
        将response转换成字典后返回
        """
        __dic_content = json.loads(self.__resp.content)
        return __dic_content

    @property
    def headers(self):
        __headers = self.__resp.headers
        return __headers