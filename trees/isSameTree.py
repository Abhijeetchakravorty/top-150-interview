# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time Complexity : O(n)
    # Space Complexity: O(n)
    def isSameTree(self, p, q) -> bool:
        # Base case: If both trees are empty, they are considered the same.
        if not p and not q:
            return True

        # Check if both trees are non-empty and their root values are equal.
        if p and q and p.val == q.val:
            # Recursively check if the left and right subtrees are the same.
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            # If any of the conditions fail, the trees are not the same.
            return False