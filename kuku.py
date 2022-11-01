from unittest import result


gyou = [1,2,3,4,5,6,7,8,9]
retsu = [1,2,3,4,5,6,7,8,9]
# 同じ変数みたいな感じで使えるから配列は1つでいい


for i in gyou:
    for j in retsu:
        print(i*j,end=' ')
    print('')

print('')

for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print('')

print('')
