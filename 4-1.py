def compare_string(a,b):
    if len(a)>len(b):
        print(a)
    else:
        print(b)

print("文字数を比較します")

a = input('1つ目の文字を入力')
b = input('2つ目の文字を入力')

compare_string(a,b)