while True:
    year_input = input("输入年份（输入 q 或 Q 退出）: ")
if year_input == 'q' or year_input == 'Q':
    print("系统退出")
    break
else:
    year = int(year_input)
    if (year % 4 ==0 and year % 100 ==0) or (year % 400) == 0:
        print(f"{year}是闰年")
    else:
        print(f"{year}不是闰年")