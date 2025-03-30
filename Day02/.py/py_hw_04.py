# 用户输入年龄，如果年龄超过65岁，输出："可以退休了"， 否则，输出："小伙子，加油干！"

user_age = int(input("输入年龄: "))
if user_age < 0 or user_age > 100:
    print("输入有误")
elif user_age > 65:
    print("可以退休了")
else:
    print("小伙子,加油干!")
