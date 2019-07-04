from Node import *

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0

        def helper(node, target):
            if not node: return 0
            left = helper(node.left, target - node.val)
            right = helper(node.right, target - node.val)
            return (node.val == target) + left + right

        return helper(root, sum) + helper(root.left, sum) + helper(root.right, sum)


sol = Solution()
root = stringToTreeNode("[1,null,2,null,3,null,4,null,5]")
print(sol.pathSum(root, 3))