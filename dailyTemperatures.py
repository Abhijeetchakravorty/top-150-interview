class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0]*len(temperatures)
        stack = [] #pair: [temperature, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t, i])
        return res
           
                


            



a = Solution()
b = a.dailyTemperatures([73,74,75,71,69,72,76,73])
print(b)

# b = a.dailyTemperatures([30,60,90])
# print(b)

