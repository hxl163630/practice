# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        node, v = head, []
        while node is not None:
            v.append(node)
            node = node.next
        v.sort(key = lambda x: x.val)
        for i in range(len(v) - 1):
            v[i].next = v[i + 1]
        return v[0]


sol = Solution()
root = ListNode(4)
root.next = ListNode(2)
root.next.next = ListNode(1)
root.next.next.next = ListNode(3)

sol.sortList(root)
