# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preIndex = 0
        self.inIndex = 0

        def helper(preorder, inorder, insuccessor):
            if (self.inIndex >= len(inorder) or inorder[self.inIndex] == insuccessor):
                return None
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1
            root.left = helper(preorder, inorder, root.val)
            self.inIndex += 1
            root.right = helper(preorder, inorder, insuccessor)
            return root



        return helper(preorder, inorder, float('-inf'))

import printTree
sol = Solution()
print(printTree.treeNodeToString(sol.buildTree([3,9,20,15,7], [9,3,15,20,7])))