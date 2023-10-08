class Solution:
    # Time Complexity : O(n)
    # Space Complexity: O(1)
    def reverseLinkedList(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
