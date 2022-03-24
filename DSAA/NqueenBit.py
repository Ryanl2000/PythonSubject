#N皇后问题的位运算解法
import sys

n = eval(input())
#适用于32皇后以内，如过超过32，要改类型为long int
if n < 1 or n > 32:
    sys.exit(0)
limit = (1 << n) - 1
def NqueenBit(limit, col, leftside, rightside):  #分别为总限制（位数限制）、列限制、左斜边限制、右斜边限制
    if limit == col:
        return 1
    res = 0
    pos = limit & (~(col | leftside | rightside))
    while pos:
        rightest = pos & (~pos + 1)  #pos最右边的1
        pos -= rightest
        res += NqueenBit(limit
                        ,col | rightest
                        ,(leftside | rightest) << 1
                        ,(rightside | rightest) >> 1
                        )  
    return res

print(NqueenBit(limit, 0, 0, 0))