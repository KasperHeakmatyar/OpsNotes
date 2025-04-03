# 要求：打印如下图形：一个print只能打印一颗*
#
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
"""
分析:
1. 一行五颗星怎么打印: 使用循环五次 需要print()去掉换行功能
2. 五行数据怎么打印: 使用循环将分析1的代码作为循环体跑5此

"""

# l = 1
# while l <= 5:
#     h = 1
#     while h <= 5:
#         print("x", end=" ")
#         h += 1
#     print()
#     l += 1

#rewrite
i = 0
while i <= 5:
    d = 1
    while d <= 5:
        print("*", end="")
        d += 1
    print("")
    i += 1



#乘法口诀表
# l_0 = 1
# while l_0 <= 9:
#      h_0 = 1
#      while h_0 <= l_0:
#          print(f"{l_0} x {h_0} = {l_0 * h_0}  ", end=" ")
#          h_0 += 1
#      print()
#      l_0 += 1

for i in range(1,10):
    print()
    for j in range(1,i+1):
        print(f"{j}x{i}={j*i}")