class Solution:
    def longestSubstringWithoutRepeatingChars(self, s):        
        newDict = dict()
        longest = start = 0
        for i, v in enumerate(s):
            if v in newDict and newDict[v] >= start:
                start = newDict[v]+1
                
            newDict[v] = i

            if longest < i - start + 1:
                longest = i - start + 1
        
        return longest
            



a = Solution()
b = a.longestSubstringWithoutRepeatingChars("abcdeabcdefgh")
print("Ans: ", b)

b = a.longestSubstringWithoutRepeatingChars(" ")
print("Ans: ", b)