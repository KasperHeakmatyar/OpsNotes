"""
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
re{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
"""

# 例如，一起来完成：

import re

# （1）使用X*来匹配出一个字符串：第1个字母为大小写字母，后面都是小写字母且这些字母可有可无；
print(re.match('[a-zA-Z][a-z]*','abcd')) # match='abcd'
print(re.match('[a-zA-Z][a-z]*',"Abcd")) # match='Abcd'
print(re.match('[a-zA-Z][a-z]*','A')) # match='A'
print(re.match('[a-zA-Z][a-z]*','1')) # None
print(re.match('[a-zA-Z][a-z]*','A1')) # match='A'

# （2）通过X+来匹配一个具有数字、大小写字母、下划线的字符串；
print(re.match('\w+','')) # None
print(re.match('\w+','a')) # match='a'
print(re.match('\w+','abc')) # match='abc'
print(re.match('\w+','>')) # None

# （3）通过X?来匹配0到99之间的任意数字；
print(re.match('[0-99]?','a')) # match=''
print(re.match('[0-99]?','1')) # match='1'
print(re.match('[0-99]?','100')) #  match='1'

# （4）通过X{n,m}匹配出5到16位的密码，可以是大小写英文字母、数字、下划线。
print(re.match('\w{5,16}','abcd')) # None
print(re.match('\w{5,16}','abcde')) # match='abcde'
print(re.match('\w{5,16}','12345678901234567')) # match='1234567890123456'