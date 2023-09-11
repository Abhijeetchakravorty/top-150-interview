class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        res = []
                    
        # for indx, h in enumerate(heights):
        #     stack.append((indx, h))
        #     left = indx
        #     right = left+1
        #     while left < right and right < len(heights):
        #         if(heights[left] <= heights[right]):
        #             res.append((right-indx+1)*stack[-1][1])
        #             right += 1
        #         else:
        #             res.append(1*stack[-1][1])
        #             stack.pop()
        # res.append(heights[len(heights)-1]*1)
        if len(heights) > 1:
            return max(res)
        else:
            return (heights[0]*1)





a = Solution()
b = a.largestRectangleArea([2,1,5,6,2,3])
print("Max Area: ", b)

b = a.largestRectangleArea([0])
print("Max Area: ", b)

b = a.largestRectangleArea([4, 2, 1])
print("Max Area: ", b)


b = a.largestRectangleArea([0, 9])
print("Max Area: ", b)

b = a.largestRectangleArea([2, 1,])
print("Max Area: ", b)