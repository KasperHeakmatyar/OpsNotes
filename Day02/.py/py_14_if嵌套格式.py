# 情节描述：上公交车，并且可以有座位坐下
# 要求：输入公交卡当前的余额，只要超过2元，就可以上公交车；如果车上有空座位，就可以坐下。

card_balance = int(input("录入公交卡余额"))
if card_balance >= 2:
    print("坐公交")
    seat_ava = int(input("录入座位数量"))
    if seat_ava > 0:
        print("坐下")
    else:
        print("站票")
else:
    print("请充值")
