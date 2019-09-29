#!user/bin/python3
#coding=utf-8
import xlrd

class ReadExcel:
    def __init__(self, file_name):
        self.data = xlrd.open_workbook(file_name)

    def close(self):
        self.data.close()

    def sheet_by_index(self, index):
        """
        通过表的索引获取表格的内容
        :param index: sheet的索引
        :return: 返回sheet的内容
        """
        __sheet = self.data.sheet_by_index(index)
        return __sheet

    def sheet_by_name(self, name):
        """
        通过sheet名称获取表的内容
        :param name: sheet名称
        :return: 返回sheet对象
        """
        __sheet = self.data.sheet_by_name(name)
        return __sheet

    def row_values(self, sheet_obj, row_index):
        """
        获取指定行的内容
        :param sheet_obj: 接收sheet对象
        :param row_index: 行的索引
        :return: 返回指定行的内容，类型为列表
        """
        __values_list = sheet_obj.row_values(row_index)
        return __values_list

    def col_values(self, sheet_obj, col_index):
        """
        获取指定列的内容
        :param sheet_obj: 接收sheet对象
        :param col_index: 列的索引
        :return: 返回指定列的内容，类型为列表
        """
        __values_list = sheet_obj.col_values(col_index)
        return __values_list

    def number_of_rows(self, sheet_obj):
        """
        获取指定sheet行数
        :param sheet_obj: 接收sheet对象
        :return: 返回sheet总行数
        """
        __number_of_rows = sheet_obj.nrows
        return __number_of_rows

    def number_of_cols(self, sheet_obj):
        """
        获取指定sheet列数
        :param sheet_obj: 接收sheet对象
        :return: 返回sheet总列数
        """
        __number_of_cols = sheet_obj.ncols
        return __number_of_cols

    def cell_value(self, sheet_obj, row_index, col_index):
        """
        获取指定单元格的内容
        :param sheet_obj: 接收sheet对象
        :param row_index: 行索引
        :param col_index: 列索引
        :return: 返回单元格的内容
        """
        __cell_value = sheet_obj.cell(row_index, col_index).value
        return __cell_value

    def all_content(self, sheet_obj):
        """
        获取工作表的所有内容
        :param sheet_obj:
        :return:
        """
        __content = []
        # 总行数
        __rows_num = self.number_of_rows(sheet_obj)
        for tmp in range(__rows_num):
            tmp_list = []
            # 遍历行内容
            __row_value = self.row_values(sheet_obj, tmp)
            for i in __row_value:
                i = i.encode('utf8')
                # 将每行内容放到一个列表里
                tmp_list.append(i)
            __content.append(tmp_list)
        return __content
