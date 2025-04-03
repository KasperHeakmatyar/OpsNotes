# 有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表

# method 1

list1 = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
new_list = []
for i in list1:
    if i[-1] == "e" or i[-1] == "s":
        new_list.append(i)
print(new_list)

# method 2
new_list = []
for i in list1:
    if i.endswith("e") or i.endswith("s"):
        new_list.append(i)
print(new_list)