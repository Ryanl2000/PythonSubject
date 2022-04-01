# 一个整数数组中，有的数字出现了两次，有的数字没有出现
# 空间复杂度1，时间复杂度O(N)，找出没有出现的数字
def Inplace(arr):
    if not arr:
        return
    for index in arr:
        modify(index, arr)
    res = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            res.append(i + 1)
    return res

def modify(index, arr):
    while arr[index - 1] != index:
        temp = arr[index - 1]
        arr[index - 1] = index
        index = temp

print(Inplace([1,3,4,6,6,6]))