#完全二叉树节点个数
res = 0

def process(root):  #暴力解法（O(N)）
    global res
    if not root:
        return
    res += 1
    process(root.left)
    process(root.right)

def processUltar(root):  #暴力解法的升级版
    if not root:
        return 0
    return processUltar(root.left) + processUltar(root.right) + 1

def processUpdate(root):  #升级版方法（O(logN)**2）
    if not root:
        return 0
    def deep(root):
        if not root:
            return 0
        return deep(root.left) + 1
    res = 0
    def process(root):
        nonlocal res
        if not root.left and not root.right:
            res += 1
            return
        if deep(root.left) == deep(root.right):
            res += 1 << deep(root.left)
            process(root.right)
        else:
            res += 1 << deep(root.right)
            process(root.left)
    process(root)
    return res
