# 位运算符的结合数量
def BitOperation(L, R, desire, arr):
    if L == R:
        if arr[L] == '1':
            return 1 if desire else 0
        else:
            return 0 if desire else 1

    res = 0
    if desire:
        for i in range(L + 1, R, 2):
            if arr[i] == '&':
                res += BitOperation(L, i - 1, True, arr) * \
                    BitOperation(i + 1, R, True, arr)
            if arr[i] == '|':
                res += BitOperation(L, i - 1, True, arr) * \
                    BitOperation(i + 1, R, True, arr)
                res += BitOperation(L, i - 1, True, arr) * \
                    BitOperation(i + 1, R, False, arr)
                res += BitOperation(L, i - 1, False, arr) * \
                    BitOperation(i + 1, R, True, arr)
            if arr[i] == '^':
                res += BitOperation(L, i - 1, True, arr) * \
                    BitOperation(i + 1, R, False, arr)
                res += BitOperation(L, i - 1, False, arr) * \
                    BitOperation(i + 1, R, True, arr)
    else:
        for i in range(L + 1, R, 2):
            if arr[i] == '&':
                res += BitOperation(L, i - 1, False, arr) * \
                    BitOperation(i + 1, R, False, arr)
                res += BitOperation(L, i - 1, True, arr) * \
                    BitOperation(i + 1, R, False, arr)
                res += BitOperation(L, i - 1, False, arr) * \
                    BitOperation(i + 1, R, True, arr)
            if arr[i] == '|':
                res += BitOperation(L, i - 1, False, arr) * \
                    BitOperation(i + 1, R, False, arr)
            if arr[i] == '^':
                res += BitOperation(L, i - 1, True, arr) * \
                    BitOperation(i + 1, R, True, arr)
                res += BitOperation(L, i - 1, False, arr) * \
                    BitOperation(i + 1, R, False, arr)
    return res

def BitOperationUltar(desire, arr):  #动态规划
    n = len(arr)
    dpTrue = [[0 for _ in range(n)] for _ in range(n)]
    dpFalse = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n,2):
        dpTrue[i][i] = 1 if arr[i] == '1' else 0
        dpFalse[i][i] = 0 if arr[i] == '1' else 1
    for i in range(n-3, -1, -2):
        for j in range(i+2, n, 2):
            for k in range(i+1, n, 2):
                if arr[k] == '&':
                    dpTrue[i][j] += dpTrue[i][k-1] * dpTrue[k+1][j]
                    dpFalse[i][j] += dpFalse[i][k-1] * dpFalse[k+1][j]
                    dpFalse[i][j] += dpTrue[i][k-1] * dpFalse[k+1][j]
                    dpFalse[i][j] += dpFalse[i][k-1] * dpTrue[k+1][j]
                if arr[k] == '|':
                    dpTrue[i][j] += dpTrue[i][k-1] * dpTrue[k+1][j]
                    dpTrue[i][j] += dpTrue[i][k-1] * dpFalse[k+1][j]
                    dpTrue[i][j] += dpFalse[i][k-1] * dpTrue[k+1][j]
                    dpFalse[i][j] += dpFalse[i][k-1] * dpFalse[k+1][j]
                if arr[k] == '^':
                    dpTrue[i][j] += dpTrue[i][k-1] * dpFalse[k+1][j]
                    dpTrue[i][j] += dpFalse[i][k-1] * dpTrue[k+1][j]
                    dpFalse[i][j] += dpTrue[i][k-1] * dpTrue[k+1][j]
                    dpFalse[i][j] += dpFalse[i][k-1] * dpFalse[k+1][j]
    return dpTrue[0][n-1] if desire else dpFalse[0][n-1]
    

arr = '1^0|0&0'
arr = list(arr)
print(BitOperation(0, len(arr)-1, True, arr))
print(BitOperationUltar(True, arr))
