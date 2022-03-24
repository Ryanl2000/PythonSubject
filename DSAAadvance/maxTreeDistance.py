#二叉树最长距离
def maxDistance(root):
    if not root:
        return (0, 0)  #高度和最大值
    leftTree = maxDistance(root.left)
    rightTree = maxDistance(root.right)
    leftmax = leftTree[1]
    rightmax = rightTree[1]
    heightmax = leftTree[0] + rightTree[0] + 1
    maxd = max(leftmax, rightmax, heightmax)
    height = max(leftTree[0], rightTree[0]) + 1
    return (height, maxd)

#快乐值(多叉树)
def maxHappy(root):
    if not root.next:
        return (root.happy, 0)
    yes = root.happy  #当前节点来
    no = 0  #当前节点不来
    for next in root.next:
        nextInfo = maxHappy(next)
        yes += nextInfo[1]  #如果父节点来，那么子节点不能来
        no += max(nextInfo[0], nextInfo[1])  #如果父节点不来，字节点可以选择来或者不来
    return (yes, no)

    