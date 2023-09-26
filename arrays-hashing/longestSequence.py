class Solution:
    def longestConsecutive(self, nums):
        #Time Complexity : O(n)
        #Space Complexity: O(n)
        num_set = set(nums)
        res = 0
        for n in num_set:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                res = max(res, length)
        return res

       
            


a = Solution()
b = a.longestConsecutive([1, 2, 0, 1])
print("Ans:\n", b)
b = a.longestConsecutive([100,4,200,1,3,2])
print("Ans:\n", b)
b = a.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print("Ans:\n", b)
b = a.longestConsecutive([0,-1])
print("Ans:\n", b)
b = a.longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7])
print("Ans:\n", b)
b = a.longestConsecutive([0, 0, 1, 2, 3, 4, 5, 6, 7, 8])
print("Ans:R:\n", b)
b = a.longestConsecutive([1,2,0,1])
print("Ans:\n", b)
b = a.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])
print("Ans:\n", b)


