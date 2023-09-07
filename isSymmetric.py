class Solution:
    def isSame(self, p, q):
        if p and q:
            return p.val==q.val and self.isSame(p.left, q.right) and self.isSame(p.right, q.left)
        return p is q

    def isSymmetric(self, root):
        if root:
            self.isSame(root.left, root.right)
        else:
            return True