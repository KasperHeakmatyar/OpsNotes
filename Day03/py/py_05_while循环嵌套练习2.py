# 要求：打印如下图形：
#
# *
# * *
# * * *
# * * * *
# * * * * *

i = 1
while i <= 5:
    d = 1
    while d <= i:
        d += 1
        print("*", end="")
    print()
    i +=1

