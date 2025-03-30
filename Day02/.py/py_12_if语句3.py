"""
if 条件1:
    条件1成立的代码
elif 条件2:
    条件2成立的代码
elif 条件3:
    条件3成立的代码
... ...(可以很多条件)
else:
    所有条件都不满足,走这里
"""

score = float(input("请录入分数"))
if score > 100 or score < 0:
    print("成绩录入有误,请重新录入")
elif score >= 90:
    print("成绩优秀")
elif score >= 80:
    print("成绩良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")
print("判断完毕")
