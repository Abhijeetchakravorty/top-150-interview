class Solution:
    def maxArea(self, height) -> int:
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


a = Solution()
b = a.maxArea([1,8,6,2,5,4,8,3,7])
print(b)