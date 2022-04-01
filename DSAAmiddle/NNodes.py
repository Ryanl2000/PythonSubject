#N个节点的树结构数量
def NNodes(n):  #基础枚举
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    res = 0
    for left in range(n):
        leftWay = NNodes(left)
        rightWay = NNodes(n-left-1)
        res += leftWay * rightWay
    return res

def NNodesUltar(n):  #动态规划
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]

def compare():  #对数器
    for i in range(15):
        if NNodes(i) != NNodesUltar(i):
            return False
    return True

print(compare())
# print(NNodes(5))
# print(NNodesUltar(5))
