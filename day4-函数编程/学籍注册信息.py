# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 16:20
File    : 学籍注册信息.py
Project : PycharmCode
"""
db_file = "stu_info.txt"


def stu_info():
    """
    学生信息录入
    :return: stu_data 学生数据
    """
    stu_data = {}
    print("请完成信息注册".center(50, "-"))
    name = input("请输入姓名:").strip()
    age = input("请输入年龄:").strip()
    while True:
        phone = input("请输入您的电话:").strip()
        if phone in phone_list:
            print("手机号已存在，请重新输入")
        else:
            break
    while True:
        ID = input("请输入身份证号:").strip()
        if ID in id_list:
            print("身份证已存在，请重新输入")
        else:
            break

    course_list = ["Python开发", "网络安全", "Linux云计算", "Java开发", "运维开发"]

    for index, course in enumerate(course_list):
        print(f"{index + 1}. {course}")

    while True:
        selected_course = input("选择的课程是：")
        if selected_course.isdigit():
            selected_course = int(selected_course)
            if selected_course > 0 and selected_course <= len(course_list):
                course = course_list[selected_course - 1]
                print(f"您选择了'{course}'课程")
                break
            else:
                print("非法输入。。。，请输入正确的编号")
        else:
            print("非法输入。。。,请重新输入课程编号")

    stu_data["name"] = name
    stu_data["age"] = age
    stu_data["phone"] = phone
    stu_data["ID"] = ID
    stu_data["course"] = course
    return stu_data


def save_file(filename, stu_data):
    """
    将学生信息保存到文件内
    :param filename: 文件名
    :param stu_data: 学生数据
    :return:
    """
    f = open(filename, "a")
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['ID']},{stu_data['course']}\n"
    f.write(row)
    f.close()


def validate(filename):
    f = open(filename)
    phone_list = []
    id_list = []
    for line in f:
        line = line.split(",")
        phone = line[2]
        id = line[3]
        phone_list.append(phone)
        id_list.append(id)
    return phone_list, id_list


phone_list, id_list = validate(db_file)
student_data = stu_info()
# 将信息存入文件stu_info.txt
save_file(db_file, student_data)
print(student_data)
