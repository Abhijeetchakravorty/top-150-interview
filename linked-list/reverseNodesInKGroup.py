# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # This function reverses nodes in k-group within a singly-linked list.
    # Time Complexity: O(N) where N is the number of nodes in the linked list.
    # Space Complexity: O(1) as it uses a constant amount of extra space.
    def reverseKGroup(self, head, k: int):
        # Create a dummy node and make it the new head.
        dummy = ListNode(0, head)
        groupPrev = dummy  # Initialize the group's previous node as the dummy node.

        while True:
            # Find the kth node in the current group or None if there aren't enough nodes.
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break  # If there are not enough nodes, break the loop.

            groupNext = kth.next  # Store the next node after the current group.
            prev, cur = kth.next, groupPrev.next  # Initialize pointers for reversing the group.

            while cur != groupNext:
                nxt = cur.next  # Store the next node to avoid losing the reference.
                cur.next = prev  # Reverse the current node's next pointer.
                prev = cur
                cur = nxt

            temp = groupPrev.next  # Store the start of the group before reversing.
            groupPrev.next = kth  # Connect the previous group's end to the new group's start.
            groupPrev = temp  # Move the groupPrev pointer to the end of the previous group.

        return dummy.next  # Return the modified linked list.

    # Helper function to find the kth node from the current position.
    def getKthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur  # Return the kth node or None if not enough nodes.
