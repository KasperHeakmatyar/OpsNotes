"""
标识符：给变量，类，函数等其名字的符号
     1.见名知意
     2.数字，字母，下划线组成
     3.数字不能开头
     4.区分大小写
"""
hello_2 = 100
# 2C = 100 数字不能开头
# $ = 10000 不能使用特殊符号

#导入关键字模块
import keyword
#导出关键字
print(keyword.kwlist)

"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']
"""

#变量名不能使用关键字
# if = 100
# and = 50

#推荐命名规范
myName = 100 #小驼峰
MyName = 100 #大驼峰
my_name = 100 #下划线