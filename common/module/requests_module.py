#!user/bin/python3
#coding=utf-8
import requests
import logging
from requests.exceptions import *

class GetResponse:
    def __init__(self,url,method='get'):
        self.__url = url
        self.__method = method.lower()
        self.__resp = ''

    def get_response(self,data=None,header=None):
        if self.__method == 'get':
            try:
                print("开始get请求")
                self.__resp = requests.get(self.__url,data,headers=header)
                print("状态码为：" + str(self.__resp.status_code))
                if self.__resp.status_code == 200:
                    print("请求成功")
                else:
                    print("请求失败")
            except (MissingSchema, InvalidURL):
                logging.error(u'请检查url：%s 是否正确' % self.__url)
            except ConnectionError:
                logging.error(u'网络连接失败或接口响应时间过长')
            else:
                return self.__resp

        if self.__method == 'post':
            try:
                print("开始post请求")
                self.__resp = requests.post(self.__url,data,headers=header)
                print("状态码为：" + str(self.__resp.status_code))
                if self.__resp.status_code == 200:
                    print("请求成功")
                else:
                    print("请求失败")
            except (MissingSchema, InvalidURL):
                logging.error(u'请检查url：%s 是否正确' % self.__url)
            except ConnectionError:
                logging.error(u'网络连接失败或接口响应时间过长')
            else:
                return self.__resp
