for i in range(1,6):
    print(f"-------{i}层---------")
    if i == 3:
        print("不走第三层")
        continue  # 跳过本次循环，进入下一次
    for j in range(1,9):
        if i==4 and j==4:
            print("遇到404鬼屋，快跑")
            break #结束本次循环
        print(f"L{i}层-{i}0{j}室")