import random
import string

s=string.ascii_uppercase+string.digits
count=0
while count<3:
    car_nums=[] #存储车牌号
    for i in range(20):
        sum1=random.choice(string.ascii_uppercase)
        sum2="".join(random.sample(s,5))
        car_num=f"京{sum1}.{sum2}"
        car_nums.append(car_num)
        print(i+1,car_num) #加编号
    u_input=input("请输入你喜欢的车牌号：").strip()
    if u_input in car_nums:
        print(f"恭喜您选择了【{u_input}】车牌号")
        exit("Good luck")
    else:
        print("不合法的选择。。。")
    count+=1


