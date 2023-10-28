# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Time Complexity :  O(n)
    # Space Complexity: O(1)
    def removeNthFromEnd(self, head, n: int):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        print("fast val", fast.val)
        slow.next = slow.next.next
        return head

    def printList(self, head):
        while head:
            print(head.val)
            head = head.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

a = Solution()
b = a.removeNthFromEnd(head, 3)
a.printList(b)
