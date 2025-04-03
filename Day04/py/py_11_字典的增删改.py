"""
增: 字典[键]=值
改:字典[键]=值
删:
    del 字典[键]
    字典.pop(键) 会返回删除值(可以用一个容器来接)
"""

dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 增
dict1['id'] = 100
print(dict1) # {'name': 'Tom', 'age': 20, 'gender': 'male', 'id': 100}

# 改 -- 修改的是值
dict1['age'] = 21
print(dict1) # {'name': 'Tom', 'age': 21, 'gender': 'male', 'id': 100}

# 删除
del_item = dict1.pop('id')
print(dict1)
print(del_item) # 100 返回键对应的值

# 删除不存在的key
# dict1.pop('class_name') # KeyError: 'class_name'
# del dict1['class_name'] #KeyError: 'class_name'
# todo 都会报错