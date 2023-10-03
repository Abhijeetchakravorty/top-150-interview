# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Time Complexity : O(n)
    #Space Complexity: O(n)
    def diameterOfBinaryTree(self, root) -> int:
        # Initialize the result to store the maximum diameter found so far.
        res = 0

        # Define a recursive depth-first search (DFS) function.
        def dfs(root):
            nonlocal res  # Declare 'res' as a nonlocal variable to modify it within the function.

            # Base case: If the current node is None, return 0 (height of an empty subtree).
            if not root:
                return 0

            # Recursively calculate the height of the left subtree.
            left = dfs(root.left)

            # Recursively calculate the height of the right subtree.
            right = dfs(root.right)

            # Update 'res' with the maximum diameter found so far.
            # The diameter can be the path that passes through the current root node
            # (length = left height + right height) or the maximum diameter found in
            # its subtrees (maximum of 'res', 'left + right').
            res = max(res, left + right)

            # Return the height of the current subtree, which is the maximum height
            # between its left and right subtrees plus 1 (for the current node).
            return 1 + max(left, right)

        # Start the DFS traversal from the root of the binary tree.
        dfs(root)

        # 'res' now holds the maximum diameter of the binary tree.
        return res