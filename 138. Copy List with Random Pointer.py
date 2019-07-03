import copy
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
        print(self.data)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

def copyTree(node):

    if node is None:
        return

    node.left = copyTree(node.left)
    node.right =copyTree(node.right)

    newNode = Node(node.data)
    newNode.left = node.left
    newNode.right = node.right

    return newNode

newTree = copyTree(root)
print(newTree)