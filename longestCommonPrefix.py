class Solution:
    def longestCommonPrefix(self, strs):
        m = min(strs)
        M = max(strs)
        
        strD = ""
        for i in range(len(m)):
            if m[i]==M[i]:
                strD+=m[i]
            else:
                break
        return strD

        
a = Solution()
b = a.longestCommonPrefix(["abc", "abcefgh", "abcefgh", "abcefgh", "abcefgh", "abcefgh"])
print(b)