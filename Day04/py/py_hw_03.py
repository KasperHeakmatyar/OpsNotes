# 将下列两个列表合并，将合并后的列表去重，之后降序并输出
list1 = [11, 4, 45, 34, 51, 90]
list2 = [4, 16, 23, 51, 0]

list3 = []
for i in list1:
    list3.append(i)
for j in list2:
    list3.append(j)
print(list3)
list3 = list(set(list3))
list3.reverse()
print(list3)
