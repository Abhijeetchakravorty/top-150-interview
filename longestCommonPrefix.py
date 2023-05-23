class Solution:
    def longestCommongPrefix(self, strs):
        m = min(strs)
        M = max(strs)
        
        res = ""
        for i in range(len(m)):
            if m[i] == M[i]:
                res += m[i]
            else:
                break
        return res