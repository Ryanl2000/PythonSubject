#N皇后问题
n = eval(input())

list = [-1] * n
def isValid(i, j):  #判断能否安皇后
    for k in range(i):
        if list[k] == j or abs(list[k] - j) == abs(i - k):  #45°角代表在一个斜线上
            return False
    return True


def Nqueen(i, n):  #i为当前行
    if i == n:
        return 1
    res = 0
    for j in range(n):  #尝试i行所有列
        if isValid(i, j):
            list[i] = j
            res += Nqueen(i+1, n)
    return res

print(Nqueen(0, n))