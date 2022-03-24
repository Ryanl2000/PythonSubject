class solution:  #大根堆
    def __init__(self) -> None:
        self.heaplist = []
        self.heapsize = 0

    def swap(self, l, r):
        temp = self.heaplist[l]
        self.heaplist[l] = self.heaplist[r]
        self.heaplist[r] = temp

    def heapInsert(self, num):
        if self.heapsize == 0:
            self.heaplist.append(num)
            self.heapsize += 1
            return
        
        index = self.heapsize
        self.heaplist.append(num)
        self.heapsize += 1
        while self.heaplist[index] > self.heaplist[abs(index - 1) // 2]:
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2
    
    def heapify(self, index):  #在index位置上还能不能往下走
        left = index * 2 + 1
        while left < self.heapsize:
            if left + 1 < self.heapsize and self.heaplist[left] < self.heaplist[left+1]:
                largest = left + 1
            else:
                largest = left
            largest = largest if self.heaplist[largest] > self.heaplist[index] else index
            if largest == index:
                break
            self.swap(largest, index)
            index = largest
            left = index * 2 + 1

    def heapout(self):  #删除最大值，并进行heapify
        self.heaplist[0] = self.heaplist.pop()
        self.heapsize -= 1
        self.heapify(0)

    def heapInsertBylist(self,list):
        for i in list:
            self.heapInsert(i)

    def heapSort(self):  #堆排序
        while self.heapsize > 0:
            self.swap(0, self.heapsize - 1)
            self.heapsize -= 1
            self.heapify(0)
        return self.heaplist

    
if __name__ == '__main__':
    s = solution()
    l = [3, 4, 6, 7, 1, 2, 9]
    s.heapInsertBylist(l)
    s.heapSort()
    print(s.heaplist)
    print(s.heapsize)