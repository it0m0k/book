weight = input("体重をkg単位で入力してください")
height = input("身長をm単位で入力してください")
BMI = float(weight)/(float(height)*float(height))

print(BMI)

if BMI < 18.5:
    print("やせています")
    
elif 18.5 <= BMI< 25:
    print("ふつう")

elif 25 <= BMI <35:
    print("ちょっと太ってる")

else :
    print("だいぶ太ってる")