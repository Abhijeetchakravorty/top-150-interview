# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity can be improved to O(n+m)
class Solution:
    # Time Complexity : O(s*t)  
    # Space Complexity: O(s)
    def isSubtree(self, s, t) -> bool:
        # Base case: If t is an empty tree, 
        # it's considered a subtree of any tree.
        if not t:
            return True
        # If s is empty but t is not, t cannot be a subtree.
        if not s:
            return False

        # Check if the current s and t trees are the same. 
        # If they are, t is a subtree of s.
        if self.sameTree(s, t):
            return True

        # Recursively check if t is a subtree of s's left or right subtree.
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        # Base case: If both s and t are empty trees, 
        # they are considered the same.
        if not s and not t:
            return True
        # If s and t are non-empty and their root values are equal,
        # recursively check if their left and right subtrees are the same.
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        # If any of the conditions fail, the trees are not the same.
        return False