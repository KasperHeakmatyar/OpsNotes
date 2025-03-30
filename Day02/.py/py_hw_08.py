# #### 设计一个程序:
#
# - 1-7七个数字，分别代表周一到周日，
# - 如果输入的数字是1，输出“今天是周一”
# - 如果输入的数字是2，输出“今天是周二”
# - 如果输入的数字是3，输出“今天是周三”
# - 如果输入的数字是4，输出“今天是周四”
# - 如果输入的数字是5，输出“今天是周五”
# - 如果输入的数字是6或7，输出“今天是周末”

num = int(input("输入一个数字: "))
if num == 1:
    print("今天是周一")
elif num == 2:
    print("今天是周二")
elif num == 3:
    print("今天是周三")
elif num == 4:
    print("今天是周四")
elif num == 5:
    print("今天是周五")
elif num == 6 or num == 7:
    print("今天是周末")
else:
    print("输入有误")

#循环版
i = 0
while i < 3:
    num = int(input("输入一个数字: "))
    if num == 1:
        print("今天是周一")
    elif num == 2:
        print("今天是周二")
    elif num == 3:
        print("今天是周三")
    elif num == 4:
        print("今天是周四")
    elif num == 5:
        print("今天是周五")
    elif num == 6 or num == 7:
        print("今天是周末")
    else:
        print("输入有误")
    i += 1