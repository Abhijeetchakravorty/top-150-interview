class Solution:
        def generateParanthesis(self, n):
            res = []
            count = 0
            def dfs(left, right, s):
                nonlocal count
                
                if right==n:
                    res.append(s)
                else:
                    if left < n:
                        dfs(left+1, right, s+"(")
                    
                    if right < left:
                        dfs(left, right+1, s+")")
            dfs(0, 0, "")
            return res

a = Solution()
b = a.generateParanthesis(5)
print(b)


