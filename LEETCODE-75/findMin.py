class Solution:
    def findMin(self, nums):
        l=0
        r=len(nums)-1
        res = 0
        while l <= r:
            if (nums[l] < nums[r]):
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            res = min(nums[mid], res)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res

a = Solution().findMin([3,4,5,1,2])
print(a)