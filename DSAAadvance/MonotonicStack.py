#单调栈
def MonotonicStack(n):  # 仅能用于处理不包含重复值(下面的#中的处理重复值方法待验证)
    stack = []
    res = {}
    i = 0
    while stack or i < len(n):
        if not stack:
            stack.append(i)
            res[i] = [-1]
            i += 1
            continue
        if i == len(n):
            while stack:
                temp = stack.pop()
                res[temp].append(-1)
            break
        temp = stack.pop()
        if n[i] < n[temp]:
            res[temp].append(i)
            continue
        elif n[i] > n[temp]:
            stack.append(temp)
            stack.append(i)
            res[i] = [temp]
        # else:  # 重复值
        #     stack.append(temp)
        #     stack.append(i)
        #     res[i] = [res[temp][0]]
        i += 1
    return res

def CumsumStack(n):  #对于n中每一个数字，返回包含本身，且本身为最小值的字数组累加和
    res = []
    for key, value in MonotonicStack(n).items():
        left, right = value[0] + 1, value[1] - 1
        if value[1] == -1:
            right = len(n) - 1
        sum = 0
        for i in range(left, right + 1):
            sum += n[i]
        res.append((key,sum * n[key]))
    return res

n = [5, 3, 2, 1, 6, 7, 8, 4]
# mmdict = MonotonicStack(n)
# print(mmdict)
print(CumsumStack(n))

