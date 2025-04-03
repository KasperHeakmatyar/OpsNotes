# index() 指定数据所在位置的下标
# count() 统计指定数据在当前列表中出现的次数
# in 判断指定数据在某个列表序列,如果在返回True,否则返回False
# not in 判断数据不在某个列表序列,如果不在返回True,否则返回False

my_list = ["aaa", 'bbb', 'ccc', 'bbb']
# index() 指定数据所在位置的下标
print(my_list.index('aaa', 0, 3)) # 0 index("查找值", 起始位置, 结束位置(不包含结束位置))
print(my_list.index("ccc", 2))
print(my_list.index("ccc", 0, 5))

# print(my_list.index('MMM')) # ValueError: 'MMM' is not in list 不存在直接报错

# count() 统计指定数据在当前列表中出现的次数
print(my_list.count('bbb'))

# 语法: 元素 in 容器 判断指定数据在某个列表序列,如果在返回True,否则返回False
# 语法: 元素 not in 容器 判断指定数据不在某个列表序列,如果不在返回True,否则返回False
print("aaa" in my_list) # True
print("ddd" in my_list) # False
print("ddd" not in my_list) # True


#案例:根据录入的名字,判断是否在列表中已存在
name_list = ['Tom', 'Lily', 'Rose']

name = input('请输入您要搜索的名字：')

if name in name_list:
    print(f'您输入的名字是{name}, 名字已经存在')
else:
    print(f'您输入的名字是{name}, 名字不存在')
