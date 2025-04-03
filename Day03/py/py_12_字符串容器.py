# 定义字符串
str1 = 'Hello'
str2 = 'Python'
str3 = 'i\'lovepython' #todo \反斜线表示转义字符,能把符号转为原始含义
str4 = "i'love python"
str5 = 'i"love python'
print(str1 + str2 + str3 + str4 + str5)

str6 = "hello python"
#需求:根据索引获取到字母e
print(str6[1]) # [ ]内的数字是从0开始计数,str6的e在第二个所以是1
#需求:根据索引获取到字母p
print(str6[6])
#需求:根据索引获取到最后一个字母
print(str6[11]) # n 已经是最后一个元素的,再往下就会报错
#print(str6[12]) IndexError: string index out of range

# todo 容器中的索引支持负索引
print(str6[-1])
print(str6[-2])
# print(str6[-100]) IndexError: string index out of range