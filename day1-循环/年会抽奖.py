import random

staffs=[]
staffs1=[]
staffs2=[]
staffs3=[]
for i in range(300):
    staff=f"员工{i+1}"
    staffs.append(staff)
print(staffs)
print("第一次抽奖开始：三等将奖品零食大礼包-----------")
for j in range(30):
    staff3="".join(random.sample(staffs,1))
    staffs3.append(staff3)
    print(f"恭喜{staff3}获得三等奖")
    staffs.remove(staff3)
print(f"三等奖获得者：{staffs3}")
print("第二次抽奖开始：二等将奖品苹果手机-----------")
for k in range(6):
    staff2="".join(random.sample(staffs,1))
    staffs2.append(staff2)
    print(f"恭喜{staff2}获得三等奖")
    staffs.remove(staff2)
print(f"二等奖获得者：{staffs2}")
print("第三次抽奖开始：一等将奖品泰国三日游-----------")
for k in range(3):
    staff1="".join(random.sample(staffs,1))
    staffs1.append(staff1)
    print(f"恭喜{staff1}获得三等奖")
    staffs.remove(staff1)
print(f"一等奖获得者：{staffs1}")
print("所有获奖者名单公布：")
print(f"一等奖获得者：{staffs1}")
print(f"二等奖获得者：{staffs2}")
print(f"三等奖获得者：{staffs3}")
