#Morris遍历
#时间复杂度N，空间复杂度1
from Node import Node

def Morris(root):  #Morris源代码
    if not root:
        return
    mostRight = Node()  # 最右节点
    while root:
        mostRight = root.left
        if mostRight:
            while mostRight.right and mostRight.right != root:
                mostRight = mostRight.right
            if not mostRight.right:
                mostRight.right = root
                root = root.left
                continue
            else:  # mostRight.right == root
                mostRight.right = None
                #root = root.right和下面重合
        root = root.right


def MorrisPre(root):  # Morris先序遍历
    if not root:
        return
    mostRight = Node()  # 最右节点
    while root:
        mostRight = root.left
        if mostRight:
            while mostRight.right and mostRight.right != root:
                mostRight = mostRight.right
            if not mostRight.right:  # 第一次来到左子树
                print(root.val,end=',')
                mostRight.right = root
                root = root.left
                continue
            else:  # mostRight.right == root
                mostRight.right = None
                #root = root.right和下面重合
        else:
            print(root.val,end=',')  # 没有左数的只遍历一次
        root = root.right


def MorrisMid(root):  # Morris中序遍历
    if not root:
        return
    mostRight = Node()  # 最右节点
    while root:
        mostRight = root.left
        if mostRight:
            while mostRight.right and mostRight.right != root:
                mostRight = mostRight.right
            if not mostRight.right:
                mostRight.right = root
                root = root.left
                continue
            else:  # mostRight.right == root
                mostRight.right = None
                #root = root.right和下面重合
        print(root.val,end=',')  # 没有左子树的，以及第二次来到左子树
        root = root.right


def MorrisBack(root):  # Morris后序遍历：第二次到达左子树时，逆序打印该树的左子树右边界
    if not root:
        return
    cur = root
    mostRight = Node()  # 最右节点
    while cur:
        mostRight = cur.left
        if mostRight:
            while mostRight.right and mostRight.right != cur:
                mostRight = mostRight.right
            if not mostRight.right:
                mostRight.right = cur
                cur = cur.left
                continue
            else:  # mostRight.right == cur
                mostRight.right = None
                printEdge(cur.left)  # 打印第二次来到左子树时，左子树上所有右数的逆序
                #cur = cur.right和下面重合
        cur = cur.right
    printEdge(root)  # 遍历结束后，返回整个逆序右边界


def printEdge(node):  # 逆序打印当前节点的全部右子树
    tail = reverseEdge(node)
    while tail:
        print(tail.val,end=',')
        tail = tail.right
    reverseEdge(tail)


def reverseEdge(node):  # 反转右子树的指针（辅助printEdge函数）
    pre = None
    next = None
    while node:
        next = node.right
        node.right = pre
        pre = node
        node = next
    return pre

#Morris遍历的延申
def isBST(root):  #Morris判断搜索二叉树
    if not root:
        return
    mostRight = Node()  # 最右节点
    preValue = float('-inf')
    while root:
        mostRight = root.left
        if mostRight:
            while mostRight.right and mostRight.right != root:
                mostRight = mostRight.right
            if not mostRight.right:
                mostRight.right = root
                root = root.left
                continue
            else:  # mostRight.right == root
                mostRight.right = None
                #root = root.right和下面重合
        if root.val < preValue:
            return False
        preValue = root.val
        root = root.right
    return True