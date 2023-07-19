# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 17:35
File    : 自定义模块.py
Project : PycharmCode
"""
import os.path
import sys
import my_mod

print(__file__)  # 打印当前文件路径
print(os.path.dirname(__file__))  # dirname只保留目录名，不保存文件名
print(os.path.dirname(os.path.dirname(__file__)))
basepath = os.path.dirname(os.path.dirname(__file__))
sys.path.append(basepath)  # 添加模块查找路径

print(sys.path)  # 模块查找路径
