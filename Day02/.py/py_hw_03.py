# #### 题干
#
# 定义变量，c1 = '可乐'，c2 = '牛奶'，通过Python代码
# 把c1内容调整为牛奶，c2调整为可乐。（提示：两个变量交换值）

c1 = "可乐"
c2 = "牛奶"
temp = ""

temp = c1
c1 = c2
c2 = temp

print(c1, c2)


c1 = "可乐"
c2 = "牛奶"

c1, c2 = c2, c1
print(f"c1为{c1},c2为{c2}")
