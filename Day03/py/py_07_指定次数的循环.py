"""
注意:
range中的end是必须写的
for 变量 in range(start, end, step):
    循环体
解释:
start:开始位置,默认为0
end:结束位置,不包含结束位置
step:自增值,默认为1
"""
for i in range(5): #start默认是0, step(自增)默认是1, end是不包含在内的
    print(i)

#todo 打印5-10

for i in range(5, 11):
    print(i, end="")
print()

#todo 打印1-10之间的偶数
for i in range(2, 11, 2):
    print(i, end="")
