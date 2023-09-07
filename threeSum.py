class Solution:
    #formula for adding all the nums    
    def threeSum(self, nums):
        res = []
        nums.sort()

        for k, v in enumerate(nums):
            if k > 0 and v == nums[k-1]:
                continue
            l, r = k+1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l - 1]) and l < r:
                        l+=1
        return res


a = Solution()
b = a.threeSum([-1,0,1,2,-1,-4])
print(b)
        

