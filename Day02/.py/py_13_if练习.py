#i. 键盘录入一个月份(1-12),输出对应季节
month = int(input("请输入月份"))
if month < 1 or month > 12:
    print("录入有误")
elif month == 12 or month < 3:
    print("冬季")
elif month < 6:
    print("春季")
elif month < 9:
    print("夏季")
else:
    print("秋季")
print("季节判断程序结束")

#ii. 键盘录入a,b,输出它们的差,必须确保大减小
a = int(input("请输入a: "))
b = int(input("请输入b: "))
if a > b:
    print(a - b)
elif b > a:
    print(b - a)
elif a == b:
    print(a - b)
print("计算结束")
