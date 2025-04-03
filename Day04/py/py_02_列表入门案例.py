"""
list 表示列表类型
容器名称 = [元素,元素,...]
"""
list1 = [100, 200, "hello", True, 3.14]
print(list1) # [100, 200, 'hello', True, 3.14]
print(type(list1)) # <class 'list'>

#基本使用--获取一个元素--使用索引
print(list1[0]) #100
# print(list1[5]) # IndexError: list index out of range

#基本使用--获取多个元素--使用切片
print(list1[2:]) # ['hello', True, 3.14]
