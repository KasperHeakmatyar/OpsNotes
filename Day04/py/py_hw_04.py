# 已有列表nums = [10, 20, 30, 40, 50], 将每一个数字在原来的基础上加10再存储nums中，打印列表nums.

nums = [10, 20, 30, 40, 50]
temp = []
for i in nums:
    temp.append(i + 10)
nums = temp
print(nums)
