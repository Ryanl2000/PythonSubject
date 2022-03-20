class solution:  #桶排序
    def __init__(self, list) -> None:
        self.list = list
        self.maxs = self.maxdigits()

    def maxdigits(self):
        maxs = 0
        for i in self.list:
            maxs = max(maxs, len(str(i)))
        return maxs
    
    def transf(self):
        for i in range(len(self.list)):
            self.list[i] = (self.maxs - len(str(self.list[i]))) * '0' + str(self.list[i])
    
    def bucketSort(self):
        self.transf()
        help = self.list
        for i in range(self.maxs - 1, -1, -1):
            count = [0] * 10
            helpcopy = []
            for j in help:
                count[int(j[i])] += 1
            for k in range(1,10):
                count[k] += count[k-1]
            for j in help:
                helpcopy.append(j)
            for j in helpcopy[::-1]:
                help[count[int(j[i])]-1] = j
                count[int(j[i])] -= 1
        for i in range(len(help)):
            help[i] = int(help[i])
        return help

if __name__ == '__main__':
    list = [101,98,65,15,2]
    s = solution(list)
    s.bucketSort()
    print(s.list)
