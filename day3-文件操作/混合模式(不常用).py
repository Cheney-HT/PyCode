# -*- coding: utf-8 -*-
"""
 -*- coding: utf-8 -*-
Time    : 2023/7/18 10:19
AuThor  : Administrator
File    : 混合模式(不常用).py
Project : PycharmCode
"""
"""
w+ 写读
r+ 读写 追加写
a+ 追加读 
"""
f=open("联系方式","r+",encoding="utf-8")
print(f.readline())
f.write("哈哈哈\n")