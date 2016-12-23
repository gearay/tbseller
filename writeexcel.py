#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-23 15:05:38
# @Author  : Yan Chen (cheny.gary@gmail.com)
# @Link    : ${link}
# @Version : $Id$
import xlsxwriter as wx


def writeexcel(path, dealcontent):
    workbook = wx.Workbook(path)
    top = workbook.add_format({'border': 1, 'align': 'center',
                               'bg_color': 'white', 'font_size': 11, 'font_name': '微软雅黑'})
    red = workbook.add_format({'font_color': 'white', 'border': 1, 'align': 'center',
                               'bg_color': '800000', 'font_size': 11, 'font_name': '微软雅黑', 'bold': True})
    image = workbook.add_format(
        {'border': 1, 'align': 'center', 'bg_color': 'white', 'font_size': 11, 'font_name': '微软雅黑'})
    formatt = top
    formatt.set_align('vcenter')  # 设置单元格垂直对齐
    worksheet = workbook.add_worksheet()  # 创建一个工作表对象
    width = len(dealcontent[0])
    worksheet.set_column(0, width, 38.5)  # 设定列的宽度为22像素
    for i in range(0, len(dealcontent)):
        if i == 0:
            formatt = red
        else:
            formatt = top
        for j in range(0, len(dealcontent[i])):
            if i != 0 and j == len(dealcontent[i]) - 1:
                if dealcontent[i][j] == '':
                    worksheet.write(i, j, ' ', formatt)
                else:
                    try:
                        worksheet.insert_image(i, j, dealcontent[i][j])
                    except:
                        worksheet.write(i, j, ' ', formatt)
            else:
                if dealcontent[i][j]:
                    worksheet.write(i, j, dealcontent[i][
                                    j].replace(' ', ''), formatt)
                else:
                    worksheet.write(i, j, '无', formatt)
    workbook.close()
