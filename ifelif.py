height = float(input("please input your height(cm)"))/100
weight = float(input("please input your weight(kg)"))
bmi = weight/(height*height)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
