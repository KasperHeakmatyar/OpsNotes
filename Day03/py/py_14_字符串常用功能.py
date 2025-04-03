"""
find() : 查找子串第一次出现的位置,找到返回索引位置.找不到返回-1
index() : 查找子串第一次出现的位置,找到返回索引位置.找不到就会报错[报错下面的代码就不执行]
"""
s1 = "黑马程序员你我都是黑马888"
result = s1.find('黑马')
print(result) # 0 返回的是子串整体出现的位置

print(s1.find('黑马',5,-1)) # 9 返回值直接打印

print(s1.find("白马")) # -1 找不到返回-1

print("=" * 30)

print(s1.index("黑马")) # 0
# print(s1.index("白马")) # ValueError: substring not found

print("上面报错下面就不执行了")