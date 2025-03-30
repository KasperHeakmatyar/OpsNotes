# 1.   设置两个玩家 player computer
# 2.   player: 从控制台输⼊要出的拳 ⽯头(1)／剪⼑(2)／布(3)
# 3.   computer: 电脑 随机 出拳
# 4.   player和computer⽐较胜负

#python中的随机数产生
# randint([开始,结束])函数:返回开始和结束之间的随机数字

#1.玩家出拳
player = int(input("请出拳(1石头,2剪刀,3布)"))
#电脑出拳
import random
computer = random.randint(1,3)
print(player, "vs" ,computer)

#对比双方数字

if player > 3 or player < 1:
    print("输入有误")
elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("玩家赢了")
elif (player == 2 and computer == 1) or (player == 3 and computer == 2) or (player == 1 and computer == 3):
    print("电脑赢了")
else:
    print("平局")