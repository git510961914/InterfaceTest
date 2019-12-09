#!user/bin/python3
#coding=utf-8

import pymysql
from common.module import environment_module

class Database:
    def __init__(self,env):
        self.env = env

    def connect(self):
        db = environment_module.EnvironmentModule().get_database(self.env)
        conn = pymysql.connect(host=db['host'],port=db['port'],user=db['username'],password=db['password'])
        cursor = conn.cursor()  #獲取操作游標
        return  cursor

    def insert(self,sql):
        cursor = self.connect()
        try:
            # 执行插入sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            cursor.commit()
        except:
            # 如果发生错误则回滚
            cursor.rollback()
        # 关闭数据库连接
        cursor.close()

    def delete(self,sql):
        cursor = self.connect()
        try:
            # 执行刪除sql语句
            cursor.execute(sql)
            # 提交修改
            cursor.commit()
        except:
            # 发生错误时回滚
            cursor.rollback()
        # 关闭连接
        cursor.close()

    def update(self,sql):
        cursor = self.connect()
        try:
            # 执行更新sql语句
            cursor.execute(sql)
            # 提交修改
            cursor.commit()
        except:
            # 发生错误时回滚
            cursor.rollback()
        # 关闭连接
        cursor.close()

    def query(self,sql):
        cursor = self.connect()
        try:
            # 执行查詢sql语句
            cursor.execute(sql)
            #fetchone():该方法获取下一个查询结果集。结果集是一个对象
            #fetchall():接收全部的返回结果行
            #rowcount():这是一个只读属性，并返回执行execute()方法后影响的行数
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")
        # 关闭数据库连接
        cursor.close()
