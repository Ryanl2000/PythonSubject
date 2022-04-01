#最大子数组和（子数组代表连续）
#最大子矩阵和（子矩阵代表连续）
def MaxSubArray(arr):
    maxs = float('-inf')
    cur = 0
    for i in arr:
        cur += i
        maxs = max(maxs, cur)
        if cur < 0:
            cur = 0
    return maxs

def MaxSubMatrix(matrix):
    n = len(matrix)
    maxs = float('-inf')
    for i in range(n):
        temp = [0 for _ in range(len(matrix[0]))]
        for j in range(i,n):
            for k in range(len(matrix[0])):
                temp[k] += matrix[j][k]
            maxs = max(MaxSubArray(temp), maxs)
    return maxs

arr = [1,1,-1,-10,11,4,-6,9]
print(MaxSubArray(arr))

ma = [[-5,3,6,4],[-7,9,-5,3],[-10,1,-200,4]]
print(MaxSubMatrix(ma))