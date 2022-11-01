num = input("数字を1つ入力してください")
num = int(num)

def nabeatu(v):
    if "3" in str(num) or num%3==0:
        print("あほ")
    else:
        print(v)

nabeatu(num)