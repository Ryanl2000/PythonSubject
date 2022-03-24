#二叉树与多叉树
from collections import deque


class Node:  #节点
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
class TreeNode:  #二叉树
    def __init__(self) -> None:
        self.root = None

    def add(self, item):  #增加节点
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
    
    def addByList(self, list):  #以列表形式增加节点
        for i in list:
            self.add(i)

class TreeNodeMany:
    pass
# tr = TreeNode()
# list = [1,2,3,4,5,6,7,8]
# tr.addByList(list)


