# 例如.
# 1. 使用, 来匹配任意单个字符
import re

print(re.match(',','\n')) # None

print(re.match('.','\r')) # <re.Match object; span=(0, 1), match='\r'>

print(re.match('.','你好')) # <re.Match object; span=(0, 1), match='你'>

print(re.match('.','hello')) # <re.Match object; span=(0, 1), match='h'>

# 2. 使用[a-z],[A-Z],'[^0-9]'分别来查看小写字母,大写字母,非数字:
print(re.match('[a-z]','agc')) # match='a'
print(re.match('[a-z]','gca')) # match='g'
print(re.match('[a-z]','6abc')) # None

print(re.match('[A-Z]','abc')) # None
print(re.match('[A-Z]','Abc')) # match='A'

print(re.match('[^0-9]','abc')) # match='a'
print(re.match('[^0-9]','$ab')) # match='$'
print(re.match('[^0-9]','6ab')) # None

print(re.match('[a-f3-9A-Z]','ddd')) # <re.Match object; span=(0, 1), match='d'>
print(re.match('[a-f3-9A-Z]','666')) # <re.Match object; span=(0, 1), match='6'>
print(re.match('[a-f3-9A-Z]','MMM')) # <re.Match object; span=(0, 1), match='M'>

# 3. 使用\d来匹配一个数字字符: \d就是对[0-9]的简化方案
print(re.match('\d','123')) # <re.Match object; span=(0, 1), match='1'>
print(re.match('\d','a123')) # None

# （4）使用\w来匹配一个可能有数字、大小写字母、下划线的单个字符。
print(re.match('\w','123'))# match='1'
print(re.match('\w','aaa'))# match='a'
print(re.match('\w','AAA'))# match='A'
print(re.match('\w','___'))# match='_'
print(re.match('\w','你好'))# match='你'
print(re.match('\w','$$$')) #None