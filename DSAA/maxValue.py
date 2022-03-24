# 在限定载重的背包情况下的最大价值
def maxValue(weight, value, i, bag, alreadyWeight):
    if alreadyWeight > bag:
        return -value[i-1]
    if i == len(weight):
        return 0
    return max(
        maxValue(weight, value, i + 1, bag, alreadyWeight),
        value[i] + maxValue(weight, value, i + 1, bag,
                            alreadyWeight + weight[i])
    )


# 方法二
def maxValue2(weight, value, i, bag, alreadyWeight, alreadyValue):
    if alreadyWeight > bag:
        return -0
    if i == len(weight):
        return alreadyValue
    return max(
        maxValue2(weight, value, i + 1, bag, alreadyWeight, alreadyValue),
        maxValue2(weight, value, i + 1, bag, alreadyWeight +
                  weight[i], alreadyValue + values[i])
    )


weights = [4, 2, 3, 5]
values = [7, 8, 6, 2]
bag = 5

print(maxValue(weights, values, 0, bag, 0))
print(maxValue2(weights, values, 0, bag, 0, 0))