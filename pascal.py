class Solution:
    def pascal(self, n):
        a = [[1]]
        for i in range(1,n):
            numls = [x+y for x,y in zip([0]+a[i-1],a[i-1]+[0])]
            a.append(numls)
        return a
    
newArr = Solution().pascal(5)
print(newArr)