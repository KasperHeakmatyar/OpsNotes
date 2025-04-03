"""
    set 是集合类型:
    特点:没有索引,元素不能重复,存取无序
    创建: set1={10,20} or set2=set()
"""
set1 = {1,2,3,3,3,4}
set2 = set()
print(set1, set2)
print(type(set1), type(set2))

#todo 注意事项: 不能使用{}创建集合
set3 = {}
print(type(set3))

#todo 常用功能:去除重复元素

list1 = [1,2,3,3,3,4,5,6]
#方式1.自己实现去重
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

#方式2.利用set去重
set4 = set(list1)
print(set4)
list3 = list(set4)
print(list3)

new_list = list(set(list1))
print(new_list) # [1, 2, 3, 4, 5, 6]