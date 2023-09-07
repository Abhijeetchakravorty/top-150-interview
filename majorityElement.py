class Solution:
    def majorityElement(self, nums):
        totalNums = len(nums)
        nums.sort()
        return nums[totalNums//2]
        