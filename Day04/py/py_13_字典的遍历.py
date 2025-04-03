dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}

# 方式1:
for k in dict1.keys():
    print(k, dict1[k]) # name Tom 同时获取到键和值

# 方式2 #隐藏了元组自动拆包 k,v = ('name', 'Tom')
for k,v in dict1.items(): # ('name', 'Tom')
    print(k,v)

# todo 如果你只想拿到字典的value [了解]

for v in dict1.values():
    print(v)

# todo 直接for遍历字典,便利的内容是key [了解]
for k in dict1:
    print(k, dict1[k])