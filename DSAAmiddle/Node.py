#二叉树与多叉树
from collections import deque


class Node:  #节点
    def __init__(self, val=None) -> None:
        self.val = val
        self.left = None
        self.right = None
    
class TreeNode:  #二叉树
    def __init__(self) -> None:
        self.root = None

    def add(self, item):  #增加节点（仅适用于无空值树）
        if item == None:
            node = Node()
        else:
            node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            cur_node = queue.popleft()
            if not cur_node.left:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)
    
    def addByList(self, list):  #以列表形式增加节点（仅适用于无空值树）
        for i in list:
            self.add(i)
    
    def process(self, root, val):  
        if len(val) == 0:
            return root
        if val[0]:
            root = Node(val[0])
            val.pop(0)
            root.left = self.process(root.left, val)
            root.right = self.process(root.right, val)
            return root
        else:
            root = None
            val.pop(0)
            return root

    def Create(self, list):#可用于有空值的树，但必须输入时用None代替空，按照前序遍历输入（叶子节点下的空也算）
        self.root = self.process(None, list)


class TreeNodeMany:
    pass
# tr = TreeNode()
# list = [1,2,3,4,5,6,7,8]
# tr.addByList(list)


