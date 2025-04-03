# 1 定义一个字符串 str1, 字符串的内容为 "hello world and itcast and itheima and Python"

# 2 在字符串str1中查找 字符串 and 的下标

# 3 在字符串str1中查找字符串 'good'的下标

# 4 将字符串str1中的 and 替换为 or

# 5 将字符串 str1 按照 空白字符进行切割,保存到变量 list1 中

#1
str1 = "hello world and itcast and itheima and Python"

#2
print(str1.find('and'))

#3
print(str1.find('good'))

#4
print(str1.replace('and', 'or'))

#5
list1 = str1.split(" ")
print(list1)
