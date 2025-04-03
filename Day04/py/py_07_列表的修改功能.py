# 列表[索引] = 修改后的值  修改列表中的某个元素
# reverse() 将数据序列进行倒序排列
# sort() 对列表序列进行排序

list1 = ["aaa", "bbb", "ddd", "ccc"]

"""
#正序排序
list1.sort()
print(list1) # ['aaa', 'bbb', 'ccc', 'ddd']
 
#倒叙排序
list1.reverse()
print(list1) # ['ddd', 'ccc', 'bbb', 'aaa']
"""
#需求:颠倒数据的排序
list1.reverse()
print(list1) # ['ccc', 'ddd', 'bbb', 'aaa']

#需求: 把bbb改成fff
list1[2] = "fff"
print(list1) # ['ccc', 'ddd', 'fff', 'aaa']