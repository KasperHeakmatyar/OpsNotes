# 练习题1：输入一个字符串，打印所有偶数位上的字符(下标是0，2，4，6…位上的字符)

s1 = input("录入字符串: ")
print(s1[::2])


# 练习题2：给定一个文件名(a.txt)，判断其尾部是否以".png"结尾
s2 = "a.txt"

result = s2.find(".png")
if result == -1:
    print("不是.png结尾")
