# -*- coding: utf-8 -*-
"""
 -*- coding: utf-8 -*-
Time    : 2023/7/18 9:29
AuThor  : Administrator
File    : 文本模式.py
Project : PycharmCode
"""
f=open("aa",mode="w")
f.write("123\n")
f.write("胡歌\n")
f.close()
f=open("aa",mode="r")
f.readline() #读一行
f.read() #读剩余的全部
f.close()
f=open("aa",mode="a")
f.write("周杰伦\n")  #文本末尾最佳
f.close()