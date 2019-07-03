class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

dic = {}

def dfs(node):
    if not node.left and not node.right:
       dic[node.val] = [node.val]
       return [[node.val]]
    left = dfs(node.left)
    right = dfs(node.right)
    if node.val not in dic: dic[node.val] = []
    for item in left:
        dic[node.val].append([node.val]+item)
    for item in right:
        dic[node.val].append([node.val] + item)
    for item in left:
        for item1 in right:
            dic[node.val].append(item + item1)

    return dic[node.val]

dfs(root)
for i in dic.items():
    if(i[0] == 0):
        print(i[0])
        for j in i[1]:
            print(j)