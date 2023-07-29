count = 0
num = 33
while count >= 0:
    count += 1
    guess = int(input("请输入你要猜测数字："))
    if guess == num:
        exit("恭喜你猜对了")
    else:
        print(f"第{count}次猜数，猜错了")
