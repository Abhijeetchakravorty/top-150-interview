class Solution:
    def missingNumber(self, nums):
        res1 = sum(nums)
        res2 = len(nums) * (len(nums)+1) / 2
        return int(res2 - res1)