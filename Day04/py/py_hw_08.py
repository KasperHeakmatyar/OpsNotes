# 幸运数字6：
# 输入任意数字，如数字8，生成nums列表，元素值为1~8，
# 从中选取幸运数字(能够被6整除)移动到新列表lucky，
# 打印nums与lucky。
import random
while True:
    nums = []
    lucky = []
    num_input = int(input("Enter a number: (0 to quit)"))
    if num_input == 0:
        break
    else:
        r = random.randint(1, num_input + 1)
        for i in range(1, num_input + 1):
            nums.append(i)
        print(f"你抽到了数字{r},抱歉不是幸运数字. nums类型是{type(nums)}")
        print(nums)

        if r % 6 == 0:
            for r in range(1, r + 1):
                lucky.append(r)
            print(f"恭喜你,抽到幸运数字{r}, lucky类型是{type(lucky)}")
            print(lucky)
