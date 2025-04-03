"""
无限循环又称死循环,一直运行,永不停止.
while 格式: while True:
"""
# while True:
#     print("hello")

# -- 如果代码写错了可能会出现死循环
"""
i=0
while i > 10:
    print("python", i)
    i += 1 #todo如果写 i-= 1不会死循环
"""
# todo 无限循环场景???不明确循环次数.....
# todo 键盘录入学生信息,然后打印到控制台,输入exit退出

while True:
    name = input("录入学生姓名: ")
    if name == "exit":
        print("系统已退出")
        #退出系统
        exit(0)
    print(f"今日报道同学{name},成功")