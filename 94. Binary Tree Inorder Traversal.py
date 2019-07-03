# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack = []
        while root is not None or len(stack):
            if not root:
                root = stack.pop()
                output.append(root.val)
                root = root.right
            elif root.left:
                stack.append(root)
                root = root.left
            else:
                output.append(root.val)
                root = root.right
        return output

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
sol = Solution()
sol.inorderTraversal(root)