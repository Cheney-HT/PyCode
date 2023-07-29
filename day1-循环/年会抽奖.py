import random

staffs = []  # 存储所有员工
staffs1 = []  # 存储一等奖员工
staffs2 = []  # 存储二等奖员工
staffs3 = []  # 存储三等奖员工
for i in range(300):
    staff = f"员工{i + 1}"
    staffs.append(staff)  # 将所有员工加入到员工列表
print(staffs)
print("第一次抽奖开始：三等将奖品零食大礼包-----------")
for j in range(30):
    staff3 = "".join(random.sample(staffs, 1))  # 从员工列表抽取一个员工
    staffs3.append(staff3)  # 将抽到的员工加入到三等奖员工列表
    print(f"恭喜{staff3}获得三等奖")
    staffs.remove(staff3)  # 把抽到奖的员工从员工表中删除
print(f"三等奖获得者：{staffs3}")
print("第二次抽奖开始：二等将奖品苹果手机-----------")
for k in range(6):
    staff2 = "".join(random.sample(staffs, 1))
    staffs2.append(staff2)
    print(f"恭喜{staff2}获得三等奖")
    staffs.remove(staff2)
print(f"二等奖获得者：{staffs2}")
print("第三次抽奖开始：一等将奖品泰国三日游-----------")
for k in range(3):
    staff1 = "".join(random.sample(staffs, 1))
    staffs1.append(staff1)
    print(f"恭喜{staff1}获得三等奖")
    staffs.remove(staff1)
print(f"一等奖获得者：{staffs1}")
print("所有获奖者名单公布：")
print(f"一等奖获得者：{staffs1}")
print(f"二等奖获得者：{staffs2}")
print(f"三等奖获得者：{staffs3}")
