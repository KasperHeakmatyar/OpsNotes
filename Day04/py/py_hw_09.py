# 列表嵌套：有3个教室[[],[],[]]，
# 8名讲师['A','B','C','D','E','F','G','H']，
# 将8名讲师随机均匀分配到3个教室中.

import random

c_list = [[],[],[]]

t_list = ['A','B','C','D','E','F','G','H']

for l in range(0,len(t_list)):
    t_se = random.randrange(0, len(t_list))
    #print(t_se)

    i = l % 3
    #print(i)
    t_re = t_list.pop(t_se)
    print(f"{t_re}教师被选中")
    c_list[i].append(t_re)
print(c_list)

# import random
#
# c_list = [[], [], []]
# t_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#
# for _ in range(len(t_list)):  # 循环8次，处理所有讲师
#     t_se = random.randrange(0, len(t_list))  # 随机选择一个讲师的索引
#     i = _ % 3  # 使用循环计数器实现均匀分配到3个教室
#     t_re = t_list.pop(t_se)  # 从讲师列表中移除选中的讲师
#     c_list[i].append(t_re)  # 将讲师添加到对应的教室列表
#
# print(c_list)

