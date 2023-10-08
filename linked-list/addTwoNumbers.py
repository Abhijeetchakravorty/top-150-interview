# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Time Complexity : O(max(m, n)) 
    # Space Complexity: O(max(m, n)) 
    def addTwoNumbers(self, l1, l2):
        result_tail = ListNode()
        result = result_tail
        carry = 0

        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # new digit
            totalsum = val1 + val2 + carry
            carry = totalsum // 10
            totalsum = totalsum % 10
            result.next = ListNode(totalsum)

            # update pointers
            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result_tail.next
