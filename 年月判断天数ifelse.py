# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:37:25 2026

@author: 24159
"""

year = eval(input("输入年份："))
month = eval(input("输入月份："))
s = 4,6,9,11
n = 1,3,5,7,8,12
if 1 <= month <= 12:
    if month in s:
        days = 30
    elif month in n:
        days = 31
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days = 29
        else:
            days = 28
    print(f"{year}年{month}月有{days}天")
else:
    print("出错了")