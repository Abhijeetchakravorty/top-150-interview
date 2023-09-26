class Solution:
    def largestRectangleArea(self, heights):
        # Time Complexity : O(n)
        # Space Complexity: O(n)
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
            print("Stack: ", stack)
        
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

        
            

         



a = Solution()
b = a.largestRectangleArea([2,1,5,6,2,3])
print(b)

b = a.largestRectangleArea([2,4])
print(b)

b = a.largestRectangleArea([0])
print(b)


b = a.largestRectangleArea([0,9])
print(b)