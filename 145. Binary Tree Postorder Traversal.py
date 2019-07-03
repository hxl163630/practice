# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack = [root]
        prev = root
        while len(stack):
            root = stack.pop()
            if (root.left is None and root.right is None) or (root.right is None and root.left == prev) or (root.right == prev):
                output.append(root.val)
                prev = root
            else:
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
        return output

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
sol = Solution()
sol.postorderTraversal(root)