#并查集结构
class UnionFind:
    def __init__(self) -> None:
        self.elementMap = {}  # 记录插入的值
        self.FatherMap = {}  # 节点对应的父节点
        self.sizeMap = {}  # 代表节点所在的集合有几个点

    def Set(self, list):  #初始化并查集
        for value in list:
            self.elementMap[value] = value
            self.FatherMap[value] = value
            self.sizeMap[value] = 1

    def findHead(self, value):  #找到输入点的顶节点
        stack = []
        while value != self.FatherMap[value]:
            stack.append(value)
            value = self.FatherMap[value]
        while stack:  #扁平化优化操作：把途径的所有节点都指向顶节点
            self.FatherMap[stack.pop()] = value
        return value

    def isSameSet(self, a, b):  #是否为同一集合
        if self.elementMap.get(a) and self.elementMap.get(b):
            return self.findHead(self.elementMap.get(a)) == self.findHead(self.elementMap.get(b))
        return False

    def union(self, a, b):  #合并
        if self.elementMap.get(a) and self.elementMap.get(b):
            aF = self.findHead(self.elementMap.get(a))
            bF = self.findHead(self.elementMap.get(b))
            if aF != bF:
                big = aF if self.sizeMap.get(aF) >= self.sizeMap.get(bF) else bF
                small = bF if aF == big else aF
                self.FatherMap[small] = big
                self.sizeMap[big] = self.sizeMap.get(aF) + self.sizeMap.get(bF)
                del self.sizeMap[small]

list = ['a','b','d','c','f']
u = UnionFind()
u.Set(list)

print(u.elementMap.items())
print(u.FatherMap.items())
print(u.sizeMap.items())
print(u.isSameSet('a','d'))
u.union('a','d')
print(u.elementMap.items())
print(u.FatherMap.items())
print(u.sizeMap.items())
print(u.isSameSet('a','d'))

    
