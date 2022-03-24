import heapq

h = []
h_max = []
while 1:  #输入数字，并随时返回中位数
    s = int(input('输入数字，Ctrl+C结束：'))
    if not h_max or s <= -heapq.nsmallest(1, h_max)[0]:
        heapq.heappush(h_max, -s)
    else:
        heapq.heappush(h, s)
    if len(h) - len(h_max) == 2:
        heapq.heappush(h_max, -heapq.heappop(h))
    if len(h_max) - len(h) == 2:
        heapq.heappush(h, -heapq.heappop(h_max))
    if len(h_max) == len(h):
        print((-heapq.nsmallest(1, h_max)[0] + heapq.nsmallest(1, h)[0]) / 2)
    elif len(h_max) > len(h):
        print((-heapq.nsmallest(1, h_max)[0]))
    else:
        print(heapq.nsmallest(1, h)[0])