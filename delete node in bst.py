# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        temp = root
        if not temp: return None
        while temp:
            if temp.val > key:
                temp = temp.left
            elif temp.val < key:
                temp = temp.right
            else:
                self.delete(temp)
                break
        return root

    def delete(self, node):
        if not node.left and not node.right: return None
        if not node.left: return node.right
        if not node.right: return node.left
        prev, pred = self.findpred(node)
        node.val = pred.val
        if prev.right == pred:
            prev.right = pred.right
        else:
            prev.left = pred.right
        return node

    def findpred(self, node):
        prev = node
        node = node.right
        while node.left:
            prev = node
            node = node.left
        return prev, node

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

sol = Solution()
sol.deleteNode(root, 3)