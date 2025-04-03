# todo 吃葡萄案例,有一串葡萄.第三棵坏了,其他的20颗都是好的.模拟吃葡萄过程

count = 0 #吃葡萄计数器
for i in range(1, 21):
    if i == 3:
        print(f"第{i}颗坏了,不吃")
        continue
    print(f"正在吃第{i}颗葡萄")
    count += 1
else:
    print(f"吃葡萄完毕...共吃了{count}颗葡萄")