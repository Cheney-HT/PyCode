# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/19 17:01
File    : time模块.py
Project : PycharmCode
"""
import time

print(time.time())  # 时间戳
# start = time.time()  # 开始时间
# time.sleep(3)  # 睡眠，单位为s
# print(f"运行了count:{time.time() - start}秒")
print(time.localtime())  # 将一个时间戳转为时区元组
print(time.gmtime())  # 将一个时间戳转为UTC时区
print(time.mktime(time.localtime()))  # 将一个时间转为时间戳
print(time.strftime("%Y-%m-%d %X", time.localtime()))  # 将一个时间元组或struct_time转为格式化的字符串
