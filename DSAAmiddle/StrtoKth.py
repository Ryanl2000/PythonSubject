# 给定字符串，求他的字典序
def g(i, len):  # 以i开头，总长度为len的子序列个数
    if len == 1:
        return 1
    sum = 0
    for j in range(i + 1, 26):
        sum += g(j, len - 1)
    return sum

def f(len):  # 长度为len的字符序列个数
    sum = 0
    for i in range(26):
        sum += g(i, len)
    return sum

def StrtoKth(arr):
    res = 0
    for i in range(1, len(arr)):
        res += f(i)
    first = ord(arr[0]) - ord('a')
    for i in range(first):
        res += g(i, len(arr) - 1)
    pre = first
    for i in range(1, len(arr)):
        cur = ord(arr[i]) - ord('a')
        for j in range(pre + 1, cur):
            res += g(j, len(arr) - i)
        pre = cur
    return res + 1


print(StrtoKth('ab'))