# Longest substring without repeating characters --> abcdefabcd 5
class Solution:
    def longestSub(self, s):
        ans = 0
        leftPointer = 0
        obj = dict() # {}
        for i, val in enumerate(s):
            if val in obj:
                if obj[val]+1 > leftPointer:
                    leftPointer = obj[val]+1
            obj[val] = i
            lengthSub = i+1-leftPointer
            if ans < lengthSub:
                ans = lengthSub
        return ans

a = Solution().longestSub("abcdefabcd")
print(a)
