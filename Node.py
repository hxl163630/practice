class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "val: " + str(self.val) + " left val: " + (str(self.left.val) if self.left else "None") + " right val: " + (str(self.right.val) if self.right else "None")
