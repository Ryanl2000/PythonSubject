#抽纸牌游戏
def first(arr, l, r):  #先手函数
    if l == r:
        return arr[l]
    return max(
        arr[l] + second(arr, l+1, r),
        arr[r] + second(arr, l, r-1)
    )

def second(arr, l, r):  #后手函数
    if l == r:
        return 0
    return min(
        first(arr, l+1, r),
        first(arr, l, r-1)
    )

arr = [1,2,100,5]
print(first(arr, 0, len(arr) - 1))
print(second(arr, 0, len(arr) - 1))