# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return
        if root.val > key:
            self.deleteNode(root.left, key)
        elif root.val < key:
            self.deleteNode(root.right, key)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            prevpred = root
            pred = root.left
            while pred.right:
                prevpred = pred
                pred = pred.right
            root.val, pred.val = pred.val, root.val
            prevpred.left = self.deleteNode(pred, key)
        return root

import serialize
root = serialize.deserialize("5,3,6,2,4,null,7")
sol = Solution()
sol.deleteNode(root, 3)