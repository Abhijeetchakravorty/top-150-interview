class ListNode:
        def __init__(self, val):
                self.val = val
                self.next = None
class Solution:
        def mergeSortedList(self, l1, l2):
                out = head = ListNode()
                while l1 and l2:
                        if l1.val < l2.val:
                                head.next = l1
                                l1=l1.next
                        else:
                                head.next = l2
                                l2=l2.next
                        head = head.next
                head.next = l1 or l2
                return out.next