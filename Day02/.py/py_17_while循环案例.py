#需求:计算1~100的累加和(包含1和100)
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"1-100累加和是:{sum}")

# 需求：计算1~100之间偶数的累加和（包含1和100）
a = 1
sum_a = 0
while a <= 100:
    if a % 2 == 0:
        sum_a += a
    a += 1
print(sum_a)