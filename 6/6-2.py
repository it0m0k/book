def add(a,b):
    try:
        print(a+b)
    except TypeError as type:
        print("数値以外のデータが入っています")

add(2,3)
add('a',0)
