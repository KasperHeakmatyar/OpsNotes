"""
for 临时变量 in 列表或者字符串等:
    循环满足条件时执行的代码
"""

str1 = "abcdef"
for s in str1:
    print(s)

print("~"*30)

#如果有字母c,打印的时候打C

s1 = "abcdef123ccc"
for s in s1:
    if s == "c":
        print("C", end="")
    else:
        print(s, end="")