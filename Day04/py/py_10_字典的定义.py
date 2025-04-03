"""
定义
    dict1 = {}
    dict2 = {"name":"tom","age":19}
    dict3 = dict()
获取数据: 按照key来获取
    字典['key']
"""

dict1 = {}
dict2 = dict()
dict3 = {"id": 100, "name": "tom", "age": 19, 0: 1}
print(type(dict1), type(dict2), type(dict3))  # <class 'dict'> <class 'dict'> <class 'dict'>
print(dict1, dict2, dict3)  # {} {} {'id': 100, 'name': 'tom', 'age': 19, 0: 1}

# 获取字典的一个数据
print(dict3["name"])  # tom
print(dict3["age"])  # 19

print(dict3[0])  # 这不是按照索引取值,是有一个k为0的数据.
