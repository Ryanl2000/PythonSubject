# 路灯问题
from random import randint


def MinLightMy(str):  #贪心算法（自编，可能有bug）
    if not str:
        return 0
    res = [0 for _ in range(len(str))]
    i = 0
    while i < len(str):
        if str[i] == 'X':  #当为X的时候不能放灯
            i += 1
            continue
        if i and str[i-1] == '.' and res[i-1] == 1:  #当前方为.且前方有灯，则跳过
            i += 1
            continue
        if i < len(str) - 1 and str[i+1] == '.':  #前方有.则灯放在前方
            res[i+1] = 1
            i += 2
            continue
        res[i] = 1  #普通情况直接放灯
        i += 1
    # return res
    return sum(res)

def MinLightGreedy(str):  #贪心算法
    index = 0
    light = 0
    while index < len(str):
        if str[index] == 'X':
            index += 1
            continue
        light += 1
        if index + 1 == len(str):
            break
        elif str[index + 1] == 'X':
            index += 2
        else:
            index += 3
    return light


str = ['X','.','.','X','.','.','.','X','X','.','.','.','.','.','X','.','.','.','.','X','X','.']
print(MinLightMy(str))
print(MinLightGreedy(str))


def compare():  #对数器
    n = 0
    while n < 3:
        str = []
        for i in range(100):
            k = randint(0,1)
            if k == 0:
                str.append('X')
            else:
                str.append('.')
        if MinLightMy(str) == MinLightGreedy(str):
            print(True)
        else:
            print(False)
        n += 1

# compare()


