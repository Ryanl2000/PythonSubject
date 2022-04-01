# 流算法
# 实时添加字符串，并可以实时返回topK个字符串
class Bucket:  # 封装str和str出现的次数
    def __init__(self, str=None, times=None) -> None:  
        self.str = str
        self.times = times

class Online:
    def __init__(self, k) -> None:
        self.k = k  #topK值
        self.frequency = {}  #词频表
        self.myHeap = []  #topK堆
        self.heapindex = {}  #堆中str的位置表
        self.heapsize = 0  #堆大小

    def swap(self, l, r):
        self.heapindex[self.myHeap[l]] = r  #位置表同步更新
        self.heapindex[self.myHeap[r]] = l
        temp = self.myHeap[l]
        self.myHeap[l] = self.myHeap[r]
        self.myHeap[r] = temp
        
    def heapInsert(self, cur):
        if self.heapsize == 0:
            self.myHeap.append(cur)
            self.heapsize += 1
            return
        
        index = self.heapsize
        self.myHeap.append(cur)
        self.heapsize += 1
        while self.myHeap[index].times < self.myHeap[abs(index - 1) // 2].times:
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def heapfiy(self, index):
        left = index * 2 + 1
        while left < self.heapsize:
            if left + 1 < self.heapsize and self.myHeap[left] > self.myHeap[left+1]:
                little = left + 1
            else:
                little = left
            little = little if self.myHeap[little].times < self.myHeap[index].times else index
            if little == index:
                break
            self.swap(little, index)
            index = little
            left = index * 2 + 1

    def add(self, str):  #添加字符
        preIndex = -1
        if str not in self.frequency:  #判断是不是第一次出现的字符
            cur = Bucket(str, 1)
            self.frequency[str] = cur
            self.heapindex[cur] = -1
        else:
            cur = self.frequency[str]
            cur.times += 1
            preIndex = self.heapindex[cur]
        if preIndex == -1:
            if self.heapsize == self.k:
                if self.myHeap[0].times < cur.times:
                    self.heapindex[self.myHeap[0]] = -1
                    self.heapindex[cur] = 0
                    self.myHeap[0] = cur
                    self.heapfiy(0)
            else:
                self.heapindex[cur] = self.heapsize
                self.heapInsert(cur)
        else:
            self.heapfiy(preIndex)
        # self.printTopK()

    def printTopK(self):
        for i in range(len(self.myHeap)-1, -1, -1):
            print(self.myHeap[i].str)

test = Online(2)

test.add('a')
test.add('b')
test.add('c')
test.add('a')

