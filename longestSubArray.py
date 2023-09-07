class Solution:
    def longestSubArray(self, nums):
        prev = None
        curr = 0
        longest = 0
        for n in nums:
            if n:
                curr += 1
            else:
                if prev == None:
                    prev = 0
                longest = max(longest, prev + curr)
                prev = curr
                curr = 0
        if prev is None:
            return curr - 1
        return max(longest, prev + curr)

# nums = [0,1,1,1,0,1,1,0,1]
nums = [1, 1, 1]

print(Solution().longestSubArray(nums))