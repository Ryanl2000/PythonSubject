from random import randint

class solution:  #快速排序
    def __init__(self, arr) -> None:
        self.arr = arr

    def changeFlag(self, left, right):
        less = left - 1
        more = right
        while left < more:
            if self.arr[left] < self.arr[right]:
                self.swap(left, less + 1)
                left += 1
                less += 1
            elif self.arr[left] > self.arr[right]:
                self.swap(left, more - 1)
                more -= 1
            else:
                left += 1
        return [less, more]

    def quickSort(self, left, right):
        if left < right:
            self.swap(left + randint(0, right - left), right)
            help = self.changeFlag(left, right)
            self.quickSort(left, help[0])
            self.quickSort(help[1], right)

    def swap(self, l, r):
        t = self.arr[r]
        self.arr[r] = self.arr[l]
        self.arr[l] = t

if __name__ == '__main__':
    arr = [1,2,5,4,8,9,7,5,8,5]
    s = solution(arr)
    s.quickSort(0,len(arr)-1)
    print(s.arr)
    input()