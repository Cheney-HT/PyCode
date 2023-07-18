# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 15:46
File    : 内置函数.py
Project : PycharmCode
"""
# abs 取绝对值
print(abs(-10))
# bool 判断是否为真 0和None是False  其余都是True
print(bool("我"))
list = [1, 2, 0, 3]
# all 所有为真返回True 一个不为真则返回False
print(all(list))
# any 任意一个为真 就返回True
print(any(list))
# chr 传入数字，打印ASCII码
print(chr(97))
# dict 生成字典
print(dict())
print(dict(name="hhh", age=22))
# dir 打印当前程序所有变量名
print(dir())
# locals 打印当前程序所有变量名&变量值
print(locals())
print(list)


# map
def cacl(x):
    return x ** 2


m = map(cacl, list)
for i in m:
    print(i)
# max 求最大值 min求最小 sum求和
print(max(list))
print(sum(list))

# ord 传入字符，打印ASCII值
print(ord("a"))
# enumerate 打印索引和值
for index, val in enumerate(list):
    print(index, val)
# ranound 保留小数
print(round(3.1415926, 3))
# str 转化为字符串
print(type(str(1)))
# zip 一一对应组合
x = ["aaa", "bbb", "ccc"]
y = [1, 2, 3, 4]
for i in zip(x, y):
    print(i)
# filter 把列表每个元素给函数运行，结果为真保留这个值
l = [1, 2, 3, 5, 6, 7, 9, 8]
print(l)


def num(x):
    if x > 5:
        return x


for i in filter(num, l):
    print(i)
