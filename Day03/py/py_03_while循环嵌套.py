#todo: 连续五天每天跑3圈
d = 1
while d <= 5:
    print(f"第{d}天")
    #----------被嵌套的循环----------
    c = 1
    while c <= 3:
        print(f"正在跑第{d}天的第{c}圈")
        c += 1
    print(f"第{d}天跑步结束")
    # -----------------------------
    d += 1

#rewrite

d_1 = 1
while d_1 <= 5:
    l = 1
    while l <= 3:
        print(f"第{d_1}天跑第{l}圈")
        l += 1
    print(f"第{d_1}天跑步结束")
    d_1 += 1

