class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def validAnagram(self, s, t):
        if len(s) != len(t):
            return False

        for j in set(s):
            if s.count(j) != t.count(j):
                return False
        
        return True
        


a = Solution()
b = a.validAnagram("anagram", "nagaram")
print(b)