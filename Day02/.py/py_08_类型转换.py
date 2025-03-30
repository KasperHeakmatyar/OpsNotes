# float(x): x是任意类型的数据
# str(x): x是任意类型的数据

print(float(10)) #10转换为浮点
f1 = float("3.14") #字符串转换为浮点
print(type(f1)) # <class 'float'>
print(f1) #3.14

# todo 转换(整数和小数)有风险.需要仔细观察: [不是数字字符不能转换 ,转小数时,圆点除外]
# print(float("3.1a")) #ValueError: could not convert string to float: '3.1a'

# 转字符串 -- 一切数据皆可转换
print(str(123))
print(str(123.23))
print(str("abc"))
print(str(True))
