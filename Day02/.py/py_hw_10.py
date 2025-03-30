# 1. 书写代码求 `0-100之间所有奇数的累加和`
# 2. 计算1000以内所有不能被7整除的整数之和

# 1.
i = 0
sum_1 = 1
while i <= 100:
    sum_1 += 2
    i += 1
print(sum_1)

# 2.
a = 0
sum_2 = 0
while a <= 1000:
    if a % 7 != 0:
        sum_2 += a
    a += 1
print(sum_2)

a = 1  # 从1开始
sum_2 = 0
while a <= 999:  # 只考虑1到999之间的数
    if a % 7 != 0:
        sum_2 += a
    a += 1
print(sum_2)
