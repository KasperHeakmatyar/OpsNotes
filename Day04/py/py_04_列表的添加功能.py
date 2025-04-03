# append() 增加指定数据到列表中
# insert() 指定位置新增数据
# extend() 列表结尾追加数据,如果数据是一个序列,则这个序列的数据都逐一添加到列表

list1 = ['java', 'c', 'php']

# append() 增加指定数据到列表中
list1.append('js')
print(list1) # ['java', 'c', 'php', 'js']

# insert() 指定位置新增数据
list1.insert(0, 'python') #0代表字符位置,也就是插入的数据放哪里
print(list1) # ['python', 'java', 'c', 'php', 'js']

# extend() 列表结尾追加数据,如果数据是一个序列,则这个序列的数据都逐一添加到列表
list2=['c#', "mysql"]
list1.extend(list2)
print(list1) # ['python', 'java', 'c', 'php', 'js', 'c#', 'mysql']

list1.append(list2) # 直接添加容器也行,但是会容器嵌套,不方便取出元素
print(list1) # ['python', 'java', 'c', 'php', 'js', 'c#', 'mysql', ['c#', 'mysql']]