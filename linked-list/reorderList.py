# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = None
class Solution:
    # Time Complexity : O(n)
    # Space Complexity: O(1)
    def reorderList(self, head):
        if not head:
            return None
        
        # find middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        # reverse second half of list
        previous = None
        current = slow.next
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        # separate the two halves
        slow.next = None

        # merge the two halves
        
        first = head
        second = previous
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2 


            
            
        


a = Solution()
b = a.reorderList([1,2,3,4,5])
print("Ans: ", b)