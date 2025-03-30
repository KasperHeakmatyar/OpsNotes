# 要求：从键盘输入身高，如果身高没有超过150cm，则进动物园不用买票，否则需要买票。
"""
if 条件:
    满足条件的代码
else:
    不满足条件的代码
"""

height = int(input("请输入身高"))
if height > 150:
    print(f"您的身高为{height},请买票入园.")
else:
    print(f"您的身高为{height},无需买票.")
print("------程序结束------")