# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 15:10
File    : 学生信息注册.py
Project : PycharmCode
"""


def stu_register(name, age, course="Py", country="CN"):
    print("-----注册学生信息-----")
    print("姓名:", name)
    print("年龄:", age)
    print("课程:", course)
    print("国家:", country)


stu_register("胡歌", 22, "python")
stu_register("松下手刹", 25, "python_网安", "JP")
stu_register("艾瑞莉娅", 21,"py","US")
