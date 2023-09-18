class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def validAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
        


a = Solution()
b = a.validAnagram("anagram", "nagaram")
print(b)