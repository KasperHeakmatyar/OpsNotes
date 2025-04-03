my_list = ['C', 'java', 'python', 'shell', 'mysql']
print(type(my_list)) # <class 'list'> 列表
#while循环遍历
i = 0
print(len(my_list)) # 5 注意这个长度
while i < len(my_list):
    print(f"{i}", my_list[i])
    i += 1

print("*"*30)

#打印my_list中除了python以外的所有元素
for item in my_list:
    if item != 'python': # 如果元素不是python
        print(item) # 打印每一个元素

print("*"*30)

#打印my_list中除了第二个元素以外的所有元素
i = 0
while i < len(my_list):
    if i != 2:
        print(f"{i}", my_list[i])
    i += 1

print("*"*30)

# for遍历容器也可以带上索引

for i in range(len(my_list)):
    print(i,my_list[i])

print("*"*30)

# todo 扩展 枚举方式遍历容器---好处是既有索引又有元素
for index, item in enumerate(my_list):
    print(f"索引: {index}, 元素: {item}")