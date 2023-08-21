# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/8/16 17:47
File    : 关于字典.py
Project : PycharmCode
"""
dir = {
    "name": "周杰伦",
    "age": 33,
    "sex": "男"
}
print(dir)
print(dir["name"])
dir["huge"] = "胡歌"  # key 不存在，添加；存在，修改
print(dir)

# 字典循环遍历
for k in dir:
    print(k)
    print(dir[k])
print("-----------")
for k, v in dir.items():
    print(k)
    print(v)

print("------------")
zry = {
    "name": "张若昀",
    "age": 23,
    "wife": {
        "name": "唐艺昕",
        "age": 23,
        "hobby": ["美食", "逛街", "旅游"]
    },
    "hobby": ["游戏", "篮球", "演戏"],
    "children": [
        {"name": "孩子1", "age": 1},
        {"name": "孩子2", "age": 2},
        {"name": "孩子3", "age": 3},
    ]
}
# 打印zry老婆名字
print(zry["wife"]["name"])
# 打印zry老婆的第二个爱好
print(zry["wife"]["hobby"][1])
# 打印zry的第二个孩子的年龄
print(zry["children"][1]["age"])
# 打印zry的每个孩子的姓名
for i in zry["children"]:
    print(i["name"])

v1 = zry["马化腾"]  # 没有key直接报错
print(v1)
v2 = zry.get("马化腾")  # 没有key返回null,若有第二个参数，返回第二个参数
print(v2)
