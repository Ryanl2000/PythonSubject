class TrieNode:  #定义前缀树节点类
    def __init__(self) -> None:
        self.passed = 0
        self.end = 0
        self.nexts = {}
    
class Trie:  #前缀树
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):  #插入字符
        if not word:
            return
        chs = list(word)
        node = self.root
        node.passed += 1
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            if not node.nexts.get(index):
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            node.passed += 1
        node.end += 1

    def search(self, word):  #查询word的出现次数
        if not word:
            return
        chs = list(word)
        node = self.root
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            if not node.nexts.get(index):
                return 0
            node = node.nexts[index]
        return node.end
    
    def prefixNumber(self, word):  #查询word前缀出现的次数
        if not word:
            return
        chs = list(word)
        node = self.root
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            if not node.nexts.get(index):
                return 0
            node = node.nexts[index]
        return node.passed

    def delete(self, word):  #删除word
        if self.search(word) == 0:
            print('未出现该word！')
            return
        chs = list(word)
        node = self.root
        node.passed -= 1
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            if node.nexts[index].passed == 1:
                del node.nexts[index]
                return
            node = node.nexts[index]
            node.passed -= 1
        node.end -= 1

s = 'dexf'
s1 = 'dexd'
t = Trie()
t.insert(s)
t.insert(s1)
print(t.search('dexf'))
print(t.prefixNumber('dex'))
t.delete('dexf')
print(t.search('dexf'))
print(t.search('dexd'))
t.delete('dexf')