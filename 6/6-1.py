def test(idx):
    try:
        abc = ['a','b','c']
        print(abc[idx])

    except IndexError as IdE:
        print('インデックスが範囲外になっています')

test(10)