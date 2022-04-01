# 咖啡问题
# arr ： 数组中代表有n台机器，数字分别代表每台机器的冲咖啡的时间
# N ： 代表有N个人准备喝咖啡
# a ：代表洗杯机洗一个杯子所用的时间（仅能同时洗一个）
# b ：代表杯子自然晾干所用的时间
# 设喝咖啡时间为0，求从第一杯咖啡开始冲，到最后一个杯子晾干所用的最短时间
class myheap:  # 自建小根堆
    def __init__(self) -> None:
        self.heap = []
        self.heapsize = 0

    def swap(self, l, r):
        temp = self.heap[l]
        self.heap[l] = self.heap[r]
        self.heap[r] = temp

    def add(self, arr):
        if self.heapsize == 0:
            self.heap.append(arr)
            self.heapsize += 1
            return

        index = self.heapsize
        self.heap.append(arr)
        self.heapsize += 1
        while sum(self.heap[index]) < sum(self.heap[abs(index - 1) // 2]):
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def heapfiy(self, index):
        left = index * 2 + 1
        while left < self.heapsize:
            little = left if left + \
                1 < self.heapsize and sum(self.heap[left]) < sum(self.heap[left + 1]) else left + 1
            little = little if sum(self.heap[little]) < sum(
                self.heap[index]) else index
            if little == index:
                break
            self.swap(little, index)
            index = little
            left = index * 2 + 1


def CoffeeDrink(arr, n):  # 不考虑洗杯子等，大家都喝完所用的时间
    coffeeheap = myheap()
    for i in arr:
        coffeeheap.add([0, i])
    drinkByPeople = []
    for i in range(n):
        coffeeheap.heap[0][0] += coffeeheap.heap[0][1]
        drinkByPeople.append(coffeeheap.heap[0][0])
        coffeeheap.heapfiy(0)
    return drinkByPeople  # 返回每个人喝完咖啡的时间


def AllTime(drink, a, b, index, washline):
    # drink : 每个人喝完时间列表
    # a ：洗杯机的洗杯时间
    # b ：自然晾干时间
    # index ：当前杯子
    # washline ：洗杯机可用时间
    if index == len(drink) - 1:  # 剩余最后一杯
        return min(max(washline, drink[index]) + a, drink[index] + b)
    #如果选择洗杯
    wash = drink[index] + a
    washnext = AllTime(drink, a, b, index + 1, wash)
    over1 = max(wash, washnext)  # 最终结束时间为当前杯子洗完的时间和剩余全部杯子洗完时间的最大值
    #如果选择自然干
    dry = drink[index] + b
    drynext = AllTime(drink, a, b, index + 1, washline)
    over2 = max(dry, drynext)  # 最终结束时间为当前杯子晾干的时间和剩余全部杯子洗完时间的最大值
    return min(over1, over2)

def AllTimeUltar(drink, a, b):  #动态规划
    washlineMax = 0
    for i in drink:
        washlineMax += max(i + a, washlineMax + a)
    print(washlineMax)
    dp = [[0 for _ in range(washlineMax)] for _ in range(len(drink))]
    n = len(drink)
    for i in range(len(dp[0])):
        dp[n-1][i] = min(max(i, drink[n-1]) + a, drink[n-1] + b)
    for i in range(n-2,-1,-1):
        for j in range(len(dp[0])):
            dp[i][j] = min(max(drink[i] + a, dp[i+1][drink[i] + a]), max(drink[i] + b, dp[i+1][j]))
    return dp[0][0]

arr = [3, 2, 7]
# print(CoffeeDrink(arr, 3))
print(AllTime(CoffeeDrink(arr, 3), 3, 5, 0, 0))
print(AllTimeUltar(CoffeeDrink(arr, 3), 3, 5))
