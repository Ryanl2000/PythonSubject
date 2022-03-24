#Manacher算法
class Manacher:
    def __init__(self) -> None:
        pass

    def strTransf(self, str):  #初始化字串，中间加#
        n = len(str)
        list = [0] * (2 * n + 1)
        m = 2 * n + 1
        for i in range(1, m, 2):
            list[i] = str[i//2]
        for i in range(0, m, 2):
            list[i] = '#'
        return ''.join(list)
    
    def manacherStringDiameter(self, str):  #自编，时间较长（maybe）
        R = -1
        C = -1
        str = self.strTransf(str)
        manacher = [0] * len(str)  #此处储存的是直径
        for i in range(len(str)):
            if i > R or i + (manacher[2 * C - i] >> 1) == R:
                manacher[i] = self.expansion(str, i)
                R = (manacher[i] >> 1) + i
                C = i
                i += 1
            elif i + (manacher[2 * C - i] >> 1) < R:
                manacher[i] = manacher[2 * C - i]
            else:
                manacher[i] = 2 * (R - C) + 1
        # newmanacher = []
        # for i in range(1, len(str), 2):
        #     newmanacher.append(manacher[i] >> 1)
        return (manacher, max(manacher) >> 1)  #返回列表和最长回文子串数量

    def expansion(self, str, strindex):  #暴力扩张
        x = 1
        left, right = strindex, strindex
        while left > 0 and right < len(str) - 1:
            if str[left-1] == str[right+1]:
                x += 2
                left -= 1
                right += 1
            else:
                return x
        return x

    def manacherStringRadius(self, str):  #在该函数中R为超越右边界+1的值
        R = -1
        C = -1
        str = self.strTransf(str)
        manacher = [0] * len(str)  #该处储存的是半径
        maxs = float('-inf')
        for i in range(len(str)):
            manacher[i] = 1 if i > R else min(manacher[2 * C - i], R - i)
            while i + manacher[i] < len(str) and i - manacher[i] > -1:  #不管什么条件都要尝试扩一次
                if str[i + manacher[i]] == str[i - manacher[i]]:
                    manacher[i] += 1
                else:
                    break
            if i + manacher[i] > R:
                R = i + manacher[i]
                C = i
            maxs = max(maxs, manacher[i])
        return (manacher, maxs - 1)



m = Manacher()
print(m.manacherStringDiameter('aa'))  #直径
print(m.manacherStringRadius('aa'))  #半径


