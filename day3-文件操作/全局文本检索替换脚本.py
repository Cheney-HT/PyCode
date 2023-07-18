# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 10:45
File    : 全局文本检索替换脚本.py
Project : PycharmCode
"""
import sys

old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]
f = open(filename, "r+", encoding="utf-8")
# read to RAM
data = f.read()
# count and replayce
old_str_count = data.count(old_str)
new_data = data.replace(old_str, new_str)
# clear
f.seek(0)
f.truncate()
# save new data into file
f.write(new_data)
print(f"成功修改字符'{old_str}' to '{new_str}',共修改了{old_str_count}处")
# 命令行Terminal 执行脚本
# cd 文件夹路径 例：cd D:\DevelopTools\PycharmCode\day3-文件操作
# python 脚本文件名 参数一 参数二 参数三
