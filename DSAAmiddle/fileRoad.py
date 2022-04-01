# 给定一系列文件路径，按照路劲的父子关系进行打印
class TrieTree:  #前缀节点
    def __init__(self) -> None:
        self.nexts = {}

class Trie:  #前缀树
    def __init__(self) -> None:
        self.root = TrieTree()

    def insert(self, road):  #插入路径
        if not road:
            return
        chs = road.split('\\')
        node = self.root
        for i in chs:
            if not node.nexts.get(i):
                node.nexts[i] = TrieTree()
            node = node.nexts[i]
        
    def printRoad(self, index, node):  #打印路径
        for key, value in node.nexts.items():
            print('  ' * index + key)
            if value.nexts:
                node = value
                self.printRoad(index + 1, node)
        
s = Trie()
s.insert('C:\\Deskop\\My')
s.insert('C:\\Public')
s.insert('C:\\Deskop\\All')
s.insert('D:\\ba')
s.printRoad(0,s.root)




