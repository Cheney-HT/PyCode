# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/19 16:49
File    : OS模块.py
Project : PycharmCode
"""
import os

print(os.getcwd())  # 获取脚本的当前目录
print(os.listdir())  # 遍历当前目录下的所有文件
os.remove("test.py")  # 删除一个文件
# os.mkdir("test")
os.removedirs("test")  # 删除一个目录
os.path.isdir("test")  # 判断是否是一个目录
os.path.isfile("test.py")  # 判断是否是一个文件
os.path.exists("D:\DevelopTools\PycharmCode\day5-模块编程")  # 检测路径是否存在
os.path.abspath("test.py")  # 获取绝对路径
# os.remove(new, old)  # 重命名
