# 人气到达目的值最少的钱数
# 点赞，a钱，+2人气
# 送礼，b钱，*2人气
# 私聊，c钱，-2人气
# 人气为偶数
import pandas


def Popularity(start, aim, a, b, c, premoney, cur):
    #初始人气、目标人气、a、b、c、当前花费、当前人气
    if cur < 0 or cur > aim * 2:
        return float('inf')
    if premoney > ((aim - start) // 2) * a:
        return float('inf')
    if cur == aim:
        return premoney
    return min(Popularity(start, aim, a, b, c, premoney + a, cur + 2),
               Popularity(start, aim, a, b, c, premoney + b, cur * 2),
               Popularity(start, aim, a, b, c, premoney + c, cur - 2))


def PopularityUltar(start, aim, a, b, c):  # 动态规划（较难）
    limitPre = ((aim - start) // 2) * a + 1
    limitCur = aim * 2 + 1
    dp = [[0 for _ in range(limitCur)] for _ in range(limitPre)]
    for i in range(limitPre):
        for j in range(limitCur):
            if j == start:
                dp[i][j] = i
            else:
                dp[i][j] = float('inf')
    for pre in range(limitPre-1, -1, -1):
        for aim in range(limitCur):
            if aim - 2 >= 0 and pre + a < limitPre:
                dp[pre][aim] = min(dp[pre][aim], dp[pre + a][aim - 2])
            if aim + 2 < limitCur and pre + c < limitPre:
                dp[pre][aim] = min(dp[pre][aim], dp[pre + c][aim + 2])
            if aim & 1 == 0:
                if aim // 2 >= 0 and pre + b < limitPre:
                    dp[pre][aim] = min(dp[pre][aim], dp[pre + b][aim // 2])
    return dp




# print(Popularity(6, 10, 5, 6, 2, 0, 6))
dp = PopularityUltar(6, 10, 5, 6, 2)
print(dp[0][10])
dp = pandas.DataFrame(dp)
print(dp)
