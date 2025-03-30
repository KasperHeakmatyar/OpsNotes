# 1. 定义字符串变量 name ，输出 我的名字叫 ⼩明，请多多关照！
# 2. 定义整数变量 student_no ，输出 我的学号是 000001
# 3. 定义⼩数 price 、 weight 、 money ，输出 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元
# 4. 定义⼀个⼩数 scale ，输出 数据⽐例是 10.00%

name = "小明"
print("我的名字叫%s，请多多关照！" % name)
print(f"我的名字叫{name}，请多多关照！")

student_no = "000001"
print("我的学号是%s" % student_no)
print(f"我的学号是{student_no}")

scale = 10.00
print("数据比例是%.2f%%" % scale)
print(f"数据比例是{scale:.2f}%")

price = 9.00
weight = 5.00
money = 45.00
print("苹果单价 %5.2f 元/斤，购买了 %5.2f 斤，需要支付%5.2f 元"%(price,weight,money))
print(f"苹果单价 {price:5.2f} 元/斤，购买了 {weight:5.2f} 斤，需要支付{money:5.2f} 元")

# 编写代码完成以下名片的显示
# ==========我的名片==========
# 姓名: itheima QQ:xxxxxxx
# 手机号:185xxxxxx
# 公司地址:北京市xxxx
# ===========================

name = "itheima"
QQ = 1243253253
phone = 18543242
address = "北京市朝阳"

print("==========我的名片==========")
print(f"姓名:{name} QQ:{QQ}")
print(f"手机号:{phone}")
print(f"公司地址:{address}")
print("===========================")