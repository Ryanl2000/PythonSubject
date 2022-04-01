# 题意见同名png文件
from collections import deque
def FindMinPath(Start, To, List):  #主函数
    nexts = {}
    distance = {}
    for arr in List:
        nexts[arr] = getnexts(arr, List)
    getdistance(Start, distance, nexts)
    res = []
    solution = []
    printResult(Start, To, distance, nexts, solution, res)
    for r in res:
        print('->'.join(r))

def getnexts(arr, List):  #获取和arr只差一个字符的nexts数组
    arr = list(arr)
    temp = []
    for i in range(26):
        for j in range(len(arr)):
            if ord(arr[j]) - ord('a') != i:
                tep = arr[j]
                arr[j] = chr(i + ord('a'))
                if ''.join(arr) in List:
                    temp.append(''.join(arr))
                arr[j] = tep
    return temp

def getdistance(Start, distance, nexts):  #获取每个arr距离start的最小距离
    distance[Start] = 0
    dq = deque()
    dq.append(Start)
    arrSet = set()
    arrSet.add(Start)
    while dq:
        temp = dq.popleft()
        for arr in nexts[temp]:
            if arr not in arrSet:
                arrSet.add(arr)
                dq.append(arr)
                distance[arr] = distance.get(temp) + 1

def printResult(cur, To, distance, nexts, solution, res):   #排版结果
    solution.append(cur)
    if cur == To:
        res.append(solution[:])
    else:
        for arr in nexts[cur]:
            if distance[arr] == distance[cur] + 1:
                printResult(arr, To, distance, nexts, solution, res)
    solution.pop()


Start = 'abc'
To = 'cab'
List = {'abc','cab','acc','cbc','ccc','cac','cbb','aab','abb'}  #把start加进去

FindMinPath(Start, To, List)
