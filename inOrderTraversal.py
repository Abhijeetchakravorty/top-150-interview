class Solution:
    def inOrderTraversal(self, head):
        res = []
        st = []
        curr = head
        while True:
            while curr:
                st.append(curr)
                curr = curr.left
            
            if len(st) > 0:
                node = st.pop()
                res.append(node.val)
                curr = node.right
            
            if not curr and not st:
                break
        
        return res

