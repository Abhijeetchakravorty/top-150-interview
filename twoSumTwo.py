class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers)-1
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum < target:
                left = left + 1
            elif curSum > target:
                right = right - 1
            else:
                return [left+1, right+1]
        return []
            
a = Solution()
b = a.twoSum([2,7,11,15], 9)
print(b)
b = a.twoSum([2,3,4], 6)
print(b)