# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        def findMid(Node):
            slow = Node
            fast = Node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            if not fast: return slow
            if not fast.next: return slow.next

        def reverseList(Node):
            prev = None
            curr = Node
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        if not head or not head.next or not head.next.next: return head
        midNode = findMid(head)
        revesedRightHalf = reverseList(midNode)

        dummy = ListNode(0)
        dummy.next = head
        while revesedRightHalf:
            tmp = head.next
            head.next = revesedRightHalf

            revesedRightHalf = revesedRightHalf.next
            head.next.next = tmp
            head = head.next.next
        head.next = None

        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

sol = Solution()
tmp = sol.reorderList(head)
print(tmp.val)


