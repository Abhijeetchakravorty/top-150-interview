# Given:
#  Sorted array of distinct integers
#  A target value
#  return index if target is found
#  return index if target not found
#  Need to write O(log n) runtime

class Solution:
    def searchInsertPosition(self, nums, target):
        l=0
        r=len(nums)-1
        if target < nums[l]:
            return 0
        if target > nums[r]:
            return r+1
        if nums[l]==nums[r]:
            return l
        #First set the left and right pointers
        #Then find the middle element
        while l < r:
            mid = (l+r)//2
            #Check if the current element is greater than target then reduce right pointer
            if nums[mid] > target:
                r = mid - 1
            #Check if the current element is less than target then increase left pointer
            elif nums[mid] < target:
                l = mid + 1
            #Check if the current element is the target then return the index
            elif nums[mid] == target:
                return mid
            # In case nothing is found then we check our current index
            # The current mid index
            if(l+1 > r-1 or l > r or l==r):
                break
        mid = (l+r)//2
        print("I am here now: ", mid, l , r)
        if nums[mid] and nums[mid] < target:
            if nums[l+1] and nums[l+1] > target:
                return l+1
            else:
                return r+1
        if nums[mid] and nums[mid] > target:
            return l
        
        print("I am here: ", mid)
        return mid
            

a = Solution().searchInsertPosition([1,3,5,6], 2)
print("Ans:1 ", a)

a = Solution().searchInsertPosition([1,3,5,6], 4)
print("Ans:2 ", a)

a = Solution().searchInsertPosition([1,3], 2)
print("Ans:1 ", a)

a = Solution().searchInsertPosition([1], 1)
print("Ans:0 ", a)

a = Solution().searchInsertPosition([1, 2, 4, 6, 7], 3)
print("Ans:2 ", a)
         