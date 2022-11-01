def get_sum(**kargs):
    start = kargs['start']
    end = kargs['end']

    result = 0

    if start <= end:
        for v in range(start,end+1):
         result = result + v
        print(result)

    else:
        for v in range(end,start+1):
            result = result + v
        print(result)

get_sum(start=1, end = 100)

#rangeはあくまでendまでは入らない
for i in range(1,10):
    print(i)
