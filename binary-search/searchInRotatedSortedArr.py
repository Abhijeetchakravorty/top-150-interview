class Solution:
    def search(self, nums, target):
        # Time Complexity : O(log n) 
        # Space Complexity: O(1)
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1   
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
a = Solution()
b = a.search([4, 5, 6, 7, 0, 1, 2], 0)

print(b)


b = a.search([4, 5, 6, 7, 8, 9, 0, 1, 2], 9)

print(b)