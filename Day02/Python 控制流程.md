## if 单分支
    if 条件:
         满足条件要执行的代码:
```
#:从键盘获取自己的年龄,判断是否大于或等于18岁,满足就输出"已成年,可以去网吧"
#1. 使用input从键盘中获取数据,并且存入到一个变量中,并且使用类型转换,因为input接受的数据都是字符串.
age = int(input("请键入年龄: "))

#2. 使用if语句
if age >= 18:
    print("已成年,可以去网吧")
    print("if语句体可以有多行")
print("---这里不属于if---")
```
---

## if双分支
    if 条件:
        满足条件的代码
    else:
        不满足条件的代码
```
#动物园对150以上游客进行门票收费,请写个程序判断

height = int(input("录入身高")) #对input进行类型转换
#判断身高和150的关系
if height > 150:
    print(f"你的身高是{height},请买票进入")
else:
    print(f"你的身高是{height},直接进入")
print("---程序结束---")
```
---

## if多分支
    if 条件1:
        执行条件1代码
    elif 条件2:
        执行条件2代码
    elif 条件3:
        执行条件3代码
    ... ...
    else:
        以上所有条件都不满足,执行本行...

```
# 案例: 从键盘录入分数输出对应的级别. 90+优秀 80+良好 70+中等 60+及格 其他不及格

score = int(input("请输入分数"))
if score > 100 or score < 0:
    print("成绩录入有误")
elif score <= 100:
    print("成绩优秀")
elif score <= 90:
    print("成绩良好")
elif score <= 80
    print("成绩中等")
elif score <= 70
    print("成绩合格")
else:
    print("不及格")
print("判断完毕")
```
---

## if练习题
```
#1.键盘录入一个月份(1-12),输出对应的季节.
# 春季：3月、4月、5月
# 夏季：6月、7月、8月
# 秋季：9月、10月、11月
# 冬季：12月、1月、2月

month = int(input("请输入月份: "))
if month < 1 or month > 12:
    print("输入有误")
elif month == 12 or month < 3:
    print("冬季")
elif month < 6:
    print("春季")
elif month < 9:
    print("夏季")
else:
    print("秋季")
print("---程序结束---")

eg version:
month = int(input('录入一个月份'))
if month == 3 or month == 4 or month == 5:
    print("春季")
elif month == 6 or month == 7 or month == 8:
    print("夏季")
elif month == 9 or month == 10 or month == 11:
    print("秋天")
elif month == 12 or month == 1 or month == 2:
    print("冬天")
else:
    print('月份录入无效...')

#2. 键盘录入两个数字a和b,输出两个数字的差,必须确保大的数值减去小的数值.
a = int(input("输入a值: "))
b = int(input("输入b值: "))
if a < b:
    print(b - a)
elif a > b:
    print(a - b)
else:
    print(a - b)

eg version:
a = int(input('录入一个数'))
b = int(input('录入一个数'))
if a > b :
    print(f'a和b的差是:{a-b}')
else :
    print(f'a和b的差是:{b-a}')
```
[[Python 101 基本语法 Part 2 | F格式化输出]]

---
## if嵌套

```
# 情节描述：上公交车，并且可以有座位坐下
# 要求：输入公交卡当前的余额，只要超过2元，就可以上公交车；如果车上有空座位，就可以坐下。
card_balance = int(input("输入余额: "))
    if card_balance > 2:
        print("欢迎乘坐公交车")
        seat_ava = int(input("输入空座数量: "))
        if seat_ava > 0:
            print("可以坐着")
        else:
            print("站着")
    else:
        print("请充值")
print("程序结束")

eg version:
card_money = int(input('录入公交卡余额'))
free_sit_num = int(input("录入座位数量"))

if card_money >= 2:
    print("欢迎乘坐公交车...")
    if free_sit_num > 0:
        print("坐下开始刷视频...")
    else:
        print("站好扶稳...")
else:
    print("余额不足,请充卡...")

```
---

## if综合案例

```
# 1.   设置两个玩家 player computer
# 2.   player: 从控制台输⼊要出的拳 ⽯头(1)／剪⼑(2)／布(3)
# 3.   computer: 电脑 随机 出拳
# 4.   player和computer⽐较胜负

import random #导入随机数模块

# python中的随机数产生
# randint([开始,结束])函数: 返回开始和结束之间的随机数字.
# import random
# print(random.randint(1,5))

import random  
  
computer = random.randint(1, 3)  
player = int(input("1石头, 2剪刀, 3布"))  
print(f"{player} vs {computer}")  
if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):  
    print("玩家输了,电脑获胜")  
elif (computer == 1 and player == 3) or (computer == 2 and player == 1) or (computer == 3 and player == 2):  
    print("玩家赢了,电脑输了")  
else:  
    print("平局")

#eg version:
import random
#1.玩家出拳
player = int(input("请玩家出拳(1石头,2剪刀,3布)"))
#2.电脑出拳
computer = random.randint(1,3)
print(player,"VS",computer)

#3.对比双方的拳数字.
if (player==1 and computer==2) or (player==2 and computer==3) or (player==3 and computer==1):
    print("玩家胜利...电脑弱爆了...")
elif (player==2 and computer==1) or (player==3 and computer==2) or (player==1 and computer==3):
    print("电脑胜利...玩家太菜了...")
elif player == computer:
    print("平局...决战到天亮....")

print("---游戏结束---")

```
---

## 断点调试功能

1.打断点

![[Typora_vEa9GyaqhI.png]]

2.断点运行

![[Pasted image 20250330101827.png]]


3.分步执行代码 点击按钮或者 按下F8

![[Pasted image 20250330101852.png]]

4.代码区蓝色的代码表示将要运行但并未执行的代码.



5.如果有输出打印内容.需要切换tab栏.

![[Pasted image 20250330102043.png]]

---
## while循环

```
# 需求：循环打印5次 ”老婆我错误了 ”"""  
循环变量  
while 条件:  
    条件满足执行的循环内容  
    条件满足执行的循环内容  
    ....    改变循环变量(控制语句)!!!  
"""  
  
i = 0  
while i < 5:  
    print("老婆我错了")  
    i += 1
print("循环结束")

```

#### 循环四要素:

1. 循环初始值(循环变量)
2. 循环条件(满足条件就执行循环体.不满足就结束循环)
3. 循环体(满足循环条件要执行的代码)
4. 控制语句(控制循环变量的值)

---

## while循环案例

```
# 需求：计算1~100的累加和（包含1和100）
a=1
sum = 0
while a <= 100:
    sum += a
    a += 1
print(f"1~100之间的累加和是{sum}")


# 需求：计算1~100之间偶数的累加和（包含1和100）
b=1
sum = 0
while b <= 100:
    if b % 2 == 0:
        sum += b
    b += 1
print(F"1~100之间偶数的累加和是:{sum}")
```

## 循环版本的剪刀石头布

```
import random  
i = 0  
while i < 5:  
    player = int(input("请出拳(1石头,2剪刀,3布)"))  
    computer = random.randint(1, 3)  
    print(player, "vs", computer)  
    if player > 3 or player < 1:  
        print("输入有误")  
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):  
        print("玩家赢了")  
    elif (player == 2 and computer == 1) or (player == 3 and computer == 2) or (player == 1 and computer == 3):  
        print("电脑赢了")  
    else:  
        print("平局")  
    i += 1

eg version:
import random

# 改造为可以玩5次
i = 1
while i <= 5:
    # 1.玩家出拳
    player = int(input("请玩家出拳(1石头,2剪刀,3布)"))
    # 2.电脑出拳
    computer = random.randint(1, 3)
    print(player, "VS", computer)

    # 3.对比双方的拳数字.
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("玩家胜利...电脑弱爆了...")
    elif (player == 2 and computer == 1) or (player == 3 and computer == 2) or (player == 1 and computer == 3):
        print("电脑胜利...玩家太菜了...")
    elif player == computer:
        print("平局...决战到天亮....")

    i += 1
```