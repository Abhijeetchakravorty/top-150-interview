class Solution:
    def twoSum(self, nums, target):
        #time complexity : O(n)
        #space complexity: O(n)
        numMap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []

a = Solution()
b = a.twoSum([1, 2, 3, 4, 5], 8)
print(b)
