# 使用for和while实现 99 乘法表

for h in range(1,10):
    l = 1
    print()
    while l <= h:
        print(f"{l}x{h}={l*h} ", end="")
        l += 1