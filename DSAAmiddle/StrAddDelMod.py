# 字符串通过增、删、改变成另外一个字符串
# 增删改的代价均不同
# 编辑距离问题
def StrAddDelMod(str1, str2, add, delete, modify):  #经典dp表
    dp = [[-1 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    dp[0][0] = 0
    for i in range(1, len(str2) + 1):
        dp[0][i] = i * add
    for i in range(1, len(str1) + 1):
        dp[i][0] = i * delete
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1] + add, dp[i-1][j] + delete, dp[i-1][j-1] + modify)
    return dp[len(str1)][len(str2)]

str1 = 'abcde'
str2 = 'adcef'
print(StrAddDelMod(str1,str2,1,2,3))