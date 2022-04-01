#概率转换问题一
from random import randint

def fiveProb():  #给定：等概率返回1~5的整数
    return randint(1,5)

def BitProb():  #等概率返回0和1
    while 1:
        n = fiveProb()
        if n == 5:
            continue
        if n < 3:
            return 0
        else:
            return 1

def SevenProb():  #等概率返回1~7的整数（任意数字均类似）
    while 1:
        n1 = BitProb()
        n2 = BitProb()
        n3 = BitProb()
        n = (n1 << 2) + (n2 << 1) + n3
        if n == 7:
            continue
        return n + 1

#概率转换问题二
def binomialProb():  #给定：返回0的概率为P，返回1的概率为（1-P）
    return randint(0,1)  #假设不等概率

def EqualBinomialProb():  #等概率返回0和1
    while 1:
        n1 = binomialProb()
        n2 = binomialProb()
        if n1 == 1 and n2 == 1:
            continue
        if n1 == 0 and n2 == 0:
            continue
        if n1 == 0 and n2 == 1:
            return 0
        if n1 == 1 and n2 == 0:
            return 1

# print(fiveProb())
# print(BitProb())
# print(SevenProb())
# print(binomialProb())
# print(EqualBinomialProb())