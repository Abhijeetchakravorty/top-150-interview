class Solution:
    #Floyd's Algorithm / Tortoise and Hare Algorithm
    def findDuplicate(self, nums):
        # Time Complexity : O(n)
        # Space Complexity: O(1)
        # Phase 1: Find the intersection point of the two pointers.
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        print("Slow:Fast", slow, fast)
        
        # Phase 2: Find the entrance to the cycle without modifying the array.
        # Reset one pointer to the start and advance both pointers one step at a time.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
a = Solution().findDuplicate([1,3,4,2,2])
print("Ans: ", a)