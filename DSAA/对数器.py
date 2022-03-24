from audioop import reverse
from functools import cmp_to_key
from random import randint

def creat(randnum):
    res = []

    while randnum:
        randnum -= 1
        temp = ''
        n = randint(1,5)
        for i in range(n):
            str_ = chr(ord('a') + randint(0,25))
            temp += str_
        res.append(temp)
    
    return res

def compare(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    return 0


def greed(list):
    list.sort(key=cmp_to_key(compare), reverse=True)
    return list
    

rest = creat(100)
print(rest)
print('\n')
print(greed(rest))

