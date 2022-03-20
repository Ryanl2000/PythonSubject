from queue import Queue
def largestWidth(root) -> int:
    q = Queue()
    q.put(root)
    curdepth = 1
    curnum = 0
    listdepth = {}
    listdepth[root] = 1
    maxs = float('-inf')
    while not q.empty():
        node = q.get()
        leveldepth = listdepth.get(node)
        if leveldepth == curdepth:
            curnum += 1
        else:
            maxs = max(maxs, curnum)
            curdepth += 1
            curnum = 1
        if node.left:
            listdepth[node.left] = leveldepth + 1
            q.put(node.left)
        if node.right:
            listdepth[node.right] = leveldepth + 1
            q.put(node.right)
    maxs = max(maxs, curnum)
    return maxs