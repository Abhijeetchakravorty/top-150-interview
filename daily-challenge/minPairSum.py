class Solution:
    def minPairSum(self, nums):
        return nums.sort() or max(nums[i]+nums[-1-i] for i in range((len(nums)>>1)+1))

a = Solution()
b = a.minPairSum([3,5,2,3])
print("Ans: ", b)