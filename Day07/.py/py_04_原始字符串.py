"""
原始字符串: 在字符串左边加上 r .字符串内容就会保持原有的样子.不会转义;
"""

import re

# 例如，一起来完成：
# （1）请使用正则来匹配路径名：`E:\\`；
# （2）请尝试使用不同方式去匹配数据，观察效果；

str1 = "E:\\"
print(re.findall("[A-Z]:\\\\", str1)) # ['E:\\']
print(re.findall(r"[A-Z]:\\", str1)) # ['E:\\']

# （3）思考：当要定义一段批量文本内容时，该怎么定义字符串？
str2 = R"<html></html>\d\n\r\u\U"
print(str2)# <html></html>\d\n\r\u\U
