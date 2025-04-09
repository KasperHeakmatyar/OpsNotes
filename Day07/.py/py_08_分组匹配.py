import re

#例如,一起来完成
# 1. 使用X|Y来匹配出0-100之间的所有数字字符结果:
print(re.match('^100|[1-9]?[0-9]$', '100')) # match='100'
print(re.match('^100|[1-9]?[0-9]$', '0'))  # match='0'
print(re.match('^100|[1-9]?[0-9]$', '55')) # match='55'

# 2. 使用(x)来匹配出含有163,126,qq这几个内容且用户名位数位4-12位的邮箱,如itcast@163.com等.
result = re.match('(\w{4,12})@(163|126|qq)\.(com|cn)', 'itcast@163.com')

print(result) # match='itcast@163.com'
print(result.group()) # itcast@163.com 获取匹配到的全部数据
print(result.group(1)) # itcast
print(result.group(2)) # 163
print(result.group(3)) # com
# print(result.group(4))# IndexError: no such group