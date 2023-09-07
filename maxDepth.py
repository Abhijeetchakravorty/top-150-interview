class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        max_depth = 0
        def dfs(node, depth):
            nonlocal max_depth
            if not node.right and not node.left:
                max_depth = max(depth, max_depth)
            
            if node.right:
                dfs(node.right, depth+1)
            
            if node.left:
                dfs(node.left, depth+1)

        dfs(root, 1)
        return max_depth