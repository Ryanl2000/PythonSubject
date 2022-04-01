#下雨接水问题
height = [0,1,0,2,1,0,1,3,2,1,2,1]
def rain1(height):  #类似于洗衣机问题（时间较长）
    dp = [0] * len(height)
    for i in range(1,len(height)-1):
        leftmax = max(height[0:i])
        rightmax = max(height[i+1:])
        dp[i] = min(leftmax, rightmax) - height[i] if min(leftmax, rightmax) - height[i] >= 0 else 0
    res = 0
    for i in range(len(dp)):
        res += dp[i]
    return res


def rain2(height):  #双指针
    maxleft = height[0]
    maxright = height[-1]
    left = 1
    right = len(height) - 2
    res = 0
    while left <= right:
        if height[left] > maxleft:
            maxleft = height[left]
            left += 1
            continue
        if height[right] > maxright:
            maxright = height[right]
            right -= 1
            continue
        if maxleft > maxright:
            res += maxright - height[right]
            right -= 1
        else:
            res += maxleft - height[left]
            left += 1
    return res

print(rain2(height))