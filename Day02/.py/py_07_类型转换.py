"""
使用场景: 在进行数学运算的时候使用.
语法:
   int(x) x为任意类型数据
   float(x)
   str(x)
"""

# method 1
age = input("请输入年龄")
#打印明年年龄
age = int(age)
age = age + 1
print("我明年的年龄是%d岁." % age)
print(f"我明年的年龄是{age}岁.")

# method 2
age = int(input("请输入年龄"))
age += 1
print("我明年的年龄是%d岁." % age)
print(f"我明年的年龄是{age}岁.")
