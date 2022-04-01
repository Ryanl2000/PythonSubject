# 数字转换字符串
def StrTransf(num, index):  #递归
    if index == len(num):
        return 1
    if num[index] == '0':
        return 0
    if num[index] == '1':
        res = StrTransf(num, index + 1)
        if index < len(num) - 1:
            res += StrTransf(num, index + 2)
        return res
    if num[index] == '2':
        res = StrTransf(num, index + 1)
        if index < len(num) - 1 and num[index+1] < '7':
            res += StrTransf(num, index + 2)
        return res
    return StrTransf(num, index + 1)

def StrTranfUltar(num):  #动态规划
    dp = [0] * (len(num) + 1)
    dp[len(num)] = 1
    dp[len(num) - 1] = 1 if num[-1] != '0' else 0
    for i in range(len(num) - 2, -1, -1):
        if num[i] == '0':
            dp[i] = 0
        elif num[i] == '1':
            pre = i + 2
            dp[i] = dp[pre]
        elif num[i] == '2':
            pre = i + 2
            dp[i] = dp[pre] if num[i+1] < '7' else 0
        dp[i] += dp[i+1]
    return dp[0]

num = '1225821'
print(StrTransf(num, 0))
print(StrTranfUltar(num))