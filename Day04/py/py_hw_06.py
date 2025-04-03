# 已知字典: stu_dict = {"name":"tom","age":19,"height":1.78}
# 要求:
# 	1.删除年龄
#     2.添加性别为男
#     3.修改身高为1.89
#     4.打印身高
#     5.遍历输出字典中所有的键和值.

stu_dict = {"name":"tom","age":19,"height":1.78}

# 1
del stu_dict["age"]
print(stu_dict)

# 2
stu_dict["sex"] = "male"
print(stu_dict)

# 3
stu_dict["height"] = 1.78
print(stu_dict)

# 4
height = stu_dict.get("height")
print(height)

# 5
for k in stu_dict.keys():
    print(f"{k} : {stu_dict[k]}")