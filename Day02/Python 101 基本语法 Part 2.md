两个%连着写可以print出%
![[Pasted image 20250329100835.png]]

## 格式化输出
### 语法: "xxx占位符xxx" % (赋值的变量)

```
# %s 字符串(string)
# %d 整形(int)
# %f 浮点型(float)
# 格式: "字符串(包含占位符)" % (为占位值的变量)
age = 10
print("我的年龄是%d" % age)
a = 20
b = 30
c = 40
print("我们有三个组,a组%d人,b组%d人,c组%d人." % (a, b, c)) #多占位符在后面的
变量要用另外的括号

特殊 浮点型字符数和小数点控制
a = 10.456
print("A值为%6.2f" % a) #A值为 10.46
6是整体数位符,2是保留几位小数
```
---
## F格式化输出
### 语法:
```
F格式化是对占位符的一种优化,方便使用.
print(F"我的名字是{name}")
print(f"我的名字是{name}")
F不分大小写
```

### 案例:
```
num = 100  
print(F"我的数字是:{num}")  
print(f"我的数字是:{num}")  
  
# 1. 定义字符串变量 name ，输出 我的名字叫 ⼩明，请多多关照！  
name = "小明"  
print(f"我的名字叫 {name} ，请多多关照！")  
# 2. 定义整数变量 student_no ，输出 我的学号是 000001student_no = '000001'  
print(f"我的学号是 {student_no}")  
# 3. 定义⼩数 price 、 weight 、 money ，输出 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元  
price = 9.00  
weight = 5.00  
money = 45.00  
print(F"苹果单价 {price:.2f} 元／⽄，购买了 {weight:.2f} ⽄，需要⽀付 {money:.2f} 元")  
# 4. 定义⼀个⼩数 scale ，输出 数据⽐例是 10.00%scale = 10.00  
print(F"数据比例是{scale:.2f}%")
```

---

## input录入函数
```
# input()  
# 的小括号中放入的是，提示信息，用来在获取数据之前给用户的一个简单提示  
# input()  
# 在从键盘获取了数据以后，会存放到等号左边的变量中  
# input()  
# 会把用户输入的任何值都作为字符串来对待  
  
password = input("请输入密码")  
print("您刚刚输入的密码是: %s" % password)  
print(f"您刚刚输入的密码是: {password}")  
  
#从键盘上录入苹果的价格 、重量 ，输出: 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元.  
  
price = input("苹果价格：")  
weight = input("苹果重量：")  
money = input("支付金额：")  
print("苹果单价 %s 元/斤，购买了 %s 斤，需要支付 %s 元。" % (price, weight, money))  
print(f"苹果单价 {price} 元/斤，购买了 {weight}  斤，需要支付{money} 元。")
```
---

## 算术运算符
```
# + 加  两个对象相加 a + b 输出结果 30
# - 减  得到负数或是一个数减去另一个数 a - b 输出结果 -10
# * 乘  两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 200
# / 除  b / a 输出结果 2
# //    取整除    返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
# % 取余 返回除法的余数 b % a 输出结果 0
# **    指数 a**b 为10的20次方， 输出结果 100000000000000000000
```

```
a = 5  
b = 6  
print(a+b) #11  
print(a-b) #-1  
print(a*b) #30  
print(a/b) #0.8333333333333334  
print(a//b) #0  
print(a%b) #5  
print(a**b) #15625
```
---

## 赋值运算符
```
# = 赋值运算符  把 = 号右边的结果 赋给 左边的变量，
如 num = 1 + 2 * 3，结果num的值为7
```

```
a = 3
print(a) # 3

# todo --------以下是复制和算术运算符的结合体-----------------------------------
# +=	加法赋值运算符	c += a 等效于 c = c + a
a += 3
print(a) # 6 ==> a = a + 3 ==> [左+右的结果再赋值给左]
# -=	减法赋值运算符	c -= a 等效于 c = c - a
a -= 3
print(a)
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
a *= 3
print(a) # 9
# /=	除法赋值运算符	c /= a 等效于 c = c / a
a /= 3
print(a) # 3.0
# %=	取模赋值运算符	c %= a 等效于 c = c % a
a %= 2
print(a) # 1.0
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
a **= 3
print(a)# 1.0
# //=	取整除赋值运算符	c //= a 等效于 c = c // a
a //= 2
print(a) # 0.0

注意代码从上到下运行,a的值在被上一行代码赋值
```
---

## 数据类型转换

```
使用场景: 在进行数学运算的时候使用.  
语法:  
   int(x) x为任意类型数据  
   float(x)   
   str(x)
 
  
# method 1  
age = input("请输入年龄")  
#打印明年年龄  
age = int(age)  
age = age + 1  
print("我明年的年龄是%d岁." % age)  
print(f"我明年的年龄是{age}岁.")  
  
# method 2  
age = int(input("请输入年龄"))  
age += 1  
print("我明年的年龄是%d岁." % age)  
print(f"我明年的年龄是{age}岁.")

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
```
---

