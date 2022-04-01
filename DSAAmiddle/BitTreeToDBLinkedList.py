# 二叉树转双向列表
class TreeNode:  #二叉树类
    def __init__(self, val=None) -> None:
        self.val = val
        self.left = None
        self.right = None

class DBlink:  #双向链表类
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

def BitTreeToDBlink(root):
    if not root:
        return DBlink(None, None)
    lefthead = BitTreeToDBlink(root.left)
    righthead = BitTreeToDBlink(root.right)
    if lefthead.end:
        lefthead.end.right = root
    root.left = lefthead.end
    root.right = righthead.start
    if righthead.start:
        righthead.start.left = root
    return DBlink(lefthead.start if lefthead.start != None else root,\
                  righthead.end if righthead.end != None else root)