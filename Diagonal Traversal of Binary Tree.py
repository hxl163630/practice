import printTree

def diagTrav(node):
    if not node:
        return []
    res = []
    from collections import deque
    curLevel = deque([node])
    while curLevel:
        size = len(curLevel)
        tmp = []
        for i in range(size):
            cur = curLevel.popleft()
            while cur:
                tmp.append(cur.val)
                if cur.left:
                    curLevel.append(cur.left)
                cur = cur.right
        res.append(tmp)
    print(res)
    return res

root = printTree.stringToTreeNode("[1,3,null,null,2,3,4,55,436,4,null,null,234,43]")

diagTrav(root)
