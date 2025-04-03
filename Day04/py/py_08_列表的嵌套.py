"""
    嵌套: 列表中的元素也是列表.
    场景: 一个学校有三个班级,一个班级有三个学生,请用一个列表保存所有学生,还要体现出不同班级
"""
school_names = []

class_1 = ['张三', '李四', '王五']
class_2 = ['tom', 'jerry', 'rose']
class_3 = ['关羽', '张飞', '赵云']

school_names.append(class_1)
school_names.append(class_2)
school_names.append(class_3)

print(school_names) # [['张三', '李四', '王五'], ['tom', 'jerry', 'rose'], ['关羽', '张飞', '赵云']]

# 需求1, 打印jerry

print(school_names[1][1])

# 需求2, 打印所有班级和班级的学生
x = 1
for i in school_names:
    print(f"第{x}班学生: ", end="")
    for j in i:
        print(f"{j} ", end="")
    print()
    x += 1