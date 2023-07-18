# -*- coding: utf-8 -*-
"""
 -*- coding: utf-8 -*-
Time    : 2023/7/18 9:29
AuThor  : Administrator
File    : 文本模式.py
Project : PycharmCode
"""
"""
r 只读模式
w 创建模式 若文件存在则覆盖
a 追加模式，在文本末尾最佳数据
"""
f=open("aa.txt", "w", encoding="utf-8")
f.write("123\n")
f.write("胡歌\n")
f.close()
f=open("aa.txt", "r", encoding="utf-8")
f.readline()  # 读一行
f.read()  # 读剩余的全部
f.close()
f=open("aa.txt", "a", encoding="utf-8")
f.write("周杰伦\n")  # 文本末尾最佳
f.close()