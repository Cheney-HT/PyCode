import random
import string

s=string.ascii_letters
count=0
while count<3:
    for i in range(20):
        car_num=[] #存储车牌号
        sum1=random.choice(string.ascii_uppercase)
        sum2="".join(random.sample(s,5))
        print(f"车牌号：京{sum}.{sum2}")
        car_num.append(f"车牌号：京{sum}.{sum2}")
        u_input=input("请输入你喜欢的车牌号：")
        if

