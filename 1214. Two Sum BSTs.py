# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, object):
        return self.val

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False

        st1 = []
        st2 = []

        while True:
            while root1:
                st1.append(root1)
                root1 = root1.left
            while root2:
                st2.append(root2)
                root2 = root2.right

            if not st1 or not st2:
                return False

            root1 = st1[-1]
            root2 = st2[-1]

            if root1.val + root2.val == target:
                return True
            elif root1.val + root2.val < target:
                st1.pop()
                root1 = root1.right
            else:
                st2.pop()
                root2 = root2.left

root1 = TreeNode(5)
root1.left = TreeNode(-1)
root1.left.left = TreeNode(-2)
root1.left.left.left = TreeNode(-6)
root1.right = TreeNode(6)

root2 = TreeNode(-7)
root2.right = TreeNode(1)


sol = Solution()
print(sol.twoSumBSTs(root1, root2, -4))