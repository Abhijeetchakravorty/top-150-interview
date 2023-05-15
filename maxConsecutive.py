class Solution:
    def maxConsecutive(self, nums):
        result = 0
        count = 0
        for i in range(len(nums)):
            if (nums[i]==1):
                count += 1
            else:
                result = max(count, result)
                count = 0
        result = max(count, result)
        return result

a = Solution().maxConsecutive([1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1])
print(a)

# moneytor@design1234