# 2.练习对列表的增删改查统计的操作，具体操作如下：
# 1)声明一个列表，包含的数据有：["hello", "python", "itcast", "hello"]
# 2)在列表中追加一个数据："heima"
# 3)删除列表中的第二个数据
# 4)删除列表中的数据："heima"
# 5)将列表中的第二个数据改为："chuanzhi"
# 6)在控制台打印列表中的第一个元素
# 7)统计列表中"hello"字符串出现的次数
# 8)在控制台打印列表的长度
# 9)循环遍历列表中的所有数据

# 1
list1 = ["hello", "python", "itcast", "hello"]

print("=" * 40)
# 2
list1.append("heima")
print(list1)

print("=" * 40)
# 3
del_item = list1.pop(1)
print(del_item)  # pop会返回删除值
print(list1)

print("=" * 40)
# 4
list1.remove("heima")
print(list1)

print("=" * 40)
# 5
list1[1] = "chuanzhi"
print(list1)

print("=" * 40)
# 6
print(list1[0])

print("=" * 40)
# 7
print(list1.count("hello"))

print("=" * 40)
# 8
print(f"长度是:{len(list1)}")

print("=" * 40)
# 9

#method 1:
for i in range(len(list1)):
    print(i, list1[i])

#method 2:
i = 0
while i < len(list1):
    print(i, list1[i])
    i += 1
