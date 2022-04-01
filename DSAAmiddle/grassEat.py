#吃草问题（4**n）
def eatGrass(n):
    if n < 5:
        return '先手' if n != 2 and n != 0 else '后手'
    
    base = 1
    while base <= n:
        if eatGrass(n - base) == '后手':
            return '先手'
        # if base > n // 4:  #防止base * 4后溢出
        #     break
        base *= 4
    return '后手'

def eatGrassUltar(n):  #规律总结
    if n % 5 == 0 or n % 5 == 2:
        return '后手'
    return '先手'

def compare():  #对数器
    for i in range(50):
        if eatGrass(i) != eatGrassUltar(i):
            return False
    return True

print(compare())