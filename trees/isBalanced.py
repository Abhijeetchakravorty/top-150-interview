# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time Complexity : O(N)
    # Space Complexity: O(H)
    def isBalanced(self, root) -> bool:
        # Define a DFS (Depth-First Search) 
        # function to calculate tree 
        # height and check balance.
        def dfs(root):
            # Base case: If the 
            # current node is None, 
            # return [True, 0] 
            # indicating a balanced subtree.
            if not root:
                return [True, 0]

            # Recursively check the left and 
            # right subtrees using DFS.
            left, right = dfs(root.left), dfs(root.right)

            # Check if both left and right 
            # subtrees are balanced and 
            # the height difference is <= 1.
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Return [balanced, height] where 'balanced' 
            # indicates whether the subtree is balanced,
            # and 'height' is the height of the current 
            # subtree (maximum height of left and right subtrees + 1).
            return [balanced, 1 + max(left[1], right[1])]

        # Start the DFS traversal from the 
        # root of the binary tree and return 
        # the balance result.
        return dfs(root)[0]
