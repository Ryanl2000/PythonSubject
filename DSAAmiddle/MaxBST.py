from Node import TreeNode
# MaxheadBST：最大搜索二叉树的头节点
# isBST：是否为搜索树
# min：最小值
# max：最大值
# maxBSTsize：最大搜索二叉树的大小
def process(root):
    if not root:
        return (None, True, float('inf'), float('-inf'), 0)
        
    leftInfo = process(root.left)
    rightInfo = process(root.right)

    mi = min(leftInfo[2], rightInfo[2], root.val)
    ma = max(leftInfo[3], rightInfo[3], root.val)
    isBST = True if leftInfo[3] < root.val < rightInfo[2] and leftInfo[1] and rightInfo[1] else False
    if isBST:
        head = root
        BSTNum = leftInfo[4] + rightInfo[4] + 1
    elif leftInfo[4] > rightInfo[4]:
        head = leftInfo[0]
        BSTNum = leftInfo[4]
    else:
        head = rightInfo[0]
        BSTNum = rightInfo[4]
    return (head, isBST, mi, ma, BSTNum)


m = TreeNode()
list = [3,1,None,4,None,None,None] 
m.Create(list)

print(process(m.root))