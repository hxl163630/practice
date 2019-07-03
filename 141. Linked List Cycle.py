# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head and head.next and head.next.next:
            if head.next == head.next.next:
                return True
            else:
                head = head.next
        return False

head = ListNode(3)
head.next = ListNode(4)
head.next.next = head
sol = Solution()
print(sol.hasCycle(head))