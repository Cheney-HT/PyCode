# -*- coding: utf-8 -*-
"""
 -*- coding: utf-8 -*-
Time    : 2023/7/18 10:11
AuThor  : Administrator
File    : 文件操作.py
Project : PycharmCode
"""
f=open("seek","w")
f.write("Hello1\n")
print("返回光标当前位置：",f.tell())
f.write("Hello2\n")
f.write("Hello3\n")
f.seek(6) #回到指定位置
print("返回光标当前位置：",f.tell()) #光标位置
f.write("---")

f.flush()#将文件强制从内存刷新到磁盘