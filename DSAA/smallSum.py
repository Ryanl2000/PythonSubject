class solution:  #小和问题
    def __init__(self) -> None:
        self.l = [1,3,2,4,5]
    def recur(self, left, right):
        if left == right:
            return 0
        mid = left + ((right - left) >> 1)
        return self.recur(left, mid) + self.recur(mid + 1, right) + self.merge(left, mid, right)

    def merge(self, left, mid, right):
        help = []
        i = left
        j = mid + 1
        res = 0
        while i <= mid and j <= right:
            if self.l[i] < self.l[j]:
                res += self.l[i] * (right - j + 1)
                help.append(self.l[i])
                i += 1
            else:
                help.append(self.l[j])
                j += 1
        while i <= mid:
            help.append(self.l[i])
            i += 1
        while j <= right:
            help.append(self.l[j])
            j += 1
        for i in range(len(help)):
            self.l[i + left] =help[i] 
        return res

s = solution()
print(s.recur(0,4))