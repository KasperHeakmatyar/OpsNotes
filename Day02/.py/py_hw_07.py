# #### 设计一个程序:
#
# - 键盘录入1-7七个数字，分别代表周一到周日，
# - 如果输入的数字是6或7，输出“周末”，否则输出“工作日”

num = int(input("输入一个数字: "))
if num < 1 or num > 7:
    print("请重试")
elif num == 6 or num == 7:
    print("周末")
else:
    print("工作日")

#循环版
"""
i = 0
while i < 5:
    num = int(input("输入一个数字: "))
    if num < 1 or num > 7:
        print("请重试")
    elif num == 6 or num == 7:
        print("周末")
    else:
        print("工作日")
        i += 1
"""

