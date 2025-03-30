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
