# 给定两个集合，现要求移动其中一个集合的数到另一个集合，
# 使得原集合与后集合的平均值均上升（不能不变），每实现一次
# 即为使用了一次Magic方法，问最多能多少次Magic
def avgSet(sum, n):
    return sum / n


def MagicMove(set1, set2):
    sum1 = 0
    sum2 = 0
    for i in set1:
        sum1 += i
    for i in set2:
        sum2 += i
    avg1 = avgSet(sum1, len(set1))
    avg2 = avgSet(sum2, len(set2))
    if avg1 == avg2:  # 重定向
        return 0
    if avg1 > avg2:
        summore = sum1
        sumless = sum2
        setmore = set1
        setless = set2
    else:
        summore = sum2
        sumless = sum1
        setmore = set2
        setless = set1
    nmore = len(setmore)
    nless = len(setless)
    magic = 0
    for i in setmore:
        if avgSet(sumless, nless) < i < avgSet(summore, nmore) and i not in setless:
            summore -= i
            nmore -= 1
            nless += 1
            sumless += i
            setless.add(i)  #不需要管大集合的删除操作
            magic += 1
    return magic

set1 = set([3,4,5])
set2 = set([4.1,5,6])
print(MagicMove(set1,set2))