# break 是会结束循环的,循环回立刻终止.
# break只能用在循环中.
# todo 有一笼包子10哥,我的饭量是6个,使用循环模拟吃包子过程
for i in range(1, 11):
    if i == 6:
        print(f"已经吃了{i}个,吃饱了")
        break
    print(f"正在吃第{i}个包子")
else:
    print("饭量真大,吃完了")