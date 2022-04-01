# 给定一个字符串
# 每个字符至少保留一个
# 返回最小字典序
from collections import Counter
def Mindict(str):
    if not str or len(str) == 1:
        return str
    c = Counter()
    for i in str:
        c[i] += 1
    mindex = 0
    for i in range(len(str)):
        if c[str[i]] == 1:
            break
        c[str[i]] -= 1
        mindex = i if str[i] < str[mindex] else mindex  #找到最小字典序的字符
    temp = str[mindex] 
    str = str[mindex + 1:]
    while temp in str:  #删除后续中存在的temp
        str.remove(temp)
    return [temp] + Mindict(str)

print(Mindict([1,2,3,3,3]))
