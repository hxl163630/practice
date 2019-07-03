# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import serialize


class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root or k == 0:  return []
        upperstack = self.getpath(root, target)
        lowerstack = upperstack[:]
        if lowerstack[-1].val < target:
            self.moveupper(upperstack)
        else:
            self.movelower(lowerstack)

        res = []
        for i in range(k):
            if self.loweriscloser(lowerstack, upperstack, target):
                res.append(lowerstack[-1])
                self.movelower(lowerstack)
            else:
                res.append(upperstack[-1])
                self.moveupper(upperstack)

        return res

    def movelower(self, lower):
        if lower[-1].left:
            node = lower[-1].left
            while node:
                lower.append(node)
                node = node.right
        else:
            node = lower.pop()
            while lower and lower[-1].left == node:
                node = lower.pop()

    def moveupper(self, upper):
        if upper[-1].left:
            node = upper[-1].left
            while node:
                upper.append(node)
                node = node.right
        else:
            node = upper.pop()
            while upper and upper[-1].left == node:
                node = upper.pop()

    def loweriscloser(self, upper, lower, target):
        if not upper: return True
        if not lower: return False
        return upper[-1].val - target > target - lower[-1].val

    def getpath(self, node, target):
        path = []
        while node:
            path.append(node)
            if node.val > target:
                node = node.left
            elif node.val < target:
                node = node.right
            else:
                break
        return path

root = serialize.deserialize("4,2,5,1,3")
sol = Solution()
sol.closestKValues(root, 3.75,2)