class Solution:
    def productOfArrayExceptSelf(self, nums):
        res = [1]*len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for k in range(len(nums)-1, -1, -1):
            res[k] *= postfix
            postfix *= nums[k]
        
        return res



















# class Solution:
#     def productOfArrayExceptSelf(self, nums):
#         res = [1]*len(nums) #creating an array which has 1s
#         prefix = 1  #setting first prefix element which is the first index and comes before the 0th element

#         for i in range(len(nums)):      #looping through the list of nums
#             res[i] = prefix             # setting each element with the prefix
#             prefix *= nums[i]           # updating prefix element
        
#         print("Prefix: ", res)
#         print("Nums:   ", nums)
#         postfix = 1                             #creating postfix element
#         for j in range(len(nums)-1, -1, -1):    #looping over nums from the last
#             res[j] *= postfix                   #updating res array by multiplying prefix with the postfix
#             postfix *= nums[j]                  #

#         return res
a = Solution()
b = a.productOfArrayExceptSelf([1,2,3,4])
print(b)


b = a.productOfArrayExceptSelf([-1,1,0,-3,3])
print(b)
