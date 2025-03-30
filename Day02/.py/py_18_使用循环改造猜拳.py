import random

#改造为可以玩5次
i = 1
while i <= 5:
    player = int(input("请出拳(1石头,2剪刀,3布)"))

    computer = random.randint(1, 3)
    print(player, "vs", computer)

    # 对比双方数字

    if player > 3 or player < 1:
        print("输入有误")
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("玩家赢了")
    elif (player == 2 and computer == 1) or (player == 3 and computer == 2) or (player == 1 and computer == 3):
        print("电脑赢了")
    else:
        print("平局")
    i +=1