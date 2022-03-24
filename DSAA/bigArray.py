class solution:  
    def __init__(self, list, res=None) -> None:
        self.l = list
        self.res = res

    def bigArray(self, left, right):
        if left == right:
            return []
        
        mid = left + ((right - left) >> 1)
        self.bigArray(left, mid)
        self.bigArray(mid + 1, right)
        self.res += self.merge(left, mid, right)
        return self.res
    
    def merge(self, left, mid, right):
        help = []
        i = left
        j = mid + 1
        temp = []
        while i <= mid and j <= right:
            if self.l[i] > self.l[j]:
                k = j
                while k <= right:
                    temp.append([self.l[i], self.l[k]])
                    k += 1
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
        for m in range(len(help)):
            self.l[left + m] = help[m]
        return temp

l = [3,2,1,5,0]
s = solution(l, [])
print(s.bigArray(0, len(l)-1))
