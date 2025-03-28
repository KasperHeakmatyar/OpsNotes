## 使用cmd检查python是否安装完成
1. run cmd
2. type 'python -V'
3. check if outputs meet the version installed
![[Pasted image 20250328163832.png]]
---

## 使用pycharm创建项目

![[Pasted image 20250328161332.png]]

---
## Python基本语法

### 注释
注释分为两种  
1.单行注释: 以#开头  
2.多行: """ """

### 变量和类型

```
"""  
变量：用于存储一个数据的容器，其值可以发生改变  
语法：变量名 = 值 起名要见名知意  
"""  
a = 18  
print(a)# 18  
a = 19  
print(a)# 19  
  
"""  
变量类型：  
     1.整数/数字类型： int     
     2.字符串类型： str     
     3.布尔类型： bool     
     4.小数（浮点型）： float
"""  
age = 19  
name = "Tom"  
sex = False  
height = 1.75  
  
#查看变量的类型可以使用type()函数  
print(type(age))  
print(type(name))  
print(type(sex))  
print(type(height))

```

### 标识符
```
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
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']  
"""  
  
#变量名不能使用关键字  
# if = 100  
# and = 50  
  
#推荐命名规范  
myName = 100 #小驼峰  
MyName = 100 #大驼峰  
my_name = 100 #下划线
```

### 输出
```
# todo print函数  
print("hello")  
print("hello", "world")  
print("hello", "world", "python")  
  
# todo print函数可以打印1-默认分隔符 sep=' 'print("hello", "world", sep=',') # hello,world  
  
# todo print 函数可以打印1- 默认换行符 end='\n'print("hello", end='#')  
print("world", end='#')
```