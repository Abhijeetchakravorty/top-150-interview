class Solution:
    def search(self, nums, target: int):
        # Time Complexity : O(log n) 
        # Space Complexity: O(1)
        left = 0
        right = len(nums)-1

        while left <= right:
            #get the middle index and middle value
            mid = (left+right) // 2
            #case 1: return the middle index
            if nums[mid] == target:
                return mid
            #case 2: discard the smaller half
            elif nums[mid] < target:
                left = mid + 1
            
            #case 3: discard the larger half
            else:
                right = mid - 1
        
        return -1



a = Solution()
b = a.search([-7, -4, -1, 0, 3, 5, 9, 12], 9)
print(b)