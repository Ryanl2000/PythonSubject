import Morris
from Node import TreeNode

list = [1,2,3,4,5,6,7,8]
root = TreeNode()
root.addByList(list)
# Morris.MorrisBack(root.root)
list2 = [2,1,None,None,None]
root2 = TreeNode()
root2.Create(list2)
#print(Morris.isBST(root2.root))
#Morris.MorrisPre(root2.root)
print(Morris.isBST(root2.root))