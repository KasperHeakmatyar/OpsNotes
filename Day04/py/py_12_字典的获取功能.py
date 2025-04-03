# get(key, 默认值) 根据字典的key获取对应的value值，如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回None
# keys() 以列表返回一个字典所有的键
# values() 以列表返回字典中的所有值
# items() 以列表返回可遍历的(键, 值) 元组数组

dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 根据键查找值
print(dict1.get('name'))
print(dict1.get('ID'))
print(dict1.get('ID', 1001))

# 获取所有的键
print(dict1.keys())

# 获取所有的值
print(dict1.values())

# 获取所有的键值对
print(dict1.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender', 'male')])
