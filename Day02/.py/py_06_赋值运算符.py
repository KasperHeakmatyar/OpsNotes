# # = 赋值运算符  把 = 号右边的结果 赋给 左边的变量，
# 如 num = 1 + 2 * 3，结果num的值为7

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