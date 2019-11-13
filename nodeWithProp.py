import printTree

def getNode(node, res):
    if not node:
        return None
    left = getNode(node.left, res)
    right = getNode(node.right, res)
    if node.val == 1:
        node.left = left
        node.right = right
        return node

    if left and right:
        res.append(left)
        res.append(right)
        return None
    if left:
        return left
    if right:
        return right
    return None

root = printTree.stringToTreeNode("[1,1,2,2,1,1,1]")
res = []
if root and root.val == 1:
    res.append(root)
getNode(root, res)

for i in res:
    print(printTree.treeNodeToString(i))
