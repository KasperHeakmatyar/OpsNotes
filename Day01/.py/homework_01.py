name = "孙悟空" #str类型
age = 600 #int类型
skillset = "筋斗云、72变" #str类型
battle_record = "大闹天宫" #str类型

"""
拆成两句话，从'600岁的孙悟空能够使用'为一段，其中已经定义孙悟空，600。接下来用sep='',和end=''来填充缺失的部分。
下一段'筋斗云、72变来大闹天宫。'确实来和。，使用sep='来'和end='。'来填充。
"""
print(age, name, sep='岁的', end='能够使用', )
print(skillset, battle_record, sep='来', end='。')

#better version
"""
print(age, '岁的', name, '能够使用', skillset, '来', battle_record, sep='', end='。')
"""
