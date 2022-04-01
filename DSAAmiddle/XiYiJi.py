#洗衣机扔衣服问题
def process(arr):
    asum = 0
    for i in arr:
        asum += i
    if asum % len(arr) != 0:
        return -1
    avg = asum // len(arr)
    dp = [0 for _ in range(len(arr))]
    dp2 = []
    for index in range(len(arr)):
        dp1 = 0 if index == 0 else - dp2[index-1]
        dp2.append(avg - dp1 - arr[index])
        if dp1 < 0 and dp2[index] < 0:
            dp[index] = abs(dp1 + dp2[index])
        else:
            dp[index] = max(dp1, dp2[index])
    return max(dp)

arr = [0,6,0]
print(process(arr))