# 1.已知字符串:"www.itcast.cn"  求出 www.itcast
# 2.已知字符串:"C:/etl/input\order.csv" 求出:"C:/etl/input/order.csv"
# 3.已知字符串:"C:/etl/input"和"order.csv" 求出:"C:/etl/input/order.csv"

#1

s1 = "www.itcast.cn"
print(s1[0:-3])

#2

s2 = "C:/etl/input\order.csv"
s2_1 = s2.replace("\\","/")
print(s2_1)

#3

s3_1 = "C:/etl/input"
s3_2 = "order.csv"
s3_3 = ""
s3_3 = s3_1.replace("C:/etl/input","C:/etl/input/order.csv")
print(s3_3)
