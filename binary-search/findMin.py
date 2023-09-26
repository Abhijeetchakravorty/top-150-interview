class Solution:
    def findMin(self, nums):
        # Time Complexity : O(log n)	
        # Space Complexity: O(1)
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res







a = Solution()
# b = a.rotateRight([0,1,2,4,5,6,7])
# print(b)



b = a.findMin([3,4,5,1,2])
print(b)

b = a.findMin([4, 5, 6, 7, 0, 1, 2])
print(b)

b = a.findMin([11,13,15,17])
print(b)







































