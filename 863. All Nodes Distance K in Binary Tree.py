# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.path = []

        def dfs(node, curPath, target):
            if not node:
                return
            curPath.append(node)

            if node.val == target.val:
                self.path = list(curPath)
                return

            dfs(node.left, curPath, target)
            dfs(node.right, curPath, target)
            curPath.pop()

        dfs(root, [],  target)

        if not self.path:
            return []

        res = []
        if target.left:
            if target.left.left:
                res.append(target.left.left.val)
            if target.left.right:
                res.append(target.left.right.val)
            if target.right.left:
                res.append(target.right.left.val)
            if target.right.right:
                res.append(target.right.right.val)

        if len(self.path) == 1:
            return res
        elif len(self.path) == 2:
            self.path.pop()
            node = self.path.pop()
            if node.left == target:
                if node.right:
                    res.append(node.right.val)
            if node.right == target:
                if node.left:
                    res.append(node.left.val)
        else:
            res.append(self.path[-3].val)
        return res

import printTree

sol = Solution()
root = printTree.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
target = TreeNode(5)

sol.distanceK(root, target, 2)