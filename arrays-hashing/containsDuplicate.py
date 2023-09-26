class Solution:
    #time complexity: O(n)
    #space complexity: O(n)
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))