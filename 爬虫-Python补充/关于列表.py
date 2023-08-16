# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/8/15 11:34
File    : 关于列表.py
Project : PycharmCode
"""
list = ["王五", "哈哈哈", "张无忌", "呵呵呵"]
print(list[2][1])
print(list[1:3])  # 切片
list.append("赵敏")
print(list)
list[1] = "张三丰"  # 修改
list.insert(1, "赵本山")  # 插入
print(list)

# range
for i in range(10):  # 从开始数到10，顾头不顾尾
    print(i)
print("-------------")
for item in range(1, 10):
    print(item)
for item in list:
    print(item)

print(dir(""))
list1 = ["cht", "cy", "huge"]
# 列表所有元素首字母大写
for i in range(len(list1)):
    s = list1[i].capitalize()  # 把一句话的首字母大写，但是列表的数据不变
    list1[i] = s  # 修改
print(list1)
# for item in lst:  循环列表
# for i in range(len(lst)):     循环索引
