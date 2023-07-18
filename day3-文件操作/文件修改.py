# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 10:26
File    : 文件修改.py
Project : PycharmCode
"""
f=open("联系方式","r+",encoding="utf-8")
#1. 将文件加载到内存
data=f.read()
new_data=data.replace("岳妮妮","倪妮")
#2. 清空文件
f.seek(0)
f.truncate() #截断文件，从0开始截，相当于清空
#3. 把新内容写回磁盘
f.write(new_data)
f.close()
