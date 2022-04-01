# 二维列表寻找值是否存在
# 列表在行列上满足单调性
def FindList(arr, aim):
    i = 0
    j = len(arr[0]) - 1
    while i < len(arr) and j > 0:
        if arr[i][j] == aim:
            return True
        if arr[i][j] > aim:
            j -= 1
        else:
            i += 1
    return False

arr = [[1,3,5,8],[2,4,7,10],[4,5,9,11],[7,8,10,12]]
print(FindList(arr,6))
print(FindList(arr,5))