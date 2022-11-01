from random import randint
from unittest import result

def random_array(size):
    array = []
    for v in range(size):
        num = randint(0,100)
        array.append(num)
    return array

result = random_array(5)
print(result)

