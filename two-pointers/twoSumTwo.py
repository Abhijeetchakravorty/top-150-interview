class Solution:
    def twoSum2(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            curSum = nums[left]+nums[right]
            if curSum < target:
                left += 1
            elif curSum > target:
                right -= 1
            else:
                return [1+left, 1+right]
        return []
