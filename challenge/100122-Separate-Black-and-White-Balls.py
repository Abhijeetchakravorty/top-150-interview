class Solution:
    def minimumSteps(self, s):
        strList = list(s)
        start = 0
        end = 1
        step = 0
        while end < len(s):
            if strList[start] == "1" and strList[end] == "0":
                strList[start], strList[end] = strList[end], strList[start] 
                step += 1
                start += 1    
            else:
                start += 1    
            end += 1
    
        return step


a = Solution()
b = a.minimumSteps("101")
print("Ans: ", b)
11000111

a = Solution()
b = a.minimumSteps("100")
print("Ans: ", b)


a = Solution()
b = a.minimumSteps("1100000000111")
print("Ans: ", b)