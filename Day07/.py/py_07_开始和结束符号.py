import re

#例如,一起来完成

# 1. 使用^来匹配非数字的单个字符
print(re.match('^\D', 'a')) # match='a'
print(re.match('^\D', 'ab')) # match='a'
print(re.match('^\D$', 'ab')) # None

# 扩展: ^ 如果在[]内部,表示非(取反)的意思
print(re.match('[^0-9]', 'a')) # match='a'
print(re.match('[^0-9]', '*')) # match='*'
print(re.match('[^0-9]', '1')) # None

# 2. 使用$来匹配 www.baidu.com的结尾处
print(re.match('www\.\w{2,10}\.com$', 'www.baidu.com')) # match='www.baidu.com'
print(re.match('www\.\w{2,10}\.com$', 'www.baidu.com123')) # None
print(re.match('www\.\w{2,10}\.com$', 'www.a.com')) # None