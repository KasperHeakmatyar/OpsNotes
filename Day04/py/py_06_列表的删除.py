# del 列表[索引] 删除列表中的某个元素
# pop() 删除指定下标的数据(默认为最后一个),并返回该数据
# remove() 移除列表中某个数据的第一个匹配项
# clear() 清空列表,删除列表中的所有元素,返回空列表

my_list = ["C", "java", "python", "shell", "mysql"]

#需求1 删除第一个位置的元素
#del my_list[0]
del_item = my_list.pop(0)
print(f"{del_item}被删除了,现在是: {my_list}")

#需求2 删除python语言
my_list.remove("python")

#需求3 清空列表
# my_list.clear()

#todo 注意使用 del 可以删除列表在内存中的地址(删掉整个容器)
# del my_list

# print(my_list) # NameError: name 'my_list' is not defined
