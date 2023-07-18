names1 = []
names2 = ["a", "b", "c", "d", "e"]
names3 = ["哈", "嘿", "喔"]
names1.append("1")  # 末尾追加元素
names1.insert(0, "0")  # 插入元素
names1.extend(names2)  # 合并
names1.insert(1, names3)  # 列表嵌套
delete = names1.pop()  # e 删除最后一个元素并返回元素的值
print("删除的数据：" + delete)
names3.clear()  # 清楚列表
names2[-1] = "字母"  # 修改最后一个值
item = "a" in names1  # 判断元素是否在列表
print(item)
index = names1.index("a")  # 查找a的索引
names1[index] = "aa.txt"
print(f"列表一：{names1}")
print(f"列表二：{names2}")
print(f"列表三：{names3}")
list1 = names1[4:]  # 切片从4切到末尾
list2 = names1[0::2]  # 跳着切 num1：num2：num3   num3步长
print(f"切片：{list1}")
print(f"步长切片：{list2}")
list3 = [5, 1, 3, 6, 8, 4, 5, 15, 15, 15, 64, 6, 4]
list3.sort()  # 排序
list3.reverse()  # 翻转
print(f"排序：{list3}")
for i in names1:  # 遍历
    print(i)
for i in enumerate(names1):  # enumerate打印索引
    print(i)
