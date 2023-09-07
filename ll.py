class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thursday")
e5 = Node("Friday")
e6 = Node("Saturday")
e7 = Node("Sunday")
# Link first Node to second node
list1.headval.next = e2

# Link second Node to third node
e2.next = e3
e3.next = e4
e4.next = e5
e6.next = e7


def removeFromEnd(head, n):
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    
    if not fast:
        return head.next

    while fast.next:
        fast, slow = fast.next, slow.next
    
    # print("Before: ", slow.dataval)
    slow.next = slow.next.next
    # print("After: ", slow.dataval)

    return head

print(removeFromEnd(list1.headval, 4))