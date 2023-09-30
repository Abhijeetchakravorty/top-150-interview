class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity : O(n) 
        # Space Complexity: O(min(n,m))
        repeats = dict()
        start = longest = 0

        for i, char in enumerate(s):
            if char in repeats and repeats[char] >= start: 
                start = repeats[char] + 1
            repeats[char] = i
            longest = max(longest, i-start+1)
        
        return longest
        


            

        


a = Solution()
b = a.lengthOfLongestSubstring("dvdf")
print(b)

b = a.lengthOfLongestSubstring("pwwkew")
print(b)

b = a.lengthOfLongestSubstring(" ")
print(b)