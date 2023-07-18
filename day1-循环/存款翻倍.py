# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 14:49
File    : 存款翻倍.py
Project : PycharmCode
"""

base = 10000  # 本金
interest = 0.0325  # 利率
year = 0  # 年
while base < 20000:  # 当本金小于20000时，一直循环
    base = round(base * (1 + 0.0325), 2)  # 保留两位小数
    year += 1
    print(f"第{year}年，本金：{base}")

# 四舍五入保留小数方法
num = 3.145
print("方法一：" + "%.2f" % num)
print(f"round方法：{round(num, 2)}" )
print("方法三：" + "{:.2f}".format(num))
