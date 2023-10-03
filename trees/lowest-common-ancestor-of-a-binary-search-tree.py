# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time Complexity : O(h) 
    # Space Complexity: O(1)
    def lowestCommonAncestor(self, root, p, q):
        while True:
            # Check if the current root value is less than both p and q values.
            if root.val < p.val and root.val < q.val:
                root = root.right  # Move to the right subtree because both p and q are greater.
            
            # Check if the current root value is greater than both p and q values.
            elif root.val > p.val and root.val > q.val:
                root = root.left  # Move to the left subtree because both p and q are smaller.
            
            else:
                # If neither of the above conditions is met, it means the current root value
                # is between p and q, or it is equal to either p or q, making it the lowest common ancestor.
                return root  # Return the current root as the lowest common ancestor.
