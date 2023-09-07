class Solution:
    def pascalsTriangle(self, nums):
        a = [[1]]
        for i in range(len(nums)):
            numls = [x+y for x, y in zip(
                [0]+a[i-1],
                a[i-1]+[0]
            )]
            a.append(numls)
        return a