# 已有列表name_list1 = ['张三','李四','王五','赵六'] 和列表 name_list2=['张三','李四']
# 求出两个列表中不一样的元素.然后存放在新列表中并打印新列表内容.
# 提示可以使用 in 和 not in 来判断元素是否在另一个容器中.

name_list1 = ['张三', '李四', '王五', '赵六']
name_list2 = ['张三', '李四']

new_list = []
for i in name_list1:
    if i not in name_list2:
        new_list.append(i)
print(new_list)
