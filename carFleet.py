class Solution:
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p ) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



a = Solution()
b = a.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
print(b)