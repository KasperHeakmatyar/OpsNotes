# ==	检查两个操作数的值是否相等，如果是则条件变为真。
# !=	检查两个操作数的值是否相等，如果值不相等，则条件变为真。
# >	检查左操作数的值是否大于右操作数的值，如果是，则条件成立。
# <	检查左操作数的值是否小于右操作数的值，如果是，则条件成立。
# >=	检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。
# <=	检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。

a = 5
b = 3
c = 5
print( a == b) # False
print( a == c) # True
print( a != c) # False

print(a >= b)# True
print(a >= c)# True
print(a > c)# False



# 逻辑运算符
# 或 : or
# 且 : and
# 非 : not
print(a > b and a > c) # False
print(a > b or a > c) # True
print(not a > b) # False
