"""

    特点: 元素不能修改,有索引,可以不同数据类型,元素可以重复
    定义: t1 = (1,2,3)
         t2 = (1,)

"""

t1 = (1, 2, 3, 3, 4, 5, 5, '6', 6)
t2 = (100)
t3 = (100,)
print(type(t1), type(t2), type(t3)) # <class 'tuple'> <class 'int'> <class 'tuple'>

# 元组[索引] 根据索引下标查找元素
print(t1[0]) # 1
print(t1[-1]) # 6

# index() 查找某个数据,如果存在,返回对应的下标,否则报错,语法和列表,字符串的index方法相同
print(t1.index('6')) # 7
print(t1.index(3)) # 2

# count() 统计某个数据在当前元组出现的次数
print(t1.count(6)) # 1
print(t1.count(3)) # 2

# len() 统计元组中数据的个数
print(len(t1)) # 9

# 遍历
for i in t1:
    print(i)

# 添加修改和删除元组数据丢会报错
# del t1[0] # TypeError: 'tuple' object doesn't support item deletion
# t1[0] = 100 # TypeError: 'tuple' object does not support item assignment
