# 斐波那契数列的logN算法
# 原理：矩阵、线性代数
def Fibprocess(n):
    if n < 1:
        return -1
    if n == 1 or n == 2:
        return 1
    base = [[1,1],[1,0]]
    res = matrixPower(base, n-2)
    return res[0][0] + res[1][0]

def matrixPower(base, n):  #矩阵次方
    res = [[0 for _ in range(len(base[0]))] for _ in range(len(base))]
    for i in range(len(base)):
        res[i][i] = 1
    temp = base
    # 方法：二进制次方法
    while n:
        if n & 1:
            res = muliMatrix(res, temp)
        temp = muliMatrix(temp, temp)
        n >>= 1
    return res

def muliMatrix(m1, m2):  #矩阵相乘
    res = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][j]
    return res

print(Fibprocess(6))