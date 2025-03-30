# 用户输入年龄，按照如下标准书写程序，判断用户处于哪个年龄阶段，并提示：您的年龄是xx: 青少年/青年/中年/老年。
#
# 年龄段划分标准：0-17岁为青少年；18-35岁为青年；36-59为中年，60-99岁为老年。

user_age = int(input("请输入年龄: "))
if user_age < 0 or user_age > 100:
    print("输入有误")
elif user_age <= 17:
    print(f"您的年龄是{user_age},青少年.")
elif user_age <= 35:
    print(f"您的年龄是{user_age},青年.")
elif user_age <= 59:
    print(f"您的年龄是{user_age},中年.")
else:
    print("您的年龄是%d,老年." % user_age)