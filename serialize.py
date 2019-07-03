# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root: return None
    queue = deque([root])
    res = deque()
    while len(queue):
        node = queue.popleft()
        if not node:
            res.append("null")
            continue
        res.append(str(node.val))
        queue.append(node.left)
        queue.append(node.right)
    while res[-1] == "null":
        res.pop()
    return ",".join(res)

def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if not data: return None
    nodeval = deque(data.split(","))
    queue = deque([TreeNode(int(nodeval.popleft()))])
    root = queue[0]
    curleft = False
    while nodeval:
        node = queue[0]
        if not curleft:
            val = nodeval.popleft()
            if val != "null":
                node.left = TreeNode(int(val))
                queue.append(node.left)
            curleft = True
        elif nodeval:
            val = nodeval.popleft()
            if val != "null":
                node.right = TreeNode(int(val))
                queue.append(node.right)
            curleft = False
            queue.popleft()
    return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))