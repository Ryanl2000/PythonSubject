#汉诺塔问题
n = eval(input())

def Hanoi(x, from_, to_, other_):
    if x == 1:
        print('%s: %d -> %d'% (x, from_, to_))
    else:
        Hanoi(x-1, from_, other_, to_)
        print('%s: %d -> %d'% (x, from_, to_))
        Hanoi(x-1, other_, to_, from_)

Hanoi(n,0,1,2)