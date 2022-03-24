#KMP算法
def getNext(arr):  #获得next数组
    if len(arr) == 1:
        return [-1]
    next = [-2] * len(arr)
    next[0] = -1
    next[1] = 0
    i = 2
    cn = 0
    while i < len(arr):
        if arr[i-1] == arr[cn]:
            next[i] = cn + 1
            i += 1
            cn += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[i] = 0
            i += 1
    return next

def compareByKMP(arr1, arr2):  #KMP算法主函数
    if not arr1 or not arr2 or len(arr1) < len(arr2):
        print('Illegal input')
        return -1
    list1 = list(arr1)
    list2 = list(arr2)
    i1 = 0
    i2 = 0
    next = getNext(arr2)
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] == list2[i2]:
            i1 += 1
            i2 += 1
        elif next[i2] == -1:
            i1 += 1
        else:
            i2 = next[i2]
    return i1 - i2 if i2 == len(list2) else -1

# arr1 = 'abbacabbadabbcabbd'
# arr2 = 'abbc'
# print(compareByKMP(arr1, arr2))
