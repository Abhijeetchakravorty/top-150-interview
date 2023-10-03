# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time Complexity : O(N)
    # Space Complexity: O(2^log n) or O(n)
    def levelOrder(self, node) -> [[int]]:
        # Initialize an empty queue for 
        # breadth-first traversal and a 
        # list to store the result.
        queue = []
        result = []
        
        # Initialize a temporary 
        # list to store values at the current level.
        temp = []
        
        # Check if the input node 
        # is not None (the tree is not empty).
        if (node != None):
            queue.append(node)  # Enqueue the root node.
            queue.append('X')  # Use 'X' as a marker to indicate the end of the current level.
        
        # Perform breadth-first traversal.
        while (len(queue) > 0):
            head = queue.pop(0)  # Dequeue the front node from the queue.
            
            if (head == 'X'):
                # If the marker 'X' is encountered, it means the current level is complete.
                result.append(temp)  # Add the values at the current level to the result list.
                
                # Check if there are more nodes in the queue (more levels to process).
                if(len(queue) > 0):
                    queue.append('X')  # Enqueue a marker for the next level.
                    temp = []  # Reset the temporary list for the next level.
            else:
                # If a regular node is encountered, add its value to the temporary list.
                temp.append(head.val)
                
                # Enqueue the left and right child nodes if they exist.
                if(head.left != None):
                    queue.append(head.left)
                if(head.right != None):
                    queue.append(head.right)
        
        return result  # Return the result, which is a list of lists representing levels of the binary tree.
