# 制作用户登录系统：已知A用户注册的用户名为`aaa`，密码是`123456`。具体要求如下：
#
# 登录时需要验证用户名、密码、验证码(固定验证码为`qwer`)。
#
# 要求: 先验证验证码是否正确，正确后再验证用户名和密码。

user_id = "aaa"
user_pw = "123456"
user_code = "qwer"

code_input = input("输入验证码: ")
if code_input == user_code:
    id_input = input("请输入用户名: ")
    pw_input = input("请输入密码: ")
    if id_input == user_id and pw_input == user_pw:
        print("登陆成功")
    else:
        print("账号信息有误")
else:
    print("验证码有误")
