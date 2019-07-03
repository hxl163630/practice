# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                res.append("None")
                continue
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        # print(res)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        datalist = data.split(",")
        if datalist[0] == "None":
            return None
        root = TreeNode(datalist[0])
        cur = root
        stack = [root]
        i = 1
        while i < len(datalist):
            while i < len(datalist) and datalist[i] != "None":
                cur.left = TreeNode(datalist[i])
                cur = cur.left
                stack.append(cur)
                i += 1
            while i < len(datalist) and datalist[i] == "None":
                cur = stack.pop()
                i += 1
            if i < len(datalist):
                cur.right = TreeNode(datalist[i])
                cur = cur.right
                stack.append(cur)
                i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
codec.deserialize(codec.serialize(root))